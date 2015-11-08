import json
from random import randint

class Tournament:
    def __init__(self, ws, roomName):
        self.ws = ws
        self.room = roomName
        self.hasStarted = False
        

    def sendTourCmd(self, cmd):
        self.ws.send('{room}|/tour {cmd}'.format(room = self.room, cmd = cmd))
    def joinTour(self):
        self.sendTourCmd('join')
    def leaveTour(self):
        self.sendTourCmd('leave')
    def getWinner(self, msg):
        things = json.loads(msg)
        return things['results'][0], things['format']

    def sendChallenge(self, opponent):
        self.sendTourCmd('challenge {opp}'.format(opp = opponent))
    def acceptChallenge(self):
        self.sendTourCmd('acceptchallenge')
    def onUpdate(self, msg):
        if 'updateEnd' in msg : return
        if 'update' in msg:
            info = json.loads(msg[1])
            if 'challenges' in info and info['challenges']:
                self.sendChallenge(info['challenges'][0])
            elif 'challenged' in info and info['challenged']:
                self.acceptChallenge()
            elif 'isStarted' in info:
                self.hasStarted = info['isStarted']
