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
#   params: This hold everything else that was passed with the command, such as
#        optional parameters.
#
#   room: What room the command was used in. If the command was sent in a pm,
#         room will contain: 'Pm'. See room.py for more details.
#
#   user: A user object like the one described in the app.py file

from random import randint, choice
import re
import math # For funsies
import datetime

from invoker import ReplyObject, Command

from data.tiers import tiers, formats
from data.links import Links, YoutubeLinks
from data.pokedex import Pokedex
from data.types import Types
from data.replies import Lines

from user import User

usageLink = r'http://www.smogon.com/stats/2019-01/'

def URL(): return 'https://github.com/QuiteQuiet/PokemonShowdownBot/'

def get(robot, cmd, params, user):
    if user.isOwner():
        res = str(eval(params))
        return ReplyObject(res if not res == None else '', True)
    return ReplyObject('You do not have permisson to use this command. (Only for owner)')

def forcerestart(robot, cmd, params, user):
    if user.hasRank('#'):
        # Figure out how to do this
        robot.closeConnection()
        return ReplyObject('')
    return ReplyObject('You do not have permisson to use this command. (Only for owner)')

def savedetails(robot, cmd, params, user):
    """ Save current robot.details to details.yaml (moves rooms to joinRooms)
     Please note that this command will remove every comment from details.yaml, if those exist."""
    if user.hasRank('#'):
        robot.saveDetails()
        return ReplyObject('Details saved.', True)
    return ReplyObject("You don't have permission to save settings. (Requires #)")

def newautojoin(robot, cmd, params, user):
    if user.hasRank('#'):
        # Join the room before adding it to list of autojoined rooms
        robot.joinRoom(params)
        robot.saveDetails(True)
        return ReplyObject("New autojoin ({room}) added.".format(room = params))
    return ReplyObject("You don't have permission to save settings. (Requires #)")

def setbroadcast(robot, cmd, params, user):
    params = robot.removeSpaces(params)
    if params in User.Groups or params in ['off', 'no', 'false']:
        if user.hasRank('#'):
            if params in ['off', 'no', 'false']: params = ' '
            if robot.details['broadcastrank'] == params:
                return ReplyObject('Broadcast rank is already {rank}'.format(rank = params if not params == ' ' else 'none'), True)
            robot.details['broadcastrank'] = params
            return ReplyObject('Broadcast rank set to {rank}. (This is not saved on reboot)'.format(rank = params if not params == ' ' else 'none'), True)
        return ReplyObject('You are not allowed to set broadcast rank. (Requires #)')
    return ReplyObject('{rank} is not a valid rank'.format(rank = params if not params == ' ' else 'none'))

def uptime(robot):
    mods = [86400, 3600, 60]
    seconds = (datetime.datetime.now() - robot.startTime).total_seconds()
    uptime = []
    for mod in mods:
        unit, seconds = divmod(seconds, mod)
        uptime.append(int(unit))

    uptime[0] = '{} day{}, '.format(uptime[0], 's' if uptime[0] > 1 else '') if uptime[0] > 0 else ''
    uptime[1] = '{} hour{} and '.format(uptime[1], 's' if uptime[1] > 1 else '') if uptime[1] > 0 else ''
    uptime[2] = '{} minute{}.'.format(uptime[2], 's' if uptime[2] != 1 else '')
    return ReplyObject('Current uptime is: {uptime}'.format(uptime = ''.join(uptime)), True, broadcast = True)

def links(robot, cmd, params):
    params = params.lower()
    if not params: params = 'nu'
    if params in Links[cmd]:
        return ReplyObject(Links[cmd][params], True)
    return ReplyObject('{tier} is not a supported format for {command}'.format(tier = params if params else "''", command = cmd), True)

def declare(robot, cmd, params, user):
    if not user.hasRank('%'):
        return ReplyObject('Only Drivers and up can use this', True)
    try:
        declareType, username = params.split(',')
    except ValueError:
        return ReplyObject('Missing parameter. Usage: {}declare [type], [user] ({})'.format(robot.commandchar, params))

    declareType = declareType.strip().lower()
    if declareType == 'teambattle':
        string = 'A Team Battle is starting soon. PM {} to enter.'.format(username.strip())
    else:
        return ReplyObject('Invalid type of declare')
    return ReplyObject('/declare {}'.format(string), True, True)

def randpoke(robot, cmd):
    pick = list(tiers[cmd])[randint(0,len(tiers[cmd])-1)]
    pNoForm = re.sub('-(?:Mega(?:-(X|Y))?|Primal)','', pick).lower()
    return ReplyObject('{poke} was chosen: http://www.smogon.com/dex/sm/pokemon/{mon}/'.format(poke = pick, mon = pNoForm), True)

def randteam(robot, cmd):
    # Helper function that calculates if the team sucks against any specific type
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

    cmd = cmd.replace('team','poke')
    team = set()
    hasMega = False
    attempts = 0
    while len(team) < 6 or not acceptableWeakness(team):
        poke = choice(list(tiers[cmd]))
        # Test if share dex number with anything in the team
        if [p for p in team if Pokedex[poke]['num'] == Pokedex[p]['num']]:
            continue
        if hasMega and '-Mega' in poke:
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
               team |= {choice(list(tiers[cmd]))}
            break
    return ReplyObject(' / '.join(list(team)), True)

