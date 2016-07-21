# The command file for every external command not specifically for running
# the bot. Even more relevant commands like broadcast options are treated as such.
##
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
import math # For funsies

from data.tiers import tiers, formats
from data.links import Links, YoutubeLinks
from data.pokedex import Pokedex
from data.types import Types
from data.replies import Lines

from robot import ReplyObject
from user import User
from room import RoomCommands
from plugins import PluginCommands

ExternalCommands = RoomCommands.copy()
ExternalCommands.update(PluginCommands)

usageLink = r'http://www.smogon.com/stats/2016-06/'

def URL(): return 'https://github.com/QuiteQuiet/PokemonShowdownBot/'

def Command(self, cmd, room, msg, user):
    ''' Returns the reply if the command exists, and False if it doesn't '''

    if cmd in ['source', 'git']:
        return ReplyObject('Source code can be found at: {url}'.format(url = URL()))
    if cmd == 'credits':
        return ReplyObject('Credits can be found: {url}'.format(url = URL()), True)
    if cmd == 'owner':
        return ReplyObject('Owned by: {owner}'.format(owner = self.owner), True)
    if cmd in ['commands', 'help']:
        return ReplyObject('Read about commands here: {url}blob/master/COMMANDS.md'.format(url = URL()), True, False, False, False, True)
    if cmd == 'explain':
        return ReplyObject("BB-8 is the name of a robot in the seventh Star Wars movie :)", True)
    if cmd == 'leave':
        msg = self.removeSpaces(msg)
        if not msg: msg = room.title
        if self.leaveRoom(msg):
            return ReplyObject('Leaving room {r} succeeded'.format(r = msg))
        return ReplyObject('Could not leave room: {r}'.format(r = msg))
    if cmd == 'get':
        if user.isOwner():
            return ReplyObject(str(eval(msg)), True)
        return ReplyObject('You do not have permisson to use this command. (Only for owner)')
    # Save current self.details to details.yaml (moves rooms to joinRooms)
    # Please note that this command will remove every comment from details.yaml, if those exist.
    if cmd == 'savedetails':
        if user.hasRank('#'):
            self.saveDetails()
            return ReplyObject('Details saved.', True)
        return ReplyObject("You don't have permission to save settings. (Requires #)")

    # Permissions
    if cmd == 'broadcast':
        return ReplyObject('Rank required to broadcast: {rank}'.format(rank = self.details['broadcastrank']), True)
    if cmd == 'setbroadcast':
        msg = self.removeSpaces(msg)
        if msg in User.Groups or msg in ['off', 'no', 'false']:
            if user.hasRank('#'):
                if msg in ['off', 'no', 'false']: msg = ' '
                if self.details['broadcastrank'] == msg:
                    return ReplyObject('Broadcast rank is already {rank}'.format(rank = msg), True)
                self.details['broadcastrank'] = msg
                return ReplyObject('Broadcast rank set to {rank}. (This is not saved on reboot)'.format(rank = msg), True)
            return ReplyObject('You are not allowed to set broadcast rank. (Requires #)')
        return ReplyObject('{rank} is not a valid rank'.format(rank = msg))

    # External commands from plugins (and also room.py)
    if cmd in ExternalCommands.keys():
        return ExternalCommands[cmd](self, cmd, room, msg, user)

    # Informational commands
    if cmd in Links:
        msg = msg.lower()
        if msg in Links[cmd]:
            return ReplyObject(Links[cmd][msg], True)
        return ReplyObject('{tier} is not a supported format for {command}'.format(tier = msg, command = cmd), True)
    if cmd == 'usage':
        return ReplyObject(usageLink, True, False, False, False, True)
    # Fun stuff
    if cmd == 'pick':
        options = msg.split(',')
        return ReplyObject(options[randint(0,(len(options)-1))], True)
    if cmd == 'ask':
        return ReplyObject(Lines[randint(0, len(Lines)-1)], True)

    if cmd == 'squid':
        return ReplyObject('\u304f\u30b3\u003a\u5f61', True)
    if cmd in YoutubeLinks:
        return ReplyObject(YoutubeLinks[cmd], True)
    if cmd in tiers:
        pick = list(tiers[cmd])[randint(0,len(tiers[cmd])-1)]
        pNoForm = re.sub('-(?:Mega(?:-(X|Y))?|Primal)','', pick).lower()
        return ReplyObject('{poke} was chosen: http://www.smogon.com/dex/xy/pokemon/{mon}/'.format(poke = pick, mon = pNoForm), True)
    if cmd in [t.replace('poke','team') for t in tiers]:
        team = set()
        hasMega = False
        attempts = 0
        while len(team) < 6 or not acceptableWeakness(team):
            poke = list(tiers[cmd.replace('team','poke')])[randint(0,len(tiers[cmd.replace('team','poke')])-1)]
            # Test if share dex number with anything in the team
            if [p for p in team if Pokedex[poke]['dex'] == Pokedex[p]['dex']]:
                continue
            if hasMega:
                continue
            team |= {poke}
            if not acceptableWeakness(team):
                team -= {poke}
            elif '-Mega' in poke:
                hasMega = True
            if len(team) >= 6:
                break
            attempts += 1
            if attempts >= 100:
                # Prevents locking up if a pokemon turns the team to an impossible genration
                # Since the team is probably bad anyway, just finish it and exit
                while len(team) < 6:
                   team |= {list(tiers[cmd.replace('team','poke')])[randint(0,len(tiers[cmd.replace('team','poke')])-1)]}
                break
        return ReplyObject(' / '.join(list(team)), True)
    if cmd in formats:
        return ReplyObject('Format: http://www.smogon.com/dex/xy/formats/{tier}/'.format(tier = cmd), True)
    # This command is here because it's an awful condition, so try it last :/
    if [p for p in Pokedex if re.sub('-(?:mega(?:-(x|y))?|primal|xl|l)','', cmd, flags=re.I) in p.replace(' ','').lower()]:
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
        if cmd.lower() not in (self.removeSpaces(p).lower() for p in Pokedex):
            return ReplyObject('{cmd} is not a valid command'.format(cmd = cmd), True)
        if cmd in substitutes:
            cmd = substitutes[cmd]
        return ReplyObject('/addhtmlbox <a href="http://www.smogon.com/dex/xy/pokemon/{mon}/">{capital} analysis</a>'.format(mon = cmd, capital = cmd.title()), True, True)


    return ReplyObject('{command} is not a valid command.'.format(command = cmd))

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
