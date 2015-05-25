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
# websockets == 2.4

import websocket
import requests
import json
import yaml
import datetime

from room import Room
import prettyText

class PokemonShowdownBot:
    ''' Controls the most basic aspects of connecting to Pokemon Showdown as well as commands '''

    def __init__(self, url, onMessage):
        with open("details.yaml", 'r') as yaml_file:
            self.details = yaml.load(yaml_file)
            self.Groups = {' ':0,'+':1,'%':2,'@':3,'&':4,'#':5,'~':6}
            self.splitMessage = onMessage
            self.intro()
            self.ws = websocket.WebSocketApp(url,
                                             on_message = onMessage,
                                             on_error = self.onError,
                                             on_close = self.onClose)
            self.ws.on_open = self.onOpen
            self.ws.run_forever()

    def onError(self, code, error):
        print(code, ':', error)
    def onClose(self, message):
        print('websocket closed')
    def onOpen(self, message):
        print('websocket opened')
        
    def intro(self):
        print(prettyText.intro)
    def log(self, msg, user):
        print('Command: {cmd} (from user: {user})'.format(cmd = msg, user = user))
        
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
        return self.details['rooms'][roomName]

    def say(self, room, msg):
        if '\n' in msg:
            # DO NOT ABUSE THIS
            for m in msg.split('\n'):
                self.ws.send('{room}|{text}'.format(room = room, text = m))
        else:
            self.ws.send('{room}|{text}'.format(room = room, text = msg))
    def sendPm(self, user, msg):
        self.ws.send('|/pm {usr}, {text}'.format(usr = user, text = msg))

    def reply(self, room, user, response, samePlace):
        if self.evalPermission(user) and samePlace:
            self.say(room, response)
        else:
            self.sendPm(user['name'], response)

    def evalPermission(self, user):
        return self.Groups[user['group']] >= self.Groups[self.details['broadcastrank']] or self.details['master'] == user['name'] or user['name'] in self.details['whitelist']
    def takeAction(self, room, user, action, reason):
        self.ws.send('{room}|/{act} {user}, {reason}'.format(room = room, act = action, user = user, reason = reason))
        
