import json
import yaml
import re
from random import randint
import robot as r

class Tournament:

    @staticmethod
    def toId(thing): return re.sub(r'[^a-zA-z0-9,]', '', thing).lower()

    @staticmethod
    def buildRankingsTable(data, metagame):
        htmlString = '<h1 style="font-size:1em;">{}</h1><ol>'.format(metagame)
        top10 = sorted(data.items(), key = lambda x: x[1]['won'], reverse = True)[:10]
        for person in top10:
            wins = person[1]['won']
            if wins < 1: continue
            htmlString += '<li>{player}: {score} wins</li>'.format(player = person[0], score = wins)
        htmlString += '</ol>'
        return htmlString

    def __init__(self, ws, room, tourFormat, battleHandler):
        self.ws = ws
        self.room = room
        self.format = tourFormat
        self.players = []
        self.hasStarted = False
        self.bh = battleHandler

    def sendTourCmd(self, cmd):
        self.ws.send('{room}|/tour {cmd}'.format(room = self.room.title, cmd = cmd))
    def joinTour(self):
        self.sendTourCmd('join')
    def leaveTour(self):
        self.sendTourCmd('leave')

    def sendChallenge(self, opponent):
        self.sendTourCmd('challenge {opp}'.format(opp = opponent))
    def acceptChallenge(self):
        self.sendTourCmd('acceptchallenge')
    def pickTeam(self):
        team = self.bh.getRandomTeam(self.format)
        if team:
            self.ws.send('|/utm {}'.format(team))
    def onUpdate(self, msg):
        if 'updateEnd' in msg : return
        elif 'join'in msg:
            self.players.append(Tournament.toId(msg[1]))
        elif 'leave' in msg:
            self.players.remove(Tournament.toId(msg[1]))
        elif 'start' in msg:
            self.logParticipation()
        elif 'update' in msg:
            info = json.loads(msg[1])
            if 'challenges' in info and info['challenges']:
                self.pickTeam()
                self.sendChallenge(info['challenges'][0])
            elif 'challenged' in info and info['challenged']:
                self.pickTeam()
                self.acceptChallenge()
            elif 'isStarted' in info:
                self.hasStarted = info['isStarted']

    def logParticipation(self):
        with open('plugins/tournament-rankings.yaml', 'a+') as yf:
            yf.seek(0, 0)
            data = yaml.load(yf)
            if not data: data = {}
            if self.room.title not in data: data[self.room.title] = {}
            if self.format not in data[self.room.title]: data[self.room.title][self.format] = {}
            roomFormatData = data[self.room.title][self.format]
            for player in self.players:
                player = Tournament.toId(player)
                if player not in roomFormatData:
                    roomFormatData[player] = {'entered': 1, 'won': 0}
                else:
                    roomFormatData[player]['entered'] = roomFormatData[player]['entered'] + 1
            data[self.room.title][self.format] = roomFormatData
        with open('plugins/tournament-rankings.yaml', 'w') as yf:
            yaml.dump(data, yf, default_flow_style = False, explicit_start = True)

    def logWin(self, winner):
        with open('plugins/tournament-rankings.yaml', 'a+') as yf:
            yf.seek(0, 0)
            data = yaml.load(yf)
            for user in winner:
                userData = data[self.room.title][self.format][Tournament.toId(user)]
                userData['won'] = userData['won'] + 1
        with open('plugins/tournament-rankings.yaml', 'w') as yf:
            yaml.dump(data, yf, default_flow_style = False, explicit_start = True)

def oldgentour(bot, cmd, room, msg, user):
    reply = r.ReplyObject('', True, True)
    if not room.tour: return reply.response('No tour is currently active, so this command is disabled.')
    if not room.tour.format.startswith('gen'): return reply.response("The current tour isn't a previous generation, so this command is disabled.")
    pastGens = {'gen1': 'RBY', 'gen2':'GSC', 'gen3':'RSE',  'gen4':'DPP'}
    warning = ''
    if room.tour.format[0:4] in pastGens: warning = "/wall Please note that bringing Pokemon that aren't **{gen} NU** will disqualify you\n".format(gen = pastGens[room.tour.format[0:4]])
    return reply.response(warning + "/wall Sample teams here: http://www.smogon.com/forums/threads/3562659/")

def getranking(bot, cmd, room, msg, user):
    reply = r.ReplyObject('', True, True)
    if not user.hasRank('%'): reply.response('Listing the rankings require Room Driver (%) or higher.')
    # format is room (optional), format, user (if ever, also optional)
    with open('plugins/tournament-rankings.yaml', 'r+') as yf:
        yf.seek(0, 0)
        data = yaml.load(yf)

    parts = bot.removeSpaces(msg).split(',')
    try:
        roomData = data[parts[0]]
        parts.pop(0)
    except KeyError:
        roomData = data[room.title]
    try:
        formatData = roomData[parts[0]]
        parts.pop(0)
        try:
            userData = formatData[parts[0]]
            return reply.response('{user} has played {games} and won {wins} ({winrate}% win rate)'.format(user = parts[0], games = userData['entered'], wins = userData['won'], winrate = userData['won'] // userData['entered']))
        except:
            rankingsTable = Tournament.buildRankingsTable(formatData, msg)
            if bot.canHtml(room):
                return reply.response('/addhtmlbox {}'.format(rankingsTable))
            else:
                return reply.response('Cannot show rankings in this room')
    except:
        return reply.response('This room has no rankings in this format :(')
