from data.pokedex import Pokedex
from data.moves import Moves
from data.abilities import Abilities
import re
import random
import datetime

class Anagram:
    def __init__(self):
        self.hint = ''
        self.word, self.solution = self.newWord()
        self.startTime = datetime.datetime.now()
    def newWord(self):
        pokemon = list(Pokedex)
        moves = list(Moves)
        abilities = list(Abilities)
        pick = random.sample(pokemon+moves+abilities, 1)[0]
        if pick in Pokedex:
            self.hint = "It's a pokemon!"
        elif pick in Moves:
            self.hint = "It's a move!"
        elif pick in Abilities:
            self.hint = "It's an ability!"
        pick = re.sub(r'[^a-zA-Z0-9]', '', pick.lower())
        anagram = list(pick)
        random.shuffle(anagram)
        return ''.join(anagram), pick
    def getHint(self):
        return self.hint
    def getWord(self):
        return self.word
    def getSolvedWord(self):
        return self.solution
    def isCorrect(self, guess):
        return guess == self.solution
    def getSolveTimeStr(self): 
        totalTime = datetime.datetime.now() - self.startTime
        if totalTime.seconds < 60: # Less than 1 minute to solve
            return ' in {time} seconds!'.format(time = totalTime.seconds)
        elif totalTime.seconds < 60*60: # Under 1 hour
            minutes = totalTime.seconds//60
            return ' in {mins} minutes and {sec} seconds!'.format(mins = minutes, sec = totalTime.seconds-(minutes*60))
        else:
            return '!'