def pokedex(robot, cmd, params, user, room):
    cmd = re.sub('-(?:mega(?:-(x|y))?|primal)','', cmd)
    substitutes = {'gourgeist-s':'gourgeist-small',  # This doesn't break Arceus-Steel like adding |S to the regex would
                   'gourgeist-l':'gourgeist-large',  # and gourgeist-s /pumpkaboo-s still get found, because it matches the
                   'gourgeist-xl':'gourgeist-super', # entry for gougeist/pumpkaboo-super
                   'pumpkaboo-s':'pumpkaboo-small',
                   'pumpkaboo-l':'pumpkaboo-large',
                   'pumpkaboo-xl':'pumpkaboo-super',
                   'giratina-o':'giratina-origin',
                   'mr.mime':'mr_mime',
                   'mimejr.':'mime_jr'
    }
    # Just in case do a double check before progressing...
    if cmd.lower() not in (robot.removeSpaces(p).lower() for p in Pokedex):
        return ReplyObject('{cmd} is not a valid command'.format(cmd = cmd), True)
    if cmd in substitutes:
        cmd = substitutes[cmd]
    generations = ('rb', 'gs', 'rs', 'dp', 'bw', 'xy', 'sm', 'ss')
    if params not in generations:
        params = generations[-1]
    if robot.canHtml(room):
        return ReplyObject('/addhtmlbox <a href="http://www.smogon.com/dex/{gen}/pokemon/{mon}/">{capital} analysis</a>'.format(gen = params, mon = cmd, capital = cmd.title()), True, True)
    return ReplyObject('Analysis: http://www.smogon.com/dex/{gen}/pokemon/{mon}/'.format(gen = params, mon = cmd), reply = True, pmreply = True)

def analysis(robot, cmd, params, user, room):
    cmd = params.split(' ')[0]
    params = params[len(cmd) + 1:]
    response = pokedex(robot, cmd, params, user, room)
    if robot.canHtml(room):
        return response.extra('<br /><sub>This command also works without `analysis`, like {char}{pokemon}</sub>'.format(char = robot.commandchar, pokemon = cmd))
    return response


commands = [
    # The easy stuff that can be done with a single lambda expression
    Command(['source', 'git'], lambda: ReplyObject('Source code can be found at: {url}'.format(url = URL()), True)),
    Command(['credits'], lambda: ReplyObject('Credits can be found: {url}'.format(url = URL()), True)),
    Command(['owner'], lambda s: ReplyObject('Owned by: {owner}'.format(owner = s.owner), True)),
    Command(['commands', 'help'], lambda: ReplyObject('Read about commands here: {url}blob/master/COMMANDS.md'.format(url = URL()), reply = True, pmreply = True)),
    Command(['explain'], lambda: ReplyObject("BB-8 is the name of a robot in the seventh Star Wars movie :)", True)),
    Command(['ask'], lambda: ReplyObject(Lines[randint(0, len(Lines) - 1)], True)),
    Command(['squid'], lambda: ReplyObject('\u304f\u30b3\u003a\u5f61', True)),
    Command(['seen'], lambda: ReplyObject("This is not a command because I value other users privacy.", True)),
    Command(['broadcast'], lambda s: ReplyObject('Rank required to broadcast: {rank}'.format(rank = s.details['broadcastrank']), True)),
    Command(['usage'], lambda: ReplyObject(usageLink, reply = True, pmreply = True)),
    Command(['pick'], lambda s, c, p: ReplyObject(choice(p.split(',')), True)),
    Command(['teambat', 'teambattle'], lambda: ReplyObject('Team Battles Explaination: https://www.smogon.com/forums/threads/ss-nu-teambats.3678407/', True)),

    # Aliasing the pokemon command because users use `analysis [pokemon]` too much
    Command(['analysis', 'dex'], analysis),

    # Generate the command list on load
    Command([link for link in YoutubeLinks], lambda s, c: ReplyObject(YoutubeLinks[c], True)),
    Command([f for f in formats], lambda s, c: ReplyObject('Format: http://www.smogon.com/dex/sm/formats/{tier}/'.format(tier = c), True)),

    # Commands with dedicated functions because of their complexity (need more than a single expression)
    Command(['get'], get),
    Command(['forcerestart'], forcerestart),
    Command(['savedetails'], savedetails),
    Command(['newautojoin'], newautojoin),
    Command(['setbroadcast'], setbroadcast),
    Command(['uptime'], uptime),
    Command(['declare'], declare),
    Command([l for l in Links], links),
    Command([t for t in tiers], randpoke),
    Command([t.replace('poke','team') for t in tiers], randteam),

    # Hardcoding the extra parameters that the regex previously took care of
    Command([re.sub(r'[^a-zA-Z0-9]', '', p).lower() for p in Pokedex] + ['pumpkaboo-s', 'pumpkaboo-l', 'pumpkaboo-xl', 'gourgeist-s', 'gourgeist-l', 'gourgeist-xl', 'giratina-o'], pokedex)
]
