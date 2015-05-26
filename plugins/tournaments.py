import json
from random import randint

supportedFormats = ['battlecup1v1']

class Tournament:
    def __init__(self, ws, roomName):
        self.ws = ws
        self.room = roomName
        self.hasStarted = False
        

    def sendTourCmd(self, cmd):
        self.ws.send('{room}|/tour {cmd}'.format(room = self.room, cmd = cmd))
        pass
    def joinTour(self):
        self.sendTourCmd('join')
    def leaveTour(self):
        self.sendTourCmd('leave')
    def getWinner(self, msg):
        things = json.loads(msg)
        return things['results'], things['format']

    def sendChallenge(self, opponent):
        self.sendTourCmd('challenge {opp}'.format(opp = opponent))
    def acceptChallenge(self, opponent):
        self.sendTourCmd('accept {opp}'.format(opp = opponent))
    def onUpdate(self, msg):
        if msg == 'updateEnd': return
        if msg == 'update':
            info = json.loads(msg)
            if 'challenges' in info:
                self.sendChallenge(info['challenges'][randint(0,len(info['challenges'])-1)])
            elif 'challengeBys' in info:
                self.acceptChallenge(info['challengeBys'][randint(0,len(info['challengeBys'])-1)])
            elif 'isStarted' in info:
                self.hasStarted = info['isStarted']
        pass
    
