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
#
# Information passed from the chat-parser:
#   self: The program object itself.
#
#   cmd: Contains what command was used.
#
#   msg: This hold everything else that was passed with the command, such as
#        optional parameters.
#
#   room: What room the command was used in. If the command was sent in a pm,
#         room will contain: 'Pm'. See room.py for more details.
#
#   user: A user object like the one described in the app.py file

from random import randint, sample
import re
import yaml
import json
import math # For funsies

from data.tiers import tiers, formats
from data.teams import Teams
from data.links import Links, YoutubeLinks
from data.pokedex import Pokedex
from data.types import Types
from data.replies import Lines

from plugins.games import Anagram
from plugins.workshop import Workshop
from plugins.trivia.trivia import Trivia
from plugins.moderation import addBan, removeBan

usageLink = r'http://www.smogon.com/stats/2016-03/'
GameCommands = ['hangman', 'hg', 'anagram', 'a', 'trivia', 'ta']
IgnoreBroadcastPermission = ['anagram', 'a', 'trivia', 'ta', 'tour']
CanPmReplyCommands = ['usage', 'help']
IgnoreEscaping = ['tour', 'oldgentour']
Scoreboard = {}
with open('plugins/scoreboard.yaml', 'a+') as yf:
    yf.seek(0, 0)
    Scoreboard = yaml.load(yf)
    if not Scoreboard: # Empty yaml file set Scoreboard to None, but an empty dict is better
        Scoreboard = {}

