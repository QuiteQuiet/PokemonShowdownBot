import json
import os
import yaml
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader
import re
import requests
import textwrap
from datetime import datetime
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
        self.title = self.format
        self.players = []
        self.winner = None
        self.runnerUp = None
        self.finals = None
        self.hasStarted = False
        self.startTime = None
        self.loggedParticipation = False
        self.bh = battleHandler

    def send(self, room, message):
        print('{room}|{msg}'.format(room = room, msg = message))
        self.ws.send('{room}|{msg}'.format(room = room, msg = message))

    def sendTourCmd(self, cmd):
        self.send(self.room.title, '/tour {}'.format(cmd))
    def join(self, room):
        self.send('', '/join {}'.format(room))

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
        elif 'join' in msg:
            self.players.append(Tournament.toId(msg[1]))
        elif 'leave' in msg:
            self.players.remove(Tournament.toId(msg[1]))
        elif 'start' in msg:
            self.startTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.logParticipation()
        elif 'update' in msg:
            info = json.loads(msg[1])
            if 'format' in info:
                self.title = info['format']
            if 'challenges' in info and info['challenges']:
                self.pickTeam()
                self.sendChallenge(info['challenges'][0])
            elif 'challenged' in info and info['challenged']:
                self.pickTeam()
                self.acceptChallenge()
            elif 'isStarted' in info:
                self.hasStarted = info['isStarted']
            try:
                if info['bracketData']['rootNode']['state'] == 'inprogress':
                    self.finals = info['bracketData']['rootNode']['room']
                    self.join(self.finals)
            except (KeyError, TypeError):
                pass # Expected to happen a lot
        elif 'battleend' in msg and self.finals:
            self.winner, self.runnerUp = msg[1:3]
            if msg[3] != 'win':
                self.winner, self.runnerUp = self.runnerUp, self.winner

            finalsroom = self.finals
            self.send(self.finals, '/savereplay')
            self.finals = 'https://replay.pokemonshowdown.com/{}'.format(self.finals[7:]) # len('battle-') == 7

    def logParticipation(self):
        rankPath = 'plugins/stats/{room}/{format}'.format(room = self.room.title, format = self.format)
        os.makedirs(rankPath, exist_ok = True)
        with open('{path}/tournament-rankings.yaml'.format(path = rankPath), 'a+') as yf:
            yf.seek(0, 0)
            data = yaml.load(yf, Loader = Loader)
            if not data: data = {}
            for player in self.players:
                player = Tournament.toId(player)
                if player not in data:
                    data[player] = {'entered': 1, 'won': 0}
                else:
                    data[player]['entered'] = data[player]['entered'] + 1
        with open('{path}/tournament-rankings.yaml'.format(path = rankPath), 'w') as yf:
            yaml.dump(data, yf, default_flow_style = False, explicit_start = True)
        self.loggedParticipation = True

    def logWin(self, winner):
        if not self.loggedParticipation: return # This may happen if the bot joins midway through a tournament
        rankPath = 'plugins/stats/{room}/{format}'.format(room = self.room.title, format = self.format)
        os.makedirs(rankPath, exist_ok = True)
        with open('{path}/tournament-rankings.yaml'.format(path = rankPath), 'a+') as yf:
            yf.seek(0, 0)
            data = yaml.load(yf, Loader = Loader)
            for user in winner:
                userData = data[Tournament.toId(user)]
                userData['won'] = userData['won'] + 1
        with open('{path}/tournament-rankings.yaml'.format(path = rankPath), 'w') as yf:
            yaml.dump(data, yf, default_flow_style = False, explicit_start = True)

