import json
import glob
import os
import yaml
from collections import defaultdict
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
    def buildRankingsTable(data, metagame, people=10):
        top10 = sorted(data.items(), key = lambda x: (x[1]['won'], x[1]['won'] / x[1]['entered']), reverse = True)[:people]
        withWins = sum(person[1]['won'] > 0 for person in top10)
        htmlString = '<h1 style="font-size:1em;">{}</h1>'.format(metagame)
        htmlString += '<div style="height: {height}px; overflow-y: auto;">'.format(height=min(34 + 17 * withWins, 205))
        htmlString += '<table style="border-collapse: collapse; margin: 0; border: 1px solid black;">'
        htmlString += '<tr><th style="border: 1px solid black;">Rank</th>'
        htmlString += '<th style="border: 1px solid black;">Name</th>'
        htmlString += '<th style="border: 1px solid black;">Tours</th>'
        htmlString += '<th style="border: 1px solid black;">Games Won</th>'
        htmlString += '<th style="border: 1px solid black;">Game Wins / Tour</th>'
        htmlString += '<th style="border: 1px solid black;">Tours Won</th>'
        htmlString += '<th style="border: 1px solid black;">Tour Win%</th></tr>'
        rank = 1
        for person in top10:
            wins = person[1]['won']
            if wins < 1: continue
            entered = person[1]['entered']
            try:
                gamewins = person[1]['gamewins']
            except KeyError:
                gamewins = 'N/A'
            htmlString += '<tr style="{style} text-align: center;">'.format(style = 'background-color: #333333; color: #AAAAAA;' if rank % 2 == 0 else 'background-color: #AAAAAA; color: #333333;')
            htmlString += '<td>{rank}</td>'.format(rank=rank)
            htmlString += '<td>{player}</td>'.format(player=person[0]) if not person[0] == 'bb8nu' else '<td style="color: #CD853F">BB-8-NU</td>'
            htmlString += '<td>{played}</td>'.format(played=entered)
            htmlString += '<td>{gameswon}</td>'.format(gameswon=gamewins)
            try:
                htmlString += '<td>{percent:.1f}</td>'.format(percent=gamewins / entered)
            except TypeError:
                htmlString += '<td>N/A</td>'
            htmlString += '<td>{won}</td>'.format(won=wins)
            htmlString += '<td>{percent:.1f}</td></tr>'.format(percent=(wins / entered) * 100)
            rank += 1
        htmlString += '</table></div>'
        return htmlString

    @staticmethod
    def getTournamentData(room, formatName, official=False):
        if official:
            filePath = 'plugins/stats/{}/{}/official-rankings.yaml'.format(room, formatName)
        else:
            filePath = 'plugins/stats/{}/{}/tournament-rankings.yaml'.format(room, formatName)
        with open(filePath, 'r+') as yf:
            formatData = yaml.load(yf, Loader=Loader)
        return formatData

    def __init__(self, ws, room, tourFormat, battleHandler, official=False):
        self.ws = ws
        self.room = room
        self.format = tourFormat
        self.title = self.format
        self.official = official
        self.players = []
        self.gameWinners = defaultdict(int)
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
        elif 'battleend' in msg:
            winner, runnerUp = msg[1:3]
            if msg[3] != 'win':
                winner, runnerUp = runnerUp, winner
            # Count everyone's individual wins
            self.gameWinners[winner] += 1

            if self.finals:
                self.runnerUp = runnerUp
                self.send(self.finals, '/savereplay')
                self.finals = 'https://replay.pokemonshowdown.com/{}'.format(self.finals[7:]) # len('battle-') == 7

    def _logParticipationInner(self, fileDir, fileName):
        os.makedirs(fileDir, exist_ok=True)
        filePath = '{path}/{file}'.format(path=fileDir, file=fileName)
        with open(filePath, 'a+') as yf:
            yf.seek(0, 0)
            data = yaml.load(yf, Loader=Loader)
            if not data: data = {}
            for player in self.players:
                player = Tournament.toId(player)
                if player not in data:
                    data[player] = {'entered': 1, 'gamewins': 0, 'won': 0}
                else:
                    data[player]['entered'] = data[player]['entered'] + 1
        with open(filePath, 'w') as yf:
            yaml.dump(data, yf, default_flow_style=False, explicit_start=True)
        self.loggedParticipation = True

    def logParticipation(self):
        # All tours
        filePath = 'plugins/stats/{room}/{format}'.format(room=self.room.title, format=self.format)
        self._logParticipationInner(filePath, 'tournament-rankings.yaml')

        # Official tours
        if self.official:
            self._logParticipationInner(filePath, 'official-rankings.yaml')

    def _logWinsInner(self, winner, fileDir, fileName):
        if not self.loggedParticipation: return # This may happen if the bot joins midway through a tournament
        os.makedirs(fileDir, exist_ok=True)
        filePath = '{path}/{file}'.format(path=fileDir, file=fileName)
        with open(filePath, 'a+') as yf:
            yf.seek(0, 0)
            data = yaml.load(yf, Loader = Loader)
            # Tournament winner
            for user in winner:
                data[Tournament.toId(user)]['won'] += 1
            # Game winners
            for user in self.gameWinners:
                userData = data[Tournament.toId(user)]
                if 'gamewins' not in userData:
                    userData['gamewins'] = 0
                userData['gamewins'] += self.gameWinners[user]
        with open(filePath, 'w') as yf:
            yaml.dump(data, yf, default_flow_style = False, explicit_start = True)
    def logWins(self, winner):
        # All tours
        filePath = 'plugins/stats/{room}/{format}'.format(room=self.room.title, format=self.format)
        self._logWinsInner(winner, filePath, 'tournament-rankings.yaml')

        # Official tours
        if self.official:
            self._logWinsInner(winner, filePath, 'official-rankings.yaml')

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
            room.tour.winner = ', '.join(winners)
            if robot.name in winners:
                message = 'I won the {form} tournament :o'.format(form = tier)
                if len(winners) > 1:
                    winners.remove(robot.name)
                    message += '\nCongratulations to {others} for also winning :)'.format(others = ', '.join(winners))
                robot.say(room.title, message, False)
            else:
                robot.say(room.title, 'Congratulations to {name} for winning :)'.format(name = ', '.join(winners)), False)

            # This is a bit slow for large datasets, consider refactoring
            room.tour.logWins(winners)
            html = room.endTour()
            # HTML existing means we had an official tour
            if html:
                robot.say(room.title, '/addhtmlbox {}'.format(html))


    elif 'forceend' in params[0]:
        room.endTour()
    else:
        # This is for general tournament updates
        if not room.tour or room.loading: return
        room.tour.onUpdate(params)