def Command(self, cmd, room, msg, user):
    ''' Returns the reply if the command exists, and False if it doesn't '''
    # Debug commands and program info
    if cmd == 'echo':
        if not isMaster(self, user): return 'You do not have permisson to use this command. (Only for owner)', False
        return msg, True
    elif cmd in ['source', 'git']:
        return 'Source code can be found at: {url}'.format(url = URL()), False
    elif cmd == 'credits':
        return 'Credits can be found: {url}'.format(url = URL()), True
    elif cmd == 'owner':
        return 'Owned by: {owner}'.format(owner = self.details['master']), True
    elif cmd in ['commands', 'help']:
        return 'Read about commands here: {url}blob/master/COMMANDS.md'.format(url = URL()), True
    elif cmd == 'explain':
        return "BB-8 is the name of a robot in the seventh Star Wars movie :)", True
    elif cmd == 'leave':
        msg = removeSpaces(msg)
        if not msg: msg = room.title
        if self.leaveRoom(msg):
            return 'Leaving room {r} succeeded'.format(r = msg), False
        return 'Could not leave room: {r}'.format(r = msg), False
    # THIS COMMAND SHOULDN'T BE DOCUMENTED!
    elif cmd == 'get':
        if isMaster(self, user):
            return str(eval(msg)), True
        return 'You do not have permisson to use this command. (Only for owner)', False
    # Save current self.details to details.yaml (moves rooms to joinRooms)
    # Please note that this command will remove every comment from details.yaml, if those exist.
    elif cmd == 'savedetails':
        if canChange(self, user):
            saveDetails(self)
            return 'Details saved.', True
        return "You don't have permission to save settings. (Requires #)", False

    # Permissions
    elif cmd == 'broadcast':
        return 'Rank required to broadcast: {rank}'.format(rank = self.details['broadcastrank']), True
    elif cmd == 'setbroadcast':
        msg = removeSpaces(msg)
        if msg in self.Groups or msg in ['off', 'no', 'false']:
            if canChange(self, user):
                if msg in ['off', 'no', 'false']: msg = ' '
                if self.details['broadcastrank'] == msg:
                    return 'Broadcast rank is already {rank}'.format(rank = msg), True
                self.details['broadcastrank'] = msg
                return 'Broadcast rank set to {rank}. (This is not saved on reboot)'.format(rank = msg), True
            return 'You are not allowed to set broadcast rank. (Requires #)', False
        return '{rank} is not a valid rank'.format(rank = msg), False
    elif cmd == 'whitelist':
        if canSee(self, user):
            if self.details['whitelist']:
                return ', '.join(self.details['whitelist']), False
            return 'Whitelist is empty :(', False
        return 'You are not allowed to see the whitelist :l (Requires %)', False
    elif cmd in ['whitelistuser', 'wluser']:
        if canAddUser(self, user):
            msg = re.sub(r'[^a-zA-z0-9]', '', msg)
            if msg in self.details['whitelist']:
                return '{user} is already whitelisted'.format(user = msg), True
            self.details['whitelist'].append(msg)
            return 'User {usr} added to whitelist.'.format(usr = msg), True
    elif cmd == 'removewl':
        if canAddUser(self, user):
            msg = re.sub(r'[^a-zA-z0-9]', '', msg)
            if msg not in self.details['whitelist']:
                return '{user} is not whitelisted'.format(user = msg), True
            self.details['whitelist'].remove(msg)
            return 'User {usr} removed from the whitelist.'.format(usr = msg), True
    elif cmd == 'moderate':
        if not msg:
            return 'No parameters given. Command is ~moderate [room],True/False', False
        else:
            if canChange(self, user):
                things = removeSpaces(msg).split(',')
                if not len(things) == 2:
                    return 'Too few/many parameters given. Command is ~moderate [room],True/False', False
                if things[0] in self.details['rooms']:
                    if things[1] in ['True', 'true']:
                        self.getRoom(things[0]).moderate = True
                        return '{room} will now be moderated'.format(room = things[0]), False
                    elif things[1] in ['False', 'false']:
                        self.getRoom(things[0]).moderate = False
                        return '{room} will not be moderated anymore'.format(room = things[0]), False
                return 'You cannot set moderation in a room without me in it.', False
            return 'You do not have permission to set this. (Requires #)', False
    # Autobans
    elif cmd in ['banuser', 'banphrase']:
        if canAddUser(self, user):
            error = addBan(cmd[3:], room.title, msg)
            if not error:
                return 'Added {thing} to the banlist for room {room}'.format(thing = msg, room = room.title), True
            return error, True
        return 'You do not have permission to do this. (Requires #)', False
    elif cmd in ['unbanuser', 'unbanphrase']:
        if canAddUser(self, user):
            error = removeBan(cmd[5:], room.title, msg)
            if not error:
                return 'Removed {thing} from the banlist for room {room}'.format(thing = msg, room = room.title), True
            return error, True
        return 'You do not have permission to do this. (Requires #)', False

    elif cmd == 'allowgames':
        if canChange(self, user):
            msg = removeSpaces(msg)
            things = msg.split(',')
            if len(things) == 2:
                if things[0] in self.details['rooms']:
                    if things[1] in ['true','yes','y','True']:
                        if not self.getRoom(things[0]).allowGames:
                            self.getRoom(things[0]).allowGames = True
                            return 'Chatgames are now allowed in {room}'.format(room = things[0]), True
                        return 'Chatgames are already allowed in {room}'.format(room = things[0]), True
                    elif things[1] in ['false', 'no', 'n',' False']:
                        self.getRoom(things[0]).allowGames = False
                        return 'Chatgames are now not allowed in {room}'.format(room = things[0]), True
                    return '{param} is not a supported parameter'.format(param = things[1]), True
                return 'Cannot allow chatgames without being in the room', True
            return 'Too few/many parameters. Command is ~allowgames [room],True/False', False
        return 'You do not have permission to change this. (Requires #)', False

    # Pipe tour commands for whitelisted people
    elif cmd == 'tour' or cmd == 'tournament':
        if room.title == 'pm': return "You can't use this command in a pm.", False
        if not isTourWhitelisted(self, room, user): return 'You are not allowed to use this command. (Requires whitelisting by a Room Owner)', True
        if not self.Groups[room.rank] >= self.Groups['@']: return "I don't have the rank required to start a tour :(", True
        return '/tour {rest}'.format(rest = msg), True
    # Tournament whitelisting
    elif cmd == 'tourwl':
        if canAddUser(self, user):
            target = re.sub(r'[^a-zA-z0-9]', '', msg).lower()
            if room.addToWhitelist(target):
                saveDetails(self)
                return '{name} added to the whitelist in this room.'.format(name = msg), True
            return 'This user is already whitelisted in that room.', False
        return 'You do not have permission to change this. (Requires #)', False
    elif cmd =='untourwl':
        if canAddUser(self, user):
            target = re.sub(r'[^a-zA-z0-9]', '', msg).lower()
            if room.delFromWhitelist(target):
                saveDetails(self)
                return '{name} removed from the whitelist in this room.'.format(name = msg), True
            return 'This user is not whitelisted in that room.', False
        return 'You do not have permission to change this. (Requires #)', False

    # Informational commands
    elif cmd in Links:
        msg = msg.lower()
        if msg in Links[cmd]:
            return Links[cmd][msg], True
        return '{tier} is not a supported format for {command}'.format(tier = msg, command = cmd), True
    elif cmd == 'team':
        if msg not in Teams:
            return 'Unsupported format', True
        return Teams[msg][randint(0, len(Teams[msg])-1)], True
    elif cmd == 'usage':
        return usageLink, True

    elif cmd == 'oldgentour':
        if not room.tour: return 'No tour is currently active, so this command is disabled.', True
        if not room.tour.format.startswith('gen'): return "The current tour isn't a previous generation, so this command is disabled.", True
        pastGens = {'gen1': 'RBY', 'gen2':'GSC', 'gen3':'RSE',  'gen4':'DPP'}
        warning = ''
        if room.tour.format[0:4] in pastGens: warning = "/wall Please note that bringing Pokemon that aren't **{gen} NU** will disqualify you\n".format(gen = pastGens[room.tour.format[0:4]])
        return warning + "/wall Sample teams here: http://www.smogon.com/forums/threads/3562659/", True

    # Offline messages
    elif cmd == 'tell':
        if not msg: return 'You need to specify a user and a message to send in the format: [user], [message]', False
        msg = msg.split(',')
        to = re.sub(r'[^a-zA-z0-9]', '', msg[0]).lower()
        if self.usernotes.alreadySentMessage(to, user['unform']):
            return 'You already have a message to this user waiting', False
        if len(msg) < 2: return 'You forgot a message', True
        if len(msg[1].lstrip()) > 150:
            return 'Message is too long. Max limit is 150 characters', False
        self.usernotes.addMessage(to, user['unform'], msg[1].lstrip())
        return "I'll be sure to tell them that.", True
    # Getting the messages back
    elif cmd == 'read':
        if not self.usernotes.hasMessage(user['name']): return 'You have no messages waiting', False
        if not msg:
            # If the user didn't speify any amount to return, give back a single message
            return self.usernotes.getMessages(user['name'], 1), False
        if not msg.isdigit() and int(msg) < 1: return 'Please enter a whole, positive number', False
        return self.usernotes.getMessages(user['name'], int(msg)), False
    elif cmd == 'removetell':
        if not msg: return 'You need to specify a user to remove', False
        if not self.usernotes.hasMessage(msg): return 'This user has no waiting messages', False
        if not self.usernotes.removeMessage(msg, user['name']): return 'You have no message to this user waiting', False
        return 'Message removed', True

    # Fun stuff
    elif cmd == 'pick':
        options = msg.split(',')
        return options[randint(0,(len(options)-1))], True
    elif cmd == 'ask':
        return Lines[randint(0, len(Lines)-1)], True
    elif cmd in YoutubeLinks:
        return YoutubeLinks[cmd], True
    elif cmd == 'squid':
        return '\u304f\u30b3\u003a\u5f61', True
