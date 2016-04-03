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
import time

from robot import PokemonShowdownBot
from commands import Command, GameCommands, IgnoreBroadcastPermission, CanPmReplyCommands, IgnoreEscaping
from plugins.battling.battleHandler import supportedFormats
from plugins import moderation
from plugins.messages import MessageDatabase
from plugins.workshop import Workshop

class PSBot(PokemonShowdownBot):
    def __init__(self):
        self.do = Command
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
            if 'deinit' in msg[0]:
                self.details['rooms'].pop(room)
            # Go to battle handler instead of regular rooms
            # (we don't allow commands in battle rooms anyway)
            for m in msg:
                self.bh.parse(room, m)
            return

        for m in msg:
            self.parseMessage(m, room)

    def updateUser(self, name, result):
        if self.details['user'] not in name: return
        if not result == '1':
            print('login failed, still guest')
            print('crashing now; have a nice day :)')
            exit()

        if self.details['avatar'] >= 0:
            self.send('|/avatar {num}'.format(num = self.details['avatar']))
        print('{name}: Successfully logged in.'.format(name = self.details['user']))
        for rooms in self.details['joinRooms']:
            name = [n for n in rooms][0] # joinRoom entry is a list of dicts
            self.joinRoom(name, rooms[name])

    def handleJoin(self, room, message):
        if self.userIsSelf(message[1:]):
            self.details['rooms'][room.title].rank = message[0]
            room.doneLoading()
        user = re.sub(r'[^a-zA-z0-9]', '', message).lower()
        if moderation.shouldBan(self, room.moderate, user, room.title):
            self.takeAction(room.title, user, 'roomban', "You are blacklisted from this room, so please don't come here.")
            return
        self.details['rooms'][room.title].addUser(user, message[0])
        # If the user have a message waiting, tell them that in a pm
        if self.usernotes.shouldNotifyMessage(user):
            self.sendPm(user, self.usernotes.pendingMessages(user))

    def parseMessage(self, msg, roomName):
        if not msg.startswith('|'): return
        message = msg.split('|')
        room = self.getRoom(roomName)

        # Logging in
        if message[1] == 'challstr':
            print('{name}: Attempting to login...'.format(name = self.details['user']))
            self.login(message[3], message[2])

        elif message[1] == 'updateuser':
            self.updateUser(message[2], message[3])

        # Challenges
        elif 'updatechallenges' in message[1]:
            challs = json.loads(message[2])
            if challs['challengesFrom']:
                opp = [name for name, form in challs['challengesFrom'].items()][0]
                if challs['challengesFrom'][opp] in supportedFormats:
                    self.send('|/accept {name}'.format(name = opp))
                else:
                    self.sendPm(opp, 'Sorry, I only accept challenges in Challenge Cup 1v1, Random Battles or Battle Factory :(')
        elif 'updatesearch' in message[1]:
            # This gets sent before `updatechallenges` does when recieving a battle, but it's
            # not useful for anything, so just return straight away
            return

        # This is a safeguard for l and n in case that a moderation action happen
        elif 'unlink' == message[1] or 'uhtml' in message[1] or 'html' == message[1]:
            return

        # As long as the room have a roomintro (whih even groupchats do now)
        # Roomintros are also the last thing that is sent when joining a room
        # so when this show up, assume the room is loaded
        elif 'raw' == message[1]:
            if message[2].startswith('<div class="infobox infobox-roomintro"><div class="infobox-limited">'):
                room.doneLoading()

        # Joined new room
        elif 'users' in message[1]:
            room.makeUserlist(message[2])
            # If PS doesn't tell us we joined, this still give us our room rank
            room.rank = message[2][message[2].index(self.details['user']) - 1]

        elif 'j' in message[1].lower():
            self.handleJoin(room, message[2])

        elif 'l' == message[1].lower() or 'leave' == message[1].lower():
            if self.userIsSelf(message[2][1:]):
                # This is just a failsafe in case the bot is forcibly removed from a room.
                # Any other memory release required is handeled by the room destruction
                if roomName in self.details['rooms']:
                    self.details['rooms'].pop(roomName)
                return
            user = re.sub(r'[^a-zA-z0-9]', '', message[2]).lower()
            room.removeUser(user)
        elif 'n' in message[1].lower() and len(message[1]) < 3:
            # Keep track of your own rank
            # When demoting / promoting a user the server sends a |N| message to update the userlist
            if message[2][1:] == self.details['user']:
                room.rank = message[2][0]
            newName = message[2][0] + re.sub(r'[^a-zA-z0-9]', '', message[2]).lower()
            oldName = re.sub(r'[^a-zA-z0-9]', '', message[3]).lower()
            room.renamedUser(oldName, newName)


        # Chat messages
        elif 'c' in message[1].lower():
            user = {'name':re.sub(r'[^a-zA-z0-9]', '', message[3]).lower(),'group':message[3][0], 'unform': message[3][1:]}
            if room.loading: return
            if user['name'] not in room.users: return
            if self.userIsSelf(user['unform']): return

            if room.moderate and moderation.canPunish(self, room.title):
                anything = moderation.shouldAct(message[4], user, room, message[2])
                if anything:
                    action, reason = moderation.getAction(self, room.title, user, anything, message[2])
                    self.log('Action', action, user['name'])
                    self.takeAction(room.title, user['name'], action, reason)


            if message[4].startswith(self.details['command']) and message[4][1:] and message[4][1].isalpha():
                command = self.extractCommand(message[4])
                self.log('Command', message[4], user['name'])

                response, samePlace = '', True
                # If the command was a chat game and permissions aren't met, kill the game (even if it just started)
                if command in GameCommands:
                    if not room.allowGames:
                        response = 'This room does not support chatgames.'
                    if 'new' in message[4] and command in ['hangman']:
                        response = "Please use Pm to start a hangman game."

                if not response:
                    response, samePlace = self.do(self, command, room.title, message[4][len(command) + 1:].lstrip(), user)
                if response == 'NoAnswer': return

                if self.evalPermission(user) or command in IgnoreBroadcastPermission:
                    if command not in IgnoreEscaping:
                        response = self.escapeText(response)
                    self.reply(room.title, user, response, samePlace)

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
                        self.log('Invite', message[4], user['name'])
                    else:
                        self.sendPm(user['name'], 'Only global voices (+) and up can add me to rooms, sorry :(')

            if message[4].startswith(self.details['command']) and message[4][1:] and message[4][1].isalpha():
                command = self.extractCommand(message[4])
                self.log('Command', message[4], user['name'])
                params = message[4][len(command) + len(self.details['command']):].lstrip()

                response, where = '', False
                if command in GameCommands:
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
                    response, where = self.do(self, command, 'pm', params, user)

                if response:
                    self.sendPm(user['name'], response)
                else:
                    self.sendPm(user['name'], '{cmd} is not a valid command.'.format(cmd = command))

        # Tournaments
        elif 'tournament' == message[1]:
            if room.loading: return
            if 'create' in message[2]:
                if not room.tour:
                    room.createTour(self.ws, message[3])
                # Tour was created, join it if in supported formats
                if not self.details['joinTours']: return
                if room.tour and room.tour.format in supportedFormats:
                    room.tour.joinTour()
            elif 'end' == message[2]:
                if not room.tour: return
                winner, tier = room.tour.getWinner(message[3])
                if self.details['user'] in winner:
                    self.say(room.title, 'I won the {form} tournament :o'.format(form = tier))
                else:
                    self.say(room.title, 'Congratulations to {name} for winning :)'.format(name = ', '.join(winner)))
                room.endTour()
            elif 'forceend' in message[2]:
                room.endTour()
            else:
                if room.tour:
                    room.tour.onUpdate(message[2:])


psb = PSBot()
restartCount = 0
while restartCount < 100:
    # This function has a loop that runs as long as the websocket is connected
    psb.ws.run_forever()
    # If we get here, the socket is closed and disconnected
    # so we have to reconnect and restart (after waiting a bit of course, say half a minute)
    # (At least, that's the theory)
    time.sleep(30)
    print('30 seconds since last disconnect. Retrying connection...')
    psb.openWebsocket()
    psb.addBattleHandler()
    # We have websocket.run_forever earlier, so just loop around here
    # but count the total number of restarts we managed for debug purposes.
    restartCount += 1
    print('Restart Count:', restartCount)

