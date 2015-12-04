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
import datetime

import prettyText
from room import Room
from plugins.battling.battleHandler import BattleHandler

class PokemonShowdownBot:
    ''' Controls the most basic aspects of connecting to Pokemon Showdown as well as commands '''

    def __init__(self, url, onMessage = None):
        with open("details.yaml", 'r') as yaml_file:
            self.details = yaml.load(yaml_file)
            self.Groups = {' ':0,'+':1,'★':1,'%':2,'@':3,'&':4,'#':5,'~':6}
            self.intro()
            self.splitMessage = onMessage if onMessage else self.onMessage
            self.url = url
            self.openWebsocket()
            self.bh = BattleHandler(self.ws, self.details['user'])
            self.ws.run_forever()

    def onError(self, ws, error):
        print(error)
    def onClose(self, message):
        print('Websocket closed')

    def onOpen(self, message):
        print('Websocket opened')

    def openWebsocket(self):
        self.ws = websocket.WebSocketApp(self.url,
                                         on_message = self.splitMessage,
                                         on_error = self.onError,
                                         on_close = self.onClose)
        self.ws.on_open = self.onOpen

    def intro(self):
        print(prettyText.intro)
    def log(self, sort, msg, user):
        print('{sort}: {cmd} (user: {user})'.format(sort = sort, cmd = msg, user = user))
    def userIsSelf(self, user):
        return self.details['user'] == user

    def send(self, msg):
        self.ws.send(msg)

    def login(self, challenge, challengekeyid):
        payload = { 'act':'login',
                    'name': self.details['user'],
                    'pass': self.details['password'],
                    'challengekeyid': challengekeyid,
                    'challenge': challenge
                    }
        r = requests.post('http://play.pokemonshowdown.com/action.php', data=payload)
        assertion = json.loads(r.text[1:])['assertion']

        if assertion:
            self.send(('|/trn '+ self.details['user']+',0,'+str(assertion)).encode('utf-8'))
            return True
        else:
            print('Assertion failed')
            return False

    def joinRoom(self, room, data = None):
        self.send('|/join ' + room)
        self.details['rooms'][room] = Room(room, data)
    def leaveRoom(self, room):
        ''' Attempts to leave a PS room '''
        if room not in self.details['rooms']:
            print('Error! {name} not in {room}'.format(name=self.details['user'], room=room))
            return False
        self.send('|/leave ' + room)
        self.details['rooms'].pop(room, None)
        return True
    def getRoom(self, roomName):
        alias = {'nu':'neverused', 'tsb':'thestable'}
        if roomName in alias:
            roomName = alias[roomName]
        return self.details['rooms'][roomName]

    def say(self, room, msg):
        if '\n' in msg:
            # DO NOT ABUSE THIS
            for m in msg.split('\n'):
                self.send('{room}|{text}'.format(room = room, text = m))
        else:
            self.send('{room}|{text}'.format(room = room, text = msg))
    def sendPm(self, user, msg):
        if '\n' in msg:
            # DO NOT ABUSE THIS
            for m in msg.split('\n'):
                self.send('|/pm {usr}, {text}'.format(usr = user, text = m))
        else:
            self.send('|/pm {usr}, {text}'.format(usr = user, text = msg))

    def reply(self, room, user, response, samePlace):
        if samePlace:
            self.say(room, response)
        else:
            self.sendPm(user['name'], response)

    def escapeText(self, line):
        if line[0] == '/':
            return '/' + line
        elif line[0] == '!':
            return ' ' + line
        return line
    def extractCommand(self, msg):
        return msg[len(self.details['command']):].split(' ')[0].lower()
    def evalPermission(self, user):
        return self.Groups[user['group']] >= self.Groups[self.details['broadcastrank']] or self.details['master'] == user['name'] or user['name'] in self.details['whitelist']
    def takeAction(self, room, user, action, reason):
        self.send('{room}|/{act} {user}, {reason}'.format(room = room, act = action, user = user, reason = reason))

    # Default onMessage if none is given (This only support logging in, nothing else)
    # To get any actual use from the bot, create a custom onMessage function.
    def onMessage(self, ws, message):
        if not message: return
        parts = message.split('|')
        if parts[1] == 'challstr':
            print('Attempting to log in...')
            self.login(message[3], message[2])
        elif parts[1] == 'updateuser':
            if self.details['user'] not in parts[2]: return
            if parts[3] == '1':
                print('Loged in...')