#    elif cmd == 'joke':
#        if randint(0, 1) and self.Groups[user['group']] >= self.Groups['+']:
#            return user['unform'], True
#        return getJoke(), True
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

    # Workshop is not a hangman game, but uses the allowed slot for a game anyway
    # Workshops also doesn't follow the chatgames rule, as they're not chat games
    elif cmd == 'workshop':
        if not isGameType(room.game, Workshop):
            if msg.startswith('new') and canStartGame(self, user):
                room.game = Workshop(re.sub(r'[^a-zA-z0-9]', '', msg[len('new '):] if msg[len('new '):] else user['name']).lower())
                return 'A new workshop session was created', True
            return 'No active workshop right now', True
        workshop = room.game
        if msg.startswith('add'):
            if not user['name'] == workshop.host and not canStartGame(self, user):
                return 'Only the workshop host or a Room Moderator can add Pokemon', True
            return workshop.addPokemon(msg[len('add '):]), True
        elif msg.startswith('remove'):
            if not user['name'] == workshop.host and not canStartGame(self, user):
                return 'Only the workshop host or a Room Moderator can remove Pokemon', True
            return workshop.removePokemon(msg[len('remove '):]), True
        elif msg == 'clear':
            if not user['name'] == workshop.host and not canStartGame(self, user):
                return 'Only the workshop host or a Room Moderator can clear the team', True
            return workshop.clearTeam(), True
        elif msg == 'team':
            return workshop.getTeam(), True
        elif msg == 'end':
            if not user['name'] == workshop.host and not canStartGame(self, user):
                return 'Only the workshop host or a Room Moderator can end the workshop', True
            self.sendPm(workshop.host, workshop.pasteLog(room.title, self.details['apikey']))
            room.game = None
            return 'Workshop session ended', True

    # Chat games go here
    # Anagrams of Pokemon names
    elif cmd == 'anagram':
        if msg == 'new':
            if canStartGame(self, user):
                if room.game:
                    return 'A game is already running somewhere', False
                room.game = Anagram()
                return 'A new anagram has been created (guess with ~a):\n' + room.game.getWord(), True
            return 'You do not have permission to start a game in this room. (Requires %)', False
        elif msg == 'hint':
            if room.game:
                return 'The hint is: ' + room.game.getHint(), True
            return 'There is no active anagram right now', False
        elif msg == 'end':
            if canStartGame(self, user):
                if isGameType(room.game, Anagram):
                    solved = room.game.getSolvedWord()
                    room.game = None
                    return 'The anagram was forcefully ended by {baduser}. (Killjoy)\nThe solution was: **{solved}**'.format(baduser = user['unform'], solved = solved), True
                return 'There is no active anagram or a different game is active.', False
            return 'You do not have permission to end the anagram. (Requires %)', True
        elif msg.lower().startswith('score'):
            if msg.strip() == 'score':
                msg += ' {user}'.format(user = user['name'])
            name = re.sub(r'[^a-zA-z0-9]', '', msg[len('score '):]).lower()
            if name not in Scoreboard:
                return "This user never won any anagrams", True
            return 'This user has won {number} anagram{plural}'.format(number = Scoreboard[name], plural = '' if not type(Scoreboard[name]) == str and Scoreboard[name] < 2  else 's'), True

        else:
            if not msg:
                if isGameType(room.game, Anagram):
                    return 'Current anagram: {word}'.format(word = room.game.getWord()), True
                return 'There is no active anagram right now', False
            return '{param} is not a valid parameter for ~anagram. Make guesses with ~a'.format(param = msg), False
    elif cmd == 'a':
        if isGameType(room.game, Anagram):
            if room.game.isCorrect(re.sub(r'[ -]', '', msg).lower()):
                solved = room.game.getSolvedWord()
                timeTaken = room.game.getSolveTimeStr()
                room.game = None
                # Save score
                Scoreboard[user['name']] = 1 if user['name'] not in Scoreboard else Scoreboard[user['name']] + 1
                with open('plugins/scoreboard.yaml', 'w') as ym:
                    yaml.dump(Scoreboard, ym)
                return 'Congratulations, {name} got it{time}\nThe solution was: {solution}'.format(name = user['unform'], time = timeTaken, solution = solved), True
            return '{test} is wrong!'.format(test = msg.lstrip()), True
        return 'There is no anagram active right now', True
    # Trivia
    elif cmd == 'trivia':
        if msg:
            params = removeSpaces(msg).split(',')
            if params[0] in ['start', 'begin']:
                kind = 'first'
                if len(params) > 1:
                    kind = params[1]
                if canStartTrivia(self, user):
                    room.game = Trivia(self.ws, room.title, kind)
                    return 'A new trivia session has started.', True
                return 'You do not have permission to set up a trivia session', False
            elif params[0] in ['stop', 'end']:
                # The trivia class will solve everything after doing this.
                room.game.endSession = True
                room.game = None
                return 'The trivia session has been ended', True
        return '{msg} is not an valid parameter for trivia', False
    elif cmd == 'ta':
        if isGameType(room.game, Trivia):
            # Don't give information if wrong or right here, let Trivia deal with that
            if room.game.tryAnswer(msg):
                if not room.game.solver:
                    room.game.wasSolved(user['unform'])
                else:
                    room.game.multiple = True
            return 'NoAnswer', False
        return 'There is no ongoing trivia session.', True

    # Commands with awful conditions last
    elif cmd in formats:
        return 'Format: http://www.smogon.com/dex/xy/formats/{tier}/'.format(tier = cmd), True
    # This command is here because it's an awful condition, so try it last :/
    elif [p for p in Pokedex if re.sub('-(?:mega(?:-(x|y))?|primal|xl|l)','', cmd, flags=re.I) in p.replace(' ','').lower()]:
        cmd = re.sub('-(?:mega(?:-(x|y))?|primal)','', cmd)
        substitutes = {'gourgeist-s':'gourgeist-small',  # This doesn't break Arceus-Steel like adding |S to the regex would
                       'gourgeist-l':'gourgeist-large',  # and gourgeist-s /pumpkaboo-s still get found, because it matches the
                       'gourgeist-xl':'gourgeist-super', # entry for gougeist/pumpkaboo-super
                       'pumpkaboo-s':'pumpkaboo-small',
                       'pumpkaboo-l':'pumpkaboo-large',
                       'pumpkaboo-xl':'pumpkaboo-super',
                       'giratina-o':'giratina-origin',
                       'mr.mime':'mr_mime',
                       'mimejr.':'mime_jr'}
        if cmd.lower() not in (removeSpaces(p).lower() for p in Pokedex):
            return '{cmd} is not a valid command'.format(cmd = cmd),True
        if cmd in substitutes:
            cmd = substitutes[cmd]
        return 'Analysis: http://www.smogon.com/dex/xy/pokemon/{mon}/'.format(mon = cmd), True

    else:
        return '{command} is not a valid command.'.format(command = cmd), False

