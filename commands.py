# The command file for every external command not specifically for running
# the bot. Even more relevant commands like broadcast options and whitelists
# are treated as such.
#
# Every command in here should follow the basic structure of:
# elif cmd == 'commandHere':
#     doYourThings(lots, of, variables)
#     return 'Your Response', True/False
#
# True: Allows that the command in question can, if gotten from a room,
#       be returned to the same room rather than a PM.
# False: This will ALWAYS return the reply as a PM, no matter where it came from

from random import randint, sample
import re
import yaml
import json
import math # For funsies

from data.tiers import tiers, formats
from data.links import Links
from data.pokedex import Pokedex
from data.types import Types
from data.replies import Lines

from plugins.games import Hangman, Anagram

GameCommands = ['hangman', 'hg', 'anagram']

def Command(self, cmd, msg, user):
    ''' Returns the reply if the command exists, and False if it doesn't '''
    # Debug commands and program info
    if cmd == 'echo':
        return msg, True
    elif cmd in ['source', 'git']:
        return 'Source code can be found at: {url}blob/master/README.md'.format(url = getURL()), False
    elif cmd == 'credits':
        return 'Credits can be found: {url}'.format(url = getURL()), True
    elif cmd in ['commands', 'help']:
        return 'Read about commands here: {url}blob/master/COMMANDS.md'.format(url = getURL()), False
    elif cmd == 'leave':
        msg = msg.replace(' ','')
        if self.leaveRoom(msg):
            return 'Leaving room {r} succeeded'.format(r = msg), False
        else:
            return 'Could not leave room: {r}'.format(r = msg), False
    elif cmd == 'get':
        if isMaster(self, user):
            return str(eval(msg)), True
        else:
            return 'You do not have permisson to use this command. (Only for owner)', False
    # Save current self.details to details.yaml (moves rooms to joinRooms)
    elif cmd == 'savedetails':
        saveDetails(self)
        return 'Details saved.', False

    # Permissions
    elif cmd == 'broadcast':
        return 'Rank required to broadcast: {rank}'.format(rank = self.details['broadcastrank']), True
    elif cmd == 'setbroadcast':
        msg = msg.replace(' ','')
        if msg in self.Groups or msg in ['off', 'no', 'false']:
            if canChange(self, user):
                if msg in ['off', 'no', 'false']: msg = ' '
                if self.details['broadcastrank'] == msg:
                    return 'Broadcast rank is already {rank}'.format(rank = msg), True
                else:
                    self.details['broadcastrank'] = msg
                    return 'Broadcast rank set to {rank}. (This is not saved on reboot)'.format(rank = msg), True
            else:
                return 'You are not allowed to set broadcast rank. (Requires #)', False
        else:
            return '{rank} is not a valid rank'.format(rank = msg), False
    elif cmd == 'whitelist':
        if canSee(self, user):
            if self.details['whitelist']:
                return ' ,'.join(self.details['whitelist']), False
            else:
                return 'Whitelist is empty :(', False
        else:
            return 'You are not allowed to see the whitelist :l (Requires %)', False
    elif cmd in ['whitelistuser', 'wluser']:
        if canAddUser(self, user):
            self.details['whitelist'].append(msg)
            return 'User {usr} added to whitelist.'.format(usr = msg), True
    elif cmd == 'removewl':
        if canAddUser(self, user):
            self.details['whitelist'].remove(msg)
            return 'User {usr} removed from the whitelist.'.format(usr =msg), True

    elif cmd == 'allowgames':
        if canChange(self, user):
            msg = msg.replace(' ','')
            things = msg.split(',')
            if len(things) == 2:
                if things[0] in self.details['rooms']:
                    if things[1] in ['true','yes','y','True']:
                        if not self.details['rooms'][things[0]].allowGames:
                            self.details['rooms'][things[0]].allowGames = True
                            return 'Chatgames are now allowed in {room}'.format(room = things[0]), True
                        else:
                            return 'Chatgames are already allowed in {room}'.format(room = things[0]), True
                    elif things[1] in ['false', 'no', 'n',' False']:
                        self.details['rooms'][things[0]].allowGames = False
                        return 'Chatgames are now not allowed in {room}'.format(room = things[0]), True
                    else:
                        return '{param} is not a supported parameter'.format(param = things[1]), True
                else:
                    return 'Cannot allow chatgames without being in the room', True
            else:
                return 'Too few/many parameters. Command is ~allowgames [room],True/False', False
        else:
            return 'You do not have permission to change this. (Requires #)', False

    # Informational commands
    elif cmd in Links:
        if msg in Links[cmd]:
            return Links[cmd][msg], True
        else:
            return '{tier} is not a supported format for {command}'.format(tier = msg, command = cmd), True
    # Fun stuff
    elif cmd == 'pick':
        options = msg.split(',')
        return options[randint(0,(len(options)-1))], True
    elif cmd == 'ask':
        return Lines[randint(0, len(Lines)-1)], True
    elif cmd == 'joke':
        if randint(0, 1) and self.Groups[user['group']] >= self.Groups['%']:
            return user['unform'], True
        else:
            return getJoke(), True
    elif cmd in tiers:
        pick = list(tiers[cmd])[randint(0,len(tiers[cmd])-1)]
        pNoForm = re.sub('-(?:Mega(?:-(X|Y))?|Primal)','', pick).lower()
        return '{poke} was chosen: http://www.smogon.com/dex/xy/pokemon/{mon}/'.format(poke = pick, mon = pNoForm), True
    elif cmd in [t.replace('poke','team') for t in tiers]:
        team = set()
        attempts = 0
        while len(team) < 6 or not acceptableWeakness(team):
            poke = list(tiers[cmd.replace('team','poke')])[randint(0,len(tiers[cmd.replace('team','poke')])-1)]
            # Test if share dex number with anything in the team
            if [p for p in team if Pokedex[poke]['dex'] == Pokedex[p]['dex']]:
                continue
            if [p for p in team if '-Mega' in p] and '-Mega' in poke:
                continue
            team |= {poke}
            if not acceptableWeakness(team):
                team -= {poke}
            if len(team) >= 6:
                break
            attempts += 1
            if attempts >= 100:
                # Prevents locking up if a pokemon turns the team to an impossible genration
                # Since the team is probably bad anyway, just finish it and exit
                while len(team) < 6:
                   team |= {list(tiers[cmd.replace('team','poke')])[randint(0,len(tiers[cmd.replace('team','poke')])-1)]} 
                break
        return ' / '.join(list(team)), True

    # Chat games go here
    # Hangman
    elif cmd == 'hangman':
        msg = msg.strip().split(',')
        if 'end' in msg[0] and canStartGame(self, user) and isGameType(self.details['gamerunning'], Hangman):
            phrase = self.details['gamerunning'].getSolution()
            self.details['gamerunning'] = None
            return 'The hangman game was forcefully ended by {baduser}. (Killjoy)\nThe solution was: **{solved}**'.format(baduser = user['unform'], solved = phrase), True
        elif 'new' in msg[0]: # ~hangman new,room,[phrase]
            if canStartGame(self, user):
                if self.details['gamerunning']:
                    return 'A game is already running somewhere', False
                else:              
                    phrase = re.sub(r'[^a-zA-Z0-9 ]', '', re.sub(r'\s{2,}', ' ', msg[2].lstrip()))
                    if not phrase.strip():
                        return 'You can only have letters, numbers or spaces in the phrase', False
                    self.details['gamerunning'] = Hangman(phrase)
                    return 'A new game of hangman has begun:\n' + self.details['gamerunning'].printCurGame(), True
            else:
                return 'You do not have permission to start a game in this room. (Requires %)', False
        else:
            return 'To start a new hangman game: ~hangman new,[room],[phrase]', True
    elif cmd == 'hg':
        if self.details['gamerunning']:
            if len(msg.replace(' ','')) == 1:
                return self.details['gamerunning'].guessLetter(msg.replace(' ','').lower()), True
            else:
                if not msg.lstrip():
                    return "You can't guess nothing", True
                if self.details['gamerunning'].guessPhrase(msg.lstrip()):
                    solved = self.details['gamerunning'].getFormatedPhrase()
                    self.details['gamerunning'] = None
                    return 'Congratulations {name}. You won!\nThe phrase was: {phrase}'.format(name = user['unform'], phrase = solved), True
                else:
                    return '{test} is wrong!'.format(test = msg.lstrip()), True
        else:
            return 'There is no hangman game in progress right now', True
    # Anagrams of Pokemon names
    elif cmd == 'anagram':
        if msg == 'new':
            if canStartGame(self, user):    
                if self.details['gamerunning']:
                    return 'A game is already running somewhere', False
                else:
                    self.details['gamerunning'] = Anagram()
                    return 'A new anagram has been created:\n' + self.details['gamerunning'].getWord(), True
            else:
                return 'You do not have permission to starta game in this room. (Requires %)', False
        elif msg == 'hint':
            if self.details['gamerunning']:
                return 'The hint is: ' + self.details['gamerunning'].getHint(), True
            else:
                return 'There is no active anagram right now', False
        elif msg == 'end':
            if canStartGame(self, user) and isGameType(self.details['gamerunning'], Anagram):
                solved = self.details['gamerunning'].getSolvedWord()
                self.details['gamerunning'] = None
                return 'The anagram was forcefully ended by {baduser}. (Killjoy)\nThe solution was: **{solved}**'.format(baduser = user['unform'], solved = solved), True
        # Everything else is guesses
        else:
            if self.details['gamerunning']:
                if self.details['gamerunning'].isCorrect(msg.lower()):
                    solved = self.details['gamerunning'].getSolvedWord()
                    self.details['gamerunning'] = None
                    return 'Congratulations {name}. You won!\nThe solution was: {solution}'.format(name = user['unform'], solution = solved), True
                else:
                    return '{test} is wrong!'.format(test = msg.lstrip()), True
            else:
                return 'There is no anagram active right now', True 
        

    # Commands with awful conditions last
    elif cmd in formats:
        return 'Format: http://www.smogon.com/dex/xy/formats/{tier}/'.format(tier = cmd), True
    # This command is here because it's an awful condition, so try it last :/
    elif [p for p in Pokedex if re.sub('-(?:mega(?:-(x|y))?|primal|xl|l)','', cmd, flags=re.I) in p.lower()]:
        cmd = re.sub('-(?:mega(?:-(x|y))?|primal)','', cmd)
        substitutes = {'gourgeist-s':'gourgeist-small',  # This doesn't break Arceus-Steel like adding |S to the regex would
                       'gourgeist-l':'gourgeist-large',  # and gourgeist-s /pumpkaboo-s still get found, because it matches the
                       'gourgeist-xl':'gourgeist-super', # entry for gougeist/pumpkaboo-super
                       'pumpkaboo-s':'pumpkaboo-small',
                       'pumpkaboo-l':'pumpkaboo-large',
                       'pumpkaboo-xl':'pumpkaboo-super',
                       'giratina-o':'giratina-origin'} 
        if cmd in substitutes:
            cmd = substitutes[cmd]
        if cmd.lower() not in (p.lower() for p in Pokedex):
            return '{cmd} is not a valid command'.format(cmd = cmd),True
        return 'Analysis: http://www.smogon.com/dex/xy/pokemon/{mon}/'.format(mon = cmd), True
    
    else:
        return False, False


def isMaster(self, user):
    return user['name'] == self.details['master']
def canSee(self, user):
    return user['name'] == self.details['master'] or self.Groups[user['group']] >= self.Groups['%']
def canChange(self, user):
    return user['name'] == self.details['master'] or self.Groups[user['group']] >= self.Groups['#']
def canAddUser(self, user):
    return user['name'] == self.details['master'] or self.Groups[user['group']] >= self.Groups['#']
def canStartGame(self, user):
    return user['name'] == self.details['master'] or self.Groups[user['group']] >= self.Groups['%']
def isGameType(running, gameType):
    return type(running) == gameType  
def acceptableWeakness(team):
    if not team: return False
    comp = {t:{'weak':0,'res':0} for t in Types}
    for poke in team:
        types = Pokedex[poke]['types']
        if len(types) > 1:
            for matchup in Types:
                eff = Types[types[0]][matchup] * Types[types[1]][matchup]
                if eff > 1:
                    comp[matchup]['weak'] += 1
                elif eff < 1:
                    comp[matchup]['res'] += 1
        else:
            for matchup in Types:
                if Types[types[0]][matchup] > 1:
                    comp[matchup]['weak'] += 1
                elif Types[types[0]][matchup] < 1:
                    comp[matchup]['res'] += 1
    for t in comp:
        if comp[t]['weak'] >= 3:
            return False
        if comp[t]['weak'] >= 2 and comp[t]['res'] <= 1:
            return False
    return True
def saveDetails(self):
    pass
def getURL():
    return 'https://github.com/QuiteQuiet/PokemonShowdownBot/'
def getJoke():
    people = ['Can-Eh-Dian', 'Disjunction', 'innovamania', 'iplaytennislol', 'marilli', 'Montsegur', 'Punchshroom', 'QueenOfLuvdiscs', 'Quite Quiet', 'scorpdestroyer', 'Teddeh', 'boltsandbombers', 'Deej Dy', 'Realistic Waters', 'Sir Kay', 'SolarisFox', 'Soulgazer', 'The Goomy', 'xzern']
    return people[randint(0, len(people)-1)]
