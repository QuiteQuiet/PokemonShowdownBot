import json
import yaml
import re
from random import randint
from invoker import ReplyObject, Command

class Tournament:

    @staticmethod
    def toId(thing): return re.sub(r'[^a-zA-Z4e310-9,]', '', thing).lower()

    @staticmethod
    def buildRankingsTable(data, metagame):
        htmlString = '<h1 style="font-size:1em;">{}</h1>'.format(metagame)
        htmlString += '<table style="border-collapse: collapse; margin: 0; border: 1px solid black; width: 100%;}">'
        htmlString += '<tr><th style="border: 1px solid black;">Rank</th>'
        htmlString += '<th style="border: 1px solid black;">Name</th>'
        htmlString += '<th style="border: 1px solid black;">Tours</th>'
        htmlString += '<th style="border: 1px solid black;">Wins</th>'
        htmlString += '<th style="border: 1px solid black;">Win%</th></tr>'
        top10 = sorted(data.items(), key = lambda x: (x[1]['won'], x[1]['won'] / x[1]['entered']), reverse = True)[:10]
        rank = 1
        for person in top10:
            wins = person[1]['won']
            if wins < 1: continue
            entered = person[1]['entered']
            htmlString += '<tr style="{style} text-align: center;">'.format(style = 'background-color: #333333; color: #AAAAAA;' if rank % 2 == 0 else 'background-color: #AAAAAA; color: #333333;')
            htmlString += '<td>{rank}</td>'.format(rank = rank)
            htmlString += '<td>{player}</td>'.format(player = person[0]) if not person[0] == 'bb8nu' else '<td style="color: #CD853F">BB-8-NU</td>'
            htmlString += '<td>{played}</td>'.format(played = entered)
            htmlString += '<td>{won}</td>'.format(won = wins)
            htmlString += '<td>{percent:.1f}</td></tr>'.format(percent = (wins / entered) * 100)
            rank += 1
        htmlString += '</table>'
        return htmlString

    def __init__(self, ws, room, tourFormat, battleHandler):
        self.ws = ws
        self.room = room
        self.format = tourFormat
        self.players = []
        self.hasStarted = False
        self.loggedParticipation = False
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
            data = yaml.load(yf, Loader = yaml.CLoader) # This file might be large, and CLoader has better performance
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
        self.loggedParticipation = True

    def logWin(self, winner):
        if not self.loggedParticipation: return # This may happen if the bot joins midway through a tournament
        with open('plugins/tournament-rankings.yaml', 'a+') as yf:
            yf.seek(0, 0)
            data = yaml.load(yf, Loader = yaml.CLoader) # This file might be large, and CLoader has better performance
            for user in winner:
                userData = data[self.room.title][self.format][Tournament.toId(user)]
                userData['won'] = userData['won'] + 1
        with open('plugins/tournament-rankings.yaml', 'w') as yf:
            yaml.dump(data, yf, default_flow_style = False, explicit_start = True)

def oldgentour(bot, cmd, msg, user, room):
    reply = ReplyObject('', True, True)
    if not room.tour: return reply.response('No tour is currently active, so this command is disabled.')
    if not room.tour.format.startswith('gen'): return reply.response("The current tour isn't a previous generation, so this command is disabled.")
    pastGens = {'gen1': 'RBY', 'gen2':'GSC', 'gen3':'RSE',  'gen4':'DPP'}
    warning = ''
    if room.tour.format[0:4] in pastGens: warning = "/wall Please note that bringing Pokemon that aren't **{gen} NU** will disqualify you\n".format(gen = pastGens[room.tour.format[0:4]])
    return reply.response(warning + "/wall Sample teams here: http://www.smogon.com/forums/threads/3562659/")

def getranking(bot, cmd, msg, user, room):
    reply = ReplyObject('', True, True)
    if not user.hasRank('%') and not room.isPM: reply.response('Listing the rankings require Room Driver (%) or higher.')
    # format is room (optional), format, user (if ever, also optional)
    with open('plugins/tournament-rankings.yaml', 'r+') as yf:
        yf.seek(0, 0)
        data = yaml.load(yf, Loader = yaml.CLoader) # This file might be large, and CLoader has better performance

    parts = list(map(bot.toId, msg.split(',')))
    roomTitle = ''
    try:
        roomData = data[parts[0]]
        roomTitle = parts.pop(0)
    except KeyError:
        roomData = data[room.title] if room.title in data else None
    try:
        formatData = roomData[parts[0]]
        format = parts.pop(0)
        try:
            userData = formatData[parts[0]]
            return reply.response('{user} has played {games} and won {wins} ({winrate:.1f}% win rate)'.format(user = parts[0], games = userData['entered'], wins = userData['won'], winrate = (userData['won'] / userData['entered']) * 100))
        except IndexError:
            rankingsTable = Tournament.buildRankingsTable(formatData, format)
            if bot.canHtml(room):
                return reply.response('/addhtmlbox {}'.format(rankingsTable))
            else:
                return reply.response('Cannot show full rankings in this room')
        except KeyError:
            return reply.response('{user} has no data for {tier} in {room}'.format(user = parts[0], tier = format, room = roomTitle if roomTitle else room.title))
    except TypeError:
        return reply.response('The room {} has no data about rankings'.format(msg.split(',')[0]))
    except IndexError:
        return reply.response('No format given')
    except KeyError:
        return reply.response('The room has no data about the format {}'.format(parts[0]))

commands = [
    Command(['oldgentour'], oldgentour),
    Command(['showranking', 'leaderboard'], getranking)
]