def URL(): return 'https://github.com/QuiteQuiet/PokemonShowdownBot/'
def removeSpaces(text):
    return text.replace(' ','')
# Permission settings for different things
# These can't be changed during operation, compared to the general permission
def isMaster(self, user):
    return user['name'] == self.details['master']
def isWhitelisted(self, user):
    return isMaster(self, user) or user['name'] in self.details['whitelist']
def isTourWhitelisted(self, room, user):
    return canStartTrivia(self, user) or room.isWhitelisted(user['name'])
def canSee(self, user):
    return isMaster(self, user) or self.Groups[user['group']] >= self.Groups['%']
def canChange(self, user):
    return isMaster(self, user) or self.Groups[user['group']] >= self.Groups['#']
def canAddUser(self, user):
    return isMaster(self, user) or self.Groups[user['group']] >= self.Groups['#']
def canStartGame(self, user):
    return isMaster(self, user) or self.Groups[user['group']] >= self.Groups['%']
def canStartTrivia(self, user):
    return isMaster(self, user) or self.Groups[user['group']] >= self.Groups['@']
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
    details = {k:v for k,v in self.details.items() if not k == 'rooms' and not k == 'joinRooms'}
    details['joinRooms'] = []
    for e in self.details['rooms']:
        details['joinRooms'].append({e:{'moderate':self.getRoom(e).moderate,
                                        'allow games':self.getRoom(e).allowGames,
                                        'tourwhitelist':self.getRoom(e).tourwhitelist}
                                    })
    details['rooms'] = {}
    with open('details.yaml', 'w') as yf:
        yaml.dump(details, yf, default_flow_style = False)

def getJoke():
    people = ['Disjunction','Aladyyn','boltsandbombers','Can-Eh-Dian','Deej Dy','innovamania','Kiyo','Marilli','Montsegur','Pokedots','Punchshroom','Queen of Luvdiscs','rw','Scorpdestroyer','silver Aurum','Sir Kay','tennis','Blast Chance','HJAD','shaneghoul','Soulgazer','Allstar124','Blaziken1337','Dentricos','Finchinator','flcl','GyRro','hootie','Jarii','Less Than Three Man','Marikeinen','Metaphysical','Not Nova','Nozzle','orphic','Raptures Finest','rozes','Sweet Jesus','Syncrasy','Vileman',"Winter's Howl"]
    return people[randint(0, len(people)-1)]