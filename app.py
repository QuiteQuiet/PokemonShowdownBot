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

from robot import PokemonShowdownBot
from commands import Command, GameCommands

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
                

        # Joined new room
        elif 'users' in message[1]:
            self.getRoom(room).addUserlist(re.sub(r'[^a-zA-z0-9,]', '', message[2]).lower())

        elif 'j' in message[1].lower():
            if message[2][1:] == self.details['user']: self.getRoom(room).doneLoading()
            user = re.sub(r'[^a-zA-z0-9]', '', message[2]).lower()
            self.details['rooms'][room].addUser(user)
        elif 'l' in message[1].lower():
            user = re.sub(r'[^a-zA-z0-9]', '', message[2]).lower()
            self.details['rooms'][room].removeUser(user)
        elif 'n' in message[1].lower() and len(message[1]) < 3:
            newName = re.sub(r'[^a-zA-z0-9]', '', message[2]).lower()
            oldName = re.sub(r'[^a-zA-z0-9]', '', message[3]).lower()
            self.details['rooms'][room].renamedUser(oldName, newName)

 
        # Chat messages            
        elif 'c' in message[1].lower():
            user = {'name':re.sub(r'[^a-zA-z0-9]', '', message[3]).lower(),'group':message[3][0], 'unform': message[3][1:]}
            room = self.getRoom(room)
            if room.loading: return
            if user['name'] not in room.users: return
            if user['name'] == self.details['user']: return
            if message[4].startswith(self.details['command'] * 2): return

            if room.moderate:
                pass

            if message[4].startswith(self.details['command']):            
                command = message[4][1:].split()[0].lower()
                self.log(message[4], user['name'])
                response, samePlace = self.do(self, command, message[4][len(command) + 1:], user)

                if not room.allowGames and command in self.gameCommands:
                    response = 'This room does not support chatgames'

                if self.evalPermission(user) or command in self.gameCommands:
                    if response:
                        self.reply(room.title, user, response, samePlace)
                    else:
                        self.reply(room.title, user, '{cmd} is not a valid command.'.format(cmd = command), samePlace)
                else:
                    self.sendPm(user['name'], 'Please pm the commands for a response')

        elif 'pm' in message[1].lower():
            user = {'name':re.sub(r'[^a-zA-z0-9]', '', message[2]).lower(),'group':message[2][0], 'unform': message[3][1:]}
            if user['name'] == self.details['user']: return

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
                response, where = self.do(self, command, params, user)
                if command in self.gameCommands:
                    if params.startswith('new,'):
                        room = params[len('new,'):].split(',')[0].replace(' ','')
                        self.reply(room, user, response, where)
                    
                if response:
                    self.sendPm(user['name'], response)
                else:
                    self.sendPm(user['name'], '{cmd} is not a valid command.'.format(cmd = command))

            

psb = PSBot()
