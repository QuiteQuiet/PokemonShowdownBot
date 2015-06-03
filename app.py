# This is the entry point for the Pokemon Showdown Bot, and contain most of the
# permission checks for chat returns.
#
# It's derived from the base class PokemonShowdownBot, and as such hide a lot of
# it's core functions by simply calling functions from the base class.
# For any function called here not defined in this file, look in robot.py.
#
# Changes to this file should be made with caution, as much of the extended functions
# depend on this being structured in a specific way.

import re
import json

from robot import PokemonShowdownBot
from commands import Command, GameCommands
from plugins.tournaments import supportedFormats
from plugins import moderation

class PSBot(PokemonShowdownBot):
    def __init__(self):
        self.do = Command
        self.gameCommands = GameCommands
        PokemonShowdownBot.__init__(self,
                                    'ws://sim.smogon.com:8000/showdown/websocket',
                                    self.splitMessage)

    def splitMessage(self, ws, message):
        if not message: return
        if '\n' not in message: self.parseMessage(message, '')

        room = ''
        msg = message.split('\n')
        if msg[0].startswith('>'):
            room = msg[0][1:]
        msg.pop(0)

        if room.startswith('battle-'):
            if room not in self.details['rooms']:
                # Battle rooms don't need the same interface as chatrooms
                self.details['rooms'][room] = True
            if 'leave|{me}'.format(me = self.details['user']) == msg[0]:
                self.details['rooms'].pop(room)
            # Go to battle handler instead of regular rooms
            # (we don't allow commands in battle rooms anyway)
            for m in msg:
                self.bh.parse(room, m)
            return

        for m in msg:
            self.parseMessage(m, room)

    def parseMessage(self, msg, room):
        if not msg.startswith('|'): return
        message = msg.split('|')

       
        # Logging in
        if message[1] == 'challstr':
            print('{name}: Attempting to login...'.format(name = self.details['user']))
            self.login(message[3], message[2])

        elif message[1] == 'updateuser':
            if self.details['user'] not in message[2]: return
            if message[3] not in '1':
                print('login failed, still guest')
                print('crashing now; have a nice day :)')
                exit()

            if self.details['avatar'] >= 0:
                self.send('|/avatar {num}'.format(num = self.details['avatar']))
            print('{name}: Successfully logged in.'.format(name = self.details['user']))
            for room in self.details['joinRooms']:
                name = [n for n in room][0] # joinRoom entry is a list of dicts
                self.joinRoom(name, room[name])

        # Challenges
        elif 'updatechallenges' in message[1]:
            challs = json.loads(message[2])
            if challs['challengesFrom']:
                opp = [name for name, form in challs['challengesFrom'].items()][0]
                if challs['challengesFrom'][opp] == 'battlecup1v1':
                    self.send('|/accept {name}'.format(name = opp))
                else:
                    self.sendPm(opp, 'Sorry, I only accept challenges in Battle Cup 1v1 :(')

        # This is a safeguard for l and n in case that a moderation action happen
        elif 'unlink' == message[1]:
            return

        # Joined new room
        elif 'users' in message[1]:
            users = ','.join([u[0]+re.sub(r'[^a-zA-z0-9,]', '',u[1:]).lower() for u in message[2].split(',') if message[2].split(',').index(u) > 0])
            self.getRoom(room).addUserlist(users)

        elif 'j' in message[1].lower():
            if self.userIsSelf(message[2][1:]): self.getRoom(room).doneLoading()
            user = re.sub(r'[^a-zA-z0-9]', '', message[2]).lower()
            self.details['rooms'][room].addUser(user, message[2][0])
        elif 'l' in message[1].lower():
            if self.userIsSelf(message[2][1:]): return
            user = re.sub(r'[^a-zA-z0-9]', '', message[2]).lower()
            self.details['rooms'][room].removeUser(user)
        elif 'n' in message[1].lower() and len(message[1]) < 3:
            newName = message[2][0] + re.sub(r'[^a-zA-z0-9]', '', message[2]).lower()
            oldName = re.sub(r'[^a-zA-z0-9]', '', message[3]).lower()
            self.details['rooms'][room].renamedUser(oldName, newName)

 
        # Chat messages            
        elif 'c' in message[1].lower():
            user = {'name':re.sub(r'[^a-zA-z0-9]', '', message[3]).lower(),'group':message[3][0], 'unform': message[3][1:]}
            room = self.getRoom(room)
            if room.loading: return
            if user['name'] not in room.users: return
            if self.userIsSelf(user['unform']): return

            if room.moderate:
                if moderation.containUrl(message[4]):
                    url = moderation.getUrl(message[4])
                    if moderation.badLink(url):
                        if self.Groups[user['group']] >= self.Groups['%']: return
                        action, reason = moderation.getAction(user, 'badlink')
                        self.log(action, user['name'])
                        self.takeAction(room.title, user['name'], action, reason)

            #if re.search(r'(whats?|who).+(suspe[ck]+t|test(ed|ing))', message[4], flags=re.I):
            #    self.say(room.title, "{user}, Magneton".format(user = user['unform']))

            if message[4].startswith(self.details['command']) and message[4][1:] and message[4][1].isalpha():            
                command = message[4][1:].split()[0].lower()
                self.log(message[4], user['name'])

                response, samePlace = '', True
                # If the command was a chat game and permissions aren't met, kill the game (even if it just started)
                if command in self.gameCommands:
                    if not room.allowGames:
                        response = 'This room does not support chatgames.'
                    if 'new' in message[4] and command in ['hangman']:
                        response = "Please use Pm to start a hangman game."
                        
                if not response:
                    response, samePlace = self.do(self, command, message[4][len(command) + 1:].lstrip(), user)

                if self.evalPermission(user) or command in self.gameCommands:
                    if response:
                        self.reply(room.title, user, response, samePlace)
                    else:
                        self.reply(room.title, user, '{cmd} is not a valid command.'.format(cmd = command), samePlace)
                else:
                    self.sendPm(user['name'], 'Please pm the commands for a response.')

        elif 'pm' in message[1].lower():
            user = {'name':re.sub(r'[^a-zA-z0-9]', '', message[2]).lower(),'group':message[2][0], 'unform': message[2][1:]}
            if self.userIsSelf(user['unform']): return

            if message[4].startswith('/invite'):
                if not message[4][8:] == 'lobby':
                    if self.Groups[user['group']] >= 1:
                        self.joinRoom(message[4][8:])
                        self.log(message[4], user['name'])
                    else:
                        self.sendPm(user['name'], 'Only global voices (+) and up can add me to rooms, sorry :(')

            if message[4].startswith(self.details['command']):
                command = message[4][1:].split(' ')[0].lower()
                self.log(message[4], user['name'])
                params = message[4][len(command) + 1:].lstrip()

                response, where = '', False
                if command in self.gameCommands:
                    if params.startswith('new,'):
                        room = params[len('new,'):].split(',')[0].replace(' ','')
                        if not self.getRoom(room).allowGames:
                            response = 'This room does not support chat games'
                        else:
                            user['group'] = self.getRoom(room).users[user['name']]
                            response, where = self.do(self, command, params, user)
                            self.reply(room, user, response, where)
                            return
                if not response:
                    response, where = self.do(self, command, params, user)
                    
                if response:
                    self.sendPm(user['name'], response)
                else:
                    self.sendPm(user['name'], '{cmd} is not a valid command.'.format(cmd = command))

        # Tournaments
        elif self.details['joinTours'] and 'tournament' in message[1]:
            if self.getRoom(room).loading: return
            if 'create' in message[2]:
                # Tour was created, join it if in supported formats
                room = self.getRoom(room)
                if not room.tour:
                    room.createTour(self.ws)
                if room.tour and message[3] in supportedFormats:
                    room.tour.joinTour()
                else:
                    self.say(room.name, "Can't join tour, unsupported format or previous tour not deleted from room.")
            elif 'end' == message[2]:
                winner, tier = self.getRoom(room).tour.getWinner(message[3])
                if self.details['user'] in winner:
                    self.say(room, 'I won the {form} tournament :o'.format(form = tier))
                else:
                    self.say(room, 'Congratulations to {name} for winning :)'.format(name = ', '.join(winner)))
                self.getRoom(room).endTour()
            elif 'forceend' in message[2]:
                self.getRoom(room).endTour()
                self.say(room, "Aww, now nobody will win :(")
            else:
                if self.getRoom(room).tour:
                    self.getRoom(room).tour.onUpdate(message[2:])
            

psb = PSBot()