def rawmessage(robot, room, *message):
    if not room.tour: return
    if not room.tour.official: return
    message = '|'.join(message)
    if 'Removed bans' in message or 'Added bans' in message:
        room.tour.official = False

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
    if not user.hasRank('%') and not room.isPM: return reply.response('Listing the rankings require Room Driver (%) or higher.')

    # format is room (optional), format, user (if ever, also optional)
    parts = list(map(Tournament.toId, msg.split(',')))
    roomTitle = ''
    if os.path.exists('plugins/stats/{room}'.format(room=parts[0])):
        roomTitle = parts.pop(0)
    elif os.path.exists('plugins/stats/{room}'.format(room=room.title)):
        roomTitle = room.title
    else:
        return reply.response('The room {} has no data about rankings'.format(msg.split(',')[0]))

    officialTour = cmd == 'officialleaderboard'

    if not parts and not officialTour:
        return reply.response('No format given')
    try:
        formatName = parts.pop(0)
    except IndexError:
        # Official tours has no format
        formatName = ''

    if os.path.exists('plugins/stats/{room}/{format}'.format(room=roomTitle, format=formatName)):
        formatData = Tournament.getTournamentData(roomTitle, formatName, officialTour)
    else:
        return reply.response('The room has no data about the format {}'.format(formatName))

    try:
        userData = formatData[parts[0]]
        try:
            gamewins = userData['gamewins']
        except KeyError:
            gamewins = 'N/A'
        return reply.response('{user} has played {games}, won {ind} games, and {wins} tours ({winrate:.1f}% tour win rate)'.format(user = parts[0], games = userData['entered'], ind = gamewins, wins = userData['won'], winrate = (userData['won'] / userData['entered']) * 100))
    except IndexError:
        rankingsTable = Tournament.buildRankingsTable(formatData, formatName)
        if bot.canHtml(room):
            return reply.response('/addhtmlbox {}'.format(rankingsTable))
        else:
            return reply.response('Cannot show full rankings in this room')
    except KeyError:
        return reply.response('{user} has no data for {tier} in {room}'.format(user = parts[0], tier = format, room = roomTitle))

def excludetour(bot, cmd, msg, user, room):
    reply = ReplyObject('', True, True)
    if not user.hasRank('%'): return reply.response('Permission denied. Room Driver (%) or higher')
    if not room.tour: return reply.response('No tournament found')
    room.tour.official = False

def resetofficials(bot, cmd, msg, user, room):
    reply = ReplyObject('', True, True)
    if not user.hasRank('@'): return reply.response('Permission denied. Room Mod (@) or higher')

    fileList = glob.glob('plugins/stats/{room}/*/official-rankings.yaml'.format(room=room.title))
    if not fileList:
        return reply.response('No official rankings to clear')
    try:
        for f in fileList:
            os.remove(f)
        return reply.response('Official rankings reset')
    except FileNotFoundError:
        return reply.response('Error while clearing official data')

# Exports
handlers = {
    'tournament': tourHandler,
    'queryresponse': queryresponse,
    'raw': rawmessage,
}

commands = [
    Command(['oldgentour'], oldgentour),
    Command(['tourhistory'], tourhistory),
    Command(['leaderboard', 'officialleaderboard'], getranking),
    Command(['excludetour'], excludetour),
    Command(['resetofficials'], resetofficials)
]