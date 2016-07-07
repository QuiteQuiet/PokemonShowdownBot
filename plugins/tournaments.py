import json
from random import randint

class Tournament:
    def __init__(self, ws, roomName, tourFormat):
        self.ws = ws
        self.room = roomName
        self.format = tourFormat
        self.hasStarted = False


    def sendTourCmd(self, cmd):
        self.ws.send('{room}|/tour {cmd}'.format(room = self.room, cmd = cmd))
    def joinTour(self):
        self.sendTourCmd('join')
    def leaveTour(self):
        self.sendTourCmd('leave')

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

def oldgentour(bot, cmd, room, msg, user):
    if not room.tour: return 'No tour is currently active, so this command is disabled.', True
    if not room.tour.format.startswith('gen'): return "The current tour isn't a previous generation, so this command is disabled.", True
    pastGens = {'gen1': 'RBY', 'gen2':'GSC', 'gen3':'RSE',  'gen4':'DPP'}
    warning = ''
    if room.tour.format[0:4] in pastGens: warning = "/wall Please note that bringing Pokemon that aren't **{gen} NU** will disqualify you\n".format(gen = pastGens[room.tour.format[0:4]])
    return warning + "/wall Sample teams here: http://www.smogon.com/forums/threads/3562659/", True