# This is the master class for the Python PS bot.
# Every general-purpose command is included in this file, with the sole exception
# being onMessage(), as derived applications may need to acces this function.
#
# As such, unless a valid onMessage() function is supplied when creating an
# instance, this will not run.
#
# To run this, the following modules are required:
# PyYAML == 3.11
# requests == 2.5.1
# simplejson == 3.6.5
# websocket-client == 0.23.0

import websocket
import requests
import json
import yaml
from time import sleep
from collections import defaultdict
import datetime
import re
import importlib
import pkgutil
import traceback

from room import Room
from user import User
from plugins.battling.battleHandler import BattleHandler

# Module global for automatically update help with the correct symbol in plugins.
# This will be change from default on creation of every instance of PokemonShowdownBot!
guidechar = ' '

class PokemonShowdownBot:
    ''' Controls the most basic aspects of connecting to Pokemon Showdown as well as commands '''

    def __init__(self, url):
        global guidechar
        try:
            with open("details.yaml", 'r') as yaml_file:
                self.details = yaml.load(yaml_file)
        except FileNotFoundError:
            self.loadDefaults()

        self.owner = self.toId(self.details['master'])
        self.apikeys = self.details['apikeys']
        self.name = self.details['user']
        self.id = self.toId(self.name)
        self.rooms = {}
        self.commandchar = self.details['command']
        self.startTime = None
        self.intro()
        self.handlers = defaultdict(list)
        self.collectHandlers()
        self.url = url
        #websocket.enableTrace(True)
        self.openConnection()
        guidechar = self.commandchar

    def onError(self, ws, error):
        print('Websocket Error:', error)
    def onClose(self, message):
        self.rooms = {}
        print('Websocket closed')

    def onOpen(self, message):
        print('Websocket opened')

    def openConnection(self):
        if not self.url: return
        self.ws = websocket.WebSocketApp(self.url,
                                         on_message = self.onMessage,
                                         on_error = self.onError,
                                         on_close = self.onClose)
        self.ws.on_open = self.onOpen
        self.bh = BattleHandler(self.ws, self.name)

    def closeConnection(self):
        self.ws.close()
        self.ws = None

    def listen(self):
        self.ws.run_forever(ping_interval = 120)

    def loadDefaults(self):
        import shutil
        shutil.copy('details-example.yaml', 'details.yaml')
        with open("details.yaml", 'r') as yaml_file:
                self.details = yaml.load(yaml_file)

    def intro(self):
        print('+~~~~~~~~~~~~~~~~~~~~~~~~+')
        print('|  Pokemon Showdown Bot  |')
        print('|      Created by:       |')
        print('|      Quite Quiet       |')
        print('+~~~~~~~~~~~~~~~~~~~~~~~~+')
    def log(self, sort, msg, user):
        print('{sort}: {cmd} (user: {user})'.format(sort = sort, cmd = msg, user = user))
    def userIsSelf(self, user):
        return self.name == user

    def send(self, msg):
        self.ws.send(msg)

    def login(self, challenge, challengekeyid):
        print('Attempting to log in...')
        if self.name == 'username' and self.details['password'] == 'password':
            print('Error: Login details still at default; will not proceed with execution!')
            exit()

        payload = { 'act':'login',
                    'name': self.name,
                    'pass': self.details['password'],
                    'challengekeyid': challengekeyid,
                    'challenge': challenge
                    }
        r = requests.post('http://play.pokemonshowdown.com/~~showdown/action.php', data=payload)
        assertion = json.loads(r.text[1:])['assertion']

        if assertion:
            self.send('|/trn {name},0,{assertion}'.format(name = self.name, assertion = str(assertion)).encode('utf-8'))
            return True
        else:
            print('Assertion failed')
            return False

    def updateUser(self, name, result):
        name = self.removeAfkMessage(name)
        if self.name not in name: return
        if not result == '1':
            print('login failed, still guest')
            print('crashing now; have a nice day :)')
            exit(1)

        self.startTime = datetime.datetime.now()
        if int(self.details['avatar']) >= 0:
            self.send('|/avatar {num}'.format(num = self.details['avatar']))
        print('{name}: Successfully logged in.'.format(name = self.name))
        for room in self.details['joinRooms']:
            print('{name}: Autojoining room {room}'.format(name = self.name, room = room))
            self.joinRoom(room, self.details['joinRooms'][room])

    def joinRoom(self, room, data = None):
        if room in self.rooms: return
        self.send('|/join ' + room)
        self.rooms[room] = Room(room, data)

    def leaveRoom(self, room):
        ''' Attempts to leave a PS room '''
        if room not in self.rooms:
            print('Error! {name} not in {room}'.format(name = self.name, room = room))
            return False
        self.send('|/leave ' + room)
        return True
    def getRoom(self, roomName):
        alias = {'nu':'neverused'}
        if roomName in alias:
            roomName = alias[roomName]
        return self.rooms[roomName] if roomName in self.rooms else None

    def say(self, room, msg, ignoreMultiline = False):
        if '\n' in msg and not ignoreMultiline:
            for m in msg.split('\n'):
                self.send('{room}|{text}'.format(room = room, text = m))
        else:
            self.send('{room}|{text}'.format(room = room, text = msg))
    def sendPm(self, user, msg, ignoreMultiline = False):
        if '\n' in msg:
            if not ignoreMultiline:
                for m in msg.split('\n'):
                    self.send('|/pm {usr}, {text}'.format(usr = user, text = m))
            else:
                msg = msg.replace('\n', '\n/pm {},'.format(user))
                self.send('|/pm {usr}, {text}'.format(usr = user, text = msg))
        else:
            self.send('|/pm {usr}, {text}'.format(usr = user, text = msg))

    def reply(self, room, user, response, samePlace, ignoreMultiline = False):
        if samePlace:
            self.say(room, response, ignoreMultiline)
        else:
            self.sendPm(user.id, response)

    # Helpful functions
    def toId(self, thing):
        return re.sub(r'[^a-zA-Z0-9,]', '', thing).lower()
    def removeAfkMessage(self, user):
        return user.split('@')[0]
    def escapeText(self, line):
        if line[0] == '/':
            return '/' + line
        elif line[0] == '!':
            return ' ' + line
        return line
    def removeSpaces(self, text):
        return text.replace(' ','')
    def extractCommand(self, msg):
        return msg[len(self.commandchar):].split(' ')[0].lower()
    def escapeMessage(self, message):
        for harmful in ['\u202e']:
            message = message.replace(harmful, harmful.encode('unicode_escape').decode('ascii'))
        return message

    def takeAction(self, room, user, action, reason):
        self.log('Action', action, user.id)
        self.send('{room}|/{act} {user}, {reason}'.format(room = room, act = action, user = user.id, reason = reason))

    # Rank checks
    def canBroadcast(self, room):
        return User.compareRanks(room.rank, '+')
    def canPunish(self, room):
        return User.compareRanks(room.rank, '%')
    def canBan(self, room):
        return User.compareRanks(room.rank, '@')
    def canStartTour(self, room):
        return User.compareRanks(room.rank, '@')
    def canHtml(self, room):
        return User.compareRanks(room.rank, '*')

    # Generic permissions test for users
    def isOwner(self, name):
        return self.owner == self.toId(name)
    def userHasPermission(self, user, rank):
        return self.isOwner(user.id) or User.compareRanks(user.rank, rank)

    def saveDetails(self, newAutojoin = False):
        details = {k:v for k,v in self.details.items() if not k == 'rooms' and not k == 'joinRooms'}
        details['joinRooms'] = {}
        for e in self.rooms:
            if e.startswith('groupchat'): continue
            if not newAutojoin and e not in self.details['joinRooms']: continue
            room = self.getRoom(e)
            details['joinRooms'][e] = {'moderate': room.moderation.config,
                                        'allow games':room.allowGames,
                                        'tourwhitelist': room.tourwhitelist
                                        }
        with open('details.yaml', 'w') as yf:
            yaml.dump(details, yf, default_flow_style = False, explicit_start = True)

    def _iterPackages(self):
        for importer, modname, ispkg in pkgutil.walk_packages(path = ['.'], onerror = lambda x: None):
            yield importer, modname, ispkg

    def addHandler(self, name, func):
        self.handlers[name].append(func)

    def collectHandlers(self):
        print('Loading handlers...')
        self.addHandler('challstr', lambda s, r, cid, cstr: self.login(cstr, cid))
        self.addHandler('updateuser', lambda s, r, u, n, a, e: self.updateUser(u, n))

        failedTrees = []
        for importer, modname, ispkg in self._iterPackages():
            # skip subtrees of a failed import
            if [subtree for subtree in failedTrees if modname.startswith(subtree)]: continue
            try:
                importedModule = importlib.import_module(modname)
                try:
                    # Look through the module and see if any handlers have been defined
                    handlers = getattr(importedModule, 'handlers')
                    try:
                        for protocol, func in handlers.items():
                            self.addHandler(protocol, func)
                    except TypeError as e:
                        # The module had a `commands` entry that was of an unexpected type
                        # Mainly a safeguard towards importing native Python packages by mistake
                        print('Module {} had an incompatible type for `handlers`; type(handlers) == {}; Skipping subtree...'.format(modname, type(handlers)))
                        failedTrees.append(modname)
                    print('Loaded {count} handlers from {module}'.format(count = len(handlers), module = modname))
                except AttributeError:
                    # Module contains no handlers, this is expected and should be ignored
                    pass
            except ImportError as e:
                # Something went horribly wrong
                print(modname)
                traceback.print_tb(e.__traceback__)
                print(e)

    def onMessage(self, ws, message):
        if not message: return

        roomName = ''
        if '\n' in message:
            message = message.split('\n')
            if message[0].startswith('>'):
                roomName = message[0][1:]
            message.pop(0)
        else:
            message = [message]

        room = self.getRoom(roomName)
        # we got messages from a room we aren't in?
        if not room:
            if not roomName:
                room = Room('Empty')
            else:
                room = self.rooms[roomName] = Room(roomName)

        for msg in message:
            if not msg.startswith('|'): continue
            _, identifier, *params = self.escapeMessage(msg).split('|')
            identifier = identifier.lower()

            try:
                # Go through handlers and resolve them one by one
                for handler in self.handlers[identifier]:
                    handler(self, room, *params)
            except KeyError:
                pass # expected to happen a lot
            except Exception as e:
                traceback.print_tb(e.__traceback__)
                print(e)
                print('MESSAGE THAT CAUSED IT:\n{}'.format(msg))