def tourHandler(robot, room, *params):
    if 'create' in params[0]:
        room.createTour(robot.ws, params[1], robot.bh)

        if room.loading: return
        # Tour was created, join it if in supported formats
        if robot.details['joinTours'] and room.tour.format in robot.bh.supportedFormats:
            room.tour.joinTour()
    elif 'end' == params[0]:
        if not room.loading:
            winners, tier = room.getTourWinner(params[1])
            if robot.name in winners:
                message = 'I won the {form} tournament :o'.format(form = tier)
                if len(winners) > 1:
                    winners.remove(robot.name)
                    message += '\nCongratulations to {others} for also winning :)'.format(others = ', '.join(winners))
                robot.say(room.title, message, False)
            else:
                robot.say(room.title, 'Congratulations to {name} for winning :)'.format(name = ', '.join(winners)), False)
        room.endTour()
    elif 'forceend' in params[0]:
        room.endTour()
    else:
        # This is for general tournament updates
        if not room.tour or room.loading: return
        room.tour.onUpdate(params)

def queryresponse(robot, room, query, *data):
    data = '|'.join(data)
    if query == 'savereplay':
        roomName = 'battle-{room}'.format(room = json.loads(data)['id'])
        robot.leaveRoom(roomName)

def oldgentour(bot, cmd, msg, user, room):
    reply = ReplyObject('', True, True)
    if not room.tour: return reply.response('No tour is currently active, so this command is disabled.')
    if not room.tour.format.startswith('gen'): return reply.response("The current tour isn't a previous generation, so this command is disabled.")
    pastGens = {'gen1': 'RBY', 'gen2':'GSC', 'gen3':'RSE',  'gen4':'DPP'}
    warning = ''
    if room.tour.format[0:4] in pastGens: warning = "/wall Please note that bringing Pokemon that aren't **{gen} NU** will disqualify you\n".format(gen = pastGens[room.tour.format[0:4]])
    return reply.response(warning + "/wall Sample teams here: http://www.smogon.com/forums/threads/3562659/")

def tourhistory(bot, cmd, msg, user, room):
    reply = ReplyObject('', True)
    history = ''
    if msg:
        room = bot.getRoom(msg)
    for tour in room.pastTours:
        history += """
            Name: {name}
            Winner: {winner}
            Runner-Up: {runnerup}
            # of Participants: {players}
            Time: {starttime}
            Finals: {replay}\n""".format(
                name = tour.title,
                winner = tour.winner,
                runnerup = tour.runnerUp,
                players = len(tour.players),
                starttime = tour.startTime,
                replay = tour.finals)

    r = requests.post('https://pastebin.com/api/api_post.php',
                    data = {
                        'api_dev_key': bot.apikeys['pastebin'],
                        'api_option':'paste',
                        'api_paste_code': textwrap.dedent(history),
                        'api_paste_private': 0,
                        'api_paste_expire_date':'N'})
    if 'Bad API request' in r.text:
        return reply.response('Something went wrong ({error})'.format(error = r.text))
    return reply.response(r.text)

def getranking(bot, cmd, msg, user, room):
    reply = ReplyObject('', True, True)
    if not user.hasRank('%') and not room.isPM: reply.response('Listing the rankings require Room Driver (%) or higher.')

    # format is room (optional), format, user (if ever, also optional)
    parts = list(map(bot.toId, msg.split(',')))
    roomTitle = ''
    if os.path.exists('plugins/stats/{room}'.format(room=parts[0])):
        roomTitle = parts.pop(0)
    elif os.path.exists('plugins/stats/{room}'.format(room=room.title)):
        roomTitle = room.title
    else:
        return reply.response('The room {} has no data about rankings'.format(msg.split(',')[0]))

    if not parts:
        return reply.response('No format given')

    if os.path.exists('plugins/stats/{room}/{format}'.format(room=roomTitle, format=parts[0])):
        formatName = parts.pop(0)
        with open('plugins/stats/{}/{}/tournament-rankings.yaml'.format(roomTitle, formatName), 'r+') as yf:
            formatData = yaml.load(yf, Loader = Loader)
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
            return reply.response('{user} has no data for {tier} in {room}'.format(user = parts[0], tier = format, room = roomTitle))
    else:
        return reply.response('The room has no data about the format {}'.format(parts[0]))

# Exports
handlers = {
    'tournament': tourHandler,
    'queryresponse': queryresponse
}

commands = [
    Command(['oldgentour'], oldgentour),
    Command(['tourhistory'], tourhistory),
    Command(['showranking', 'leaderboard'], getranking)
]