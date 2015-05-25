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
#       can be returned to the same room rather than a PM.
# False: This will ALWAYS return the reply as a PM, no matter where it came from

from random import randint, sample
import re
import yaml
import json

from data.tiers import tiers, formats
from data.pokedex import Pokedex
from data.types import Types
from data.games import Hangman

GameCommands = ['hangman', 'hg']

def Command(self, cmd, msg, user):
    ''' Returns the reply if the command exists, and False if it doesn't '''
    # Debug commands and program info
    if cmd == 'echo':
        return msg, True
    elif cmd == 'source':
        return 'Source code can be found at: {url}'.format(url = getURL()), False
    elif cmd in ['commands', 'help']:
        return 'Read about commands here: {url}blob/master/COMMANDS.md'.format(url = getURL()), False
    elif cmd == 'leave':
        msg = msg.replace(' ','')
        if self.leaveRoom(msg):
            return 'Leaving room {r} succeeded'.format(r = msg), False
        else:
            return 'Could not leave room: {r}'.format(r = msg), False
    # Permissions
    elif cmd == 'broadcast':
        return 'Rank required to broadcast: {rank}'.format(rank = self.details['broadcastrank']), True
    elif cmd == 'setbroadcast':
        msg = msg.replace(' ','')
        if msg in self.Groups:
            if canChange(self, user):
                if self.details['broadcastrank'] == msg:
                    return 'Broadcast rank is already {rank}'.format(rank = msg), True
                else:
                    self.details['broadcastrank'] = msg
                    return 'Broadcast rank set to {rank}. (This is not saved on reboot)'.format(rank = msg), True
            else:
                return 'You are not allowed to set broadcast rank.', False
        else:
            return '{rank} is not a valid rank'.format(rank = msg), False
    elif cmd == 'whitelist':
        if canSee(self, user):
            if self.details['whitelist']:
                return ' ,'.join(self.details['whitelist']), False
            else:
                return 'Whitelist is empty :(', False
        else:
            return 'You are not allowed to see the whitelist :l', False
    elif cmd in ['whitelistuser', 'wluser']:
        if canAddUser(self, user):
            self.details['whitelist'].append(user['name'])
    elif cmd == 'removewl':
        if canAddUser(self, user):
            self.details['whitelist'].remove(user['name'])

    elif cmd == 'allowgames':
        msg = msg.replace(' ','')
        things = msg.split(',')
        if len(things) == 2:
            if things[0] in self.details['rooms']:
                self.details['rooms'][things[0]].allowGames = True if things[1] in ['true','yes','y','True'] else False
                return 'Chatgames are now {state} in {room}'.format(state = 'allowed' if self.details['rooms'][things[0]].allowGames else 'not allowed', room = things[0]), True
        else:
            return 'Too few/many parameters. Command is ~allowgames [room],True/False', False

    # Fun stuff
    elif cmd == 'pick':
        options = msg.split(',')
        return options[randint(0,(len(options)-1))], True
    elif cmd == 'joke':
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

    # Hangman
    elif cmd == 'hangman':
        msg = msg.lstrip().split(',')
        if 'end' in msg[0] and canStartGame(self, user):
            phrase = self.details['gamerunning'].getSolution()
            self.details['gamerunning'] = None
            return 'The hangman game was forcefully ended by {baduser}. (Killjoy)\nThe solution was: **{solved}**'.format(baduser = user['unform'], solved = phrase), True
        elif 'new' in msg[0]: # ~hangman new,room,[phrase]
            if self.details['gamerunning']:
                return 'A hangman game is already running somewhere', False
            else:
                self.details['gamerunning'] = Hangman(msg[2].lstrip())
                return 'A new game of hangman has begun:\n' + self.details['gamerunning'].printCurGame(), True
        else:
        	   return 'To start a new hangman game: ~hangman new,[room],[phrase]', True
    elif cmd == 'hg':
        if self.details['gamerunning']:
            if len(msg.replace(' ','')) == 1:
                return self.details['gamerunning'].guessLetter(msg.replace(' ','').lower()), True
            else:
                if self.details['gamerunning'].guessPhrase(msg.lstrip()):
                    solved = self.details['gamerunning'].getFormatedPhrase()
                    self.details['gamerunning'] = None
                    return 'Congratulations {name}. You won!\nThe phrase was: {phrase}'.format(name = user['unform'], phrase = solved), True
                else:
                    return '{test} is wrong!'.format(test = msg.lstrip()), True
        else:
            return 'There is no game in progress right now', True

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
        return 'Analysis: http://www.smogon.com/dex/xy/pokemon/{mon}/'.format(mon = cmd), True
    
    else:
        return False, False



def canSee(self, user):
    return user['name'] == self.details['master'] or self.Groups[user['group']] >= self.Groups['%']
def canChange(self, user):
    return user['name'] == self.details['master'] or self.Groups[user['group']] >= self.Groups['#']
def canAddUser(self, user):
    return user['name'] == self.details['master'] or self.Groups[user['group']] >= self.Groups['~']
def canStartGame(self, user):
    return user['name'] == self.details['master'] or self.Groups[user['group']] >= self.Groups['@']
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
def getURL():
    return 'https://github.com/QuiteQuiet/PokemonShowdownBot/'
def getJoke():
    people = ['canehdian', 'disjunction', 'innovamania', 'iplaytennislol', 'marilli', 'montsegur', 'punchshroom', 'queenofluvdiscs', 'quitequiet', 'scorpdestroyer', 'teddeh', 'boltsandbombers', 'deejdy', 'realisticwaters', 'sirkay', 'solarisfox', 'soulgazer', 'thegoomy', 'xzern']
    return people[randint(0, len(people)-1)]
