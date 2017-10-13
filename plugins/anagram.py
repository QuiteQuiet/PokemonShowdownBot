from data.pokedex import Pokedex
from data.moves import Moves
from data.abilities import Abilities
from plugins.games import GenericGame
from invoker import ReplyObject, Command

import re
import random
import datetime
import yaml

Scoreboard = {}
with open('plugins/scoreboard.yaml', 'a+') as yf:
    yf.seek(0, 0)
    Scoreboard = yaml.load(yf)
    if not Scoreboard: # Empty yaml file set Scoreboard to None, but a dict is expected
        Scoreboard = {}

class Anagram(GenericGame):
    def __init__(self):
        self.hints = []
        self.word, self.solution = self.newWord()
        self.startTime = datetime.datetime.now()
    def newWord(self):
        pokemon = list(Pokedex)
        moves = list(Moves)
        abilities = list(Abilities)
        pick = random.choice(pokemon+moves+abilities)
        if pick in Pokedex:
            self.hints.append("It's a pokemon!")
        elif pick in Moves:
            self.hints.append("It's a move!")
        elif pick in Abilities:
            self.hints.append("It's an ability!")
        self.hints.append("It begins with **{letter}**".format(letter = pick[0].upper()))
        pick = re.sub(r'[^a-zA-Z0-9]', '', pick.lower())
        anagram = list(pick)
        random.shuffle(anagram)
        return ''.join(anagram), pick
    def getHint(self):
        if not self.hints: return 'No more hints avaliable'
        hint = random.choice(self.hints)
        self.hints.remove(hint)
        return hint
    def getWord(self):
        return self.word
    def getSolvedWord(self):
        return self.solution
    def isCorrect(self, guess):
        return guess == self.solution
    def getSolveTimeStr(self):
        totalTime = datetime.datetime.now() - self.startTime
        if totalTime.seconds < 60:
            return ' in {time} seconds!'.format(time = totalTime.seconds)
        elif totalTime.seconds < 60 * 60: # Under 1 hour
            minutes = totalTime.seconds // 60
            return ' in {mins} minutes and {sec} seconds!'.format(mins = minutes, sec = totalTime.seconds-(minutes * 60))
        else:
            return '!'

def start(bot, cmd, msg, user, room):
    reply = ReplyObject('', True, False, False, True, True)
    if room.isPM and not cmd.startswith('score'): return reply.response("Don't try to play games in pm please")
    if msg == 'new':
        if not user.hasRank('%'): return reply.response('You do not have permission to start a game in this room. (Requires %)')
        if room.activity: return reply.response('A game is already running somewhere')
        if not room.allowGames: return reply.response('This room does not support chatgames.')
        room.activity = Anagram()
        return reply.response('A new anagram has been created (guess with ~a):\n' + room.activity.getWord())

    elif msg == 'hint':
        if room.activity: return reply.response('The hint is: ' + room.activity.getHint())
        return reply.response('There is no active anagram right now')
    elif msg == 'end':
        if not user.hasRank('%'): return reply.response('You do not have permission to end the anagram. (Requires %)')
        if not (room.activity and room.activity.isThisGame(Anagram)): return reply.response('There is no active anagram or a different game is active.')
        solved = room.activity.getSolvedWord()
        room.activity = None
        return reply.response('The anagram was forcefully ended by {baduser}. (Killjoy)\nThe solution was: **{solved}**'.format(baduser = user.name, solved = solved))

    elif msg.lower().startswith('score'):
        if msg.strip() == 'score': msg += ' {user}'.format(user = user.id)
        name = bot.toId(msg[len('score '):])
        if name not in Scoreboard: return reply.response("This user never won any anagrams")
        return reply.response('This user has won {number} anagram{plural}'.format(number = Scoreboard[name], plural = '' if not type(Scoreboard[name]) == str and Scoreboard[name] < 2  else 's'))
    else:
        if msg: return reply.response('{param} is not a valid parameter for ~anagram. Make guesses with ~a'.format(param = msg))
        if room.activity and room.activity.isThisGame(Anagram):
            return reply.response('Current anagram: {word}'.format(word = room.activity.getWord()))
        return reply.response('There is no active anagram right now')

def answer(bot, cmd, msg, user, room):
    reply = ReplyObject('', True, False, False, True, True)
    if not (room.activity and room.activity.isThisGame(Anagram)): return reply.response('There is no anagram active right now')
    if room.activity.isCorrect(re.sub(r'[ -]', '', msg).lower()):
        solved = room.activity.getSolvedWord()
        timeTaken = room.activity.getSolveTimeStr()
        room.activity = None
        # Save score
        Scoreboard[user.id] = 1 if user.id not in Scoreboard else Scoreboard[user.id] + 1
        with open('plugins/scoreboard.yaml', 'w') as ym:
            yaml.dump(Scoreboard, ym)
        return reply.response('Congratulations, {name} got it{time}\nThe solution was: {solution}'.format(name = user.name, time = timeTaken, solution = solved))
    return reply.response('{test} is wrong!'.format(test = msg.lstrip()))

commands = [
    Command(['anagram'], start),
    Command(['a'], answer)
]