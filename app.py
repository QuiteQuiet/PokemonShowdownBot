# This is the entry point for the Pokemon Showdown Bot, and contain most of the
# permission checks for chat returns.
#
# It's derived from the base class PokemonShowdownBot, and as such hide a lot of
# it's core functions by simply calling functions from the base class.
# For any function called here not defined in this file, look in robot.py.
#
# Changes to this file should be made with caution, as much of the extended functions
# depend on this being structured in a specific way.
#
# Extended notes:
# user:
#     user objects are dicts containing some information about the user who said anything.
#     This information consists of user['name'], user['group'], and user['unform']. user['name'] is
#     a format-removed id of the speaker with only a-z lowercase and 0-9 present.
#
#     user['group'] contain the auth level of the user, as a single character string of
#     either ' ', +, %, @, &, #, or ~. To compare groups against each other self.Groups have
#     the information required when used like: self.Groups[user['group']] for a numeric value.
#
#     Lastly, user['unform'] is the unaltered name as seen in the chatrooms, and can be used
#     for things like replying, but shouldn't be used for comparisions.

import re
import json

from robot import PokemonShowdownBot
from commands import Command, GameCommands, CanPmReplyCommands
from plugins.battling.battleHandler import supportedFormats
from plugins import moderation
from plugins.messages import MessageDatabase
from plugins.workshop import Workshop

class PSBot(PokemonShowdownBot):
    def __init__(self):
        self.do = Command
        self.gameCommands = GameCommands
        self.usernotes = MessageDatabase()
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
                if challs['challengesFrom'][opp] in supportedFormats:
                    self.send('|/accept {name}'.format(name = opp))
                else:
                    self.sendPm(opp, 'Sorry, I only accept challenges in Challenge Cup 1v1, Random Battles or Battle Factory :(')

        # This is a safeguard for l and n in case that a moderation action happen
        elif 'unlink' == message[1]:
            return

        # Joined new room
        elif 'users' in message[1]:
            users = ','.join([u[0]+re.sub(r'[^a-zA-z0-9,]', '',u[1:]).lower() for u in message[2].split(',') if message[2].split(',').index(u) > 0])
            self.getRoom(room).addUserlist(users)

        elif 'j' in message[1].lower():
            if self.userIsSelf(message[2][1:]):
                self.details['rooms'][room].rank = message[2][0]
                self.getRoom(room).doneLoading()
            user = re.sub(r'[^a-zA-z0-9]', '', message[2]).lower()
            self.details['rooms'][room].addUser(user, message[2][0])
            # If the user have a message waiting, send that message in a pm
            if self.usernotes.hasMessage(user):
                self.sendPm(user, self.usernotes.getMessage(user))
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

            if room.moderate and moderation.canPunish(self, room.title):
                anything = moderation.shouldAct(message[4], user, room.title, message[2])   
                if anything:
                    action, reason = moderation.getAction(user, anything, message[2])
                    # If the current rank isn't allowed to roomban, keep hourmuting them
                    if action == 'roomban' and not moderation.canBan(self, room.title):
                        action = 'hourmute'
                    self.log(action, user['name'])
                    self.takeAction(room.title, user['name'], action, reason)


            if message[4].startswith(self.details['command']) and message[4][1:] and message[4][1].isalpha():            
                command = self.extractCommand(message[4])
                self.log(message[4], user['name'])

                response, samePlace = '', True
                # If the command was a chat game and permissions aren't met, kill the game (even if it just started)
                if command in self.gameCommands:
                    if not room.allowGames:
                        response = 'This room does not support chatgames.'
                    if 'new' in message[4] and command in ['hangman']:
                        response = "Please use Pm to start a hangman game."
                        
                if not response:
                    response, samePlace = self.do(self, command, room.title, message[4][len(command) + 1:].lstrip(), user)
                if response == 'NoAnswer': return

                if self.evalPermission(user) or command in self.gameCommands:
                    if response:
                        self.reply(room.title, user, self.escapeText(response), samePlace)
                    else:
                        self.reply(room.title, user, '{cmd} is not a valid command.'.format(cmd = command), samePlace)
                elif command in CanPmReplyCommands:
                    self.sendPm(user['name'], self.escapeText(response))
                else:
                    self.sendPm(user['name'], 'Please pm the commands for a response.')

            if type(room.game) == Workshop:
                room.game.logSession(room.title, user['group'] + user['unform'], message[4])
                

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

            if message[4].startswith(self.details['command']) and message[4][1:] and message[4][1].isalpha():
                command = self.extractCommand(message[4])
                self.log(message[4], user['name'])
                params = message[4][len(command) + len(self.details['command']):].lstrip()

                response, where = '', False
                if command in self.gameCommands:
                    if params.startswith('new,'):
                        room = params[len('new,'):].split(',')[0].replace(' ','')
                        if not self.getRoom(room).allowGames:
                            response = 'This room does not support chat games'
                        else:
                            user['group'] = self.getRoom(room).users[user['name']]
                            response, where = self.do(self, command, room, params, user)
                            self.reply(room, user, response, where)
                            return
                    elif params.startswith('score'):
                        response, where = self.do(self, command, 'pm', params, user)
                    else:
                        response = "Don't try to play games in pm please"
                if not response:
                    response, where = self.do(self, command, 'room', params, user)
                    
                if response:
                    self.sendPm(user['name'], response)
                else:
                    self.sendPm(user['name'], '{cmd} is not a valid command.'.format(cmd = command))

        # Tournaments
        elif 'tournament' == message[1]:
            if self.getRoom(room).loading: return
            if 'create' in message[2]:
                # Tour was created, join it if in supported formats
                if not self.details['joinTours']: return
                room = self.getRoom(room)
                if not room.tour:
                    room.createTour(self.ws)
                if room.tour and message[3] in supportedFormats:
                    room.tour.joinTour()
            elif 'end' == message[2]:
                if not self.getRoom(room).tour: return
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
