import re
import json
import yaml
from random import randint

from invoker import ReplyObject, Command
from data.pokedex import Pokedex
from plugins.pasteImporter import PasteImporter
from .battle import Battle, Pokemon
from .battleLogic import getAction, getSwitch, getLead
# This currently only work in singles and not doubles / triples
class BattleHandler:

    @staticmethod
    def PSPackTeam(importable):
        """This method converts a PS importable to the packed format that PS use
        to send teams to the server with

        Args:
            importable: string, the importable that should be converted to packed.
        Returns:
            String with the packed team.
        Raises:
            None.
        """
        #TODO
        return ''

    def __init__(self, ws, name):
        self.ws = ws
        self.botName = name
        self.ladderFormat = False
        self.teams = {}
        self.activeBattles = {}
        self.supportedFormats = ['battlefactory',
                                 'gen7challengecup1v1',
                                 'gen7hackmonscup',
                                 'gen7randombattle',
                                 'gen8challengecup1v1',
                                 'gen8hackmonscup',
                                 'gen8randombattle']

        try:
            with open('plugins/battling/teams.yaml', 'r') as file:
                self.teams = yaml.load(file)
            for meta in self.teams:
                self.supportedFormats.append(meta)
        except:
            # No teams.yaml file exists, so create an empty one
            with open('plugins/battling/teams.yaml', 'w+') as file:
                 yaml.dump(self.teams, file, default_flow_style = False, explicit_start = True)

    def send(self, msg):
        #print(msg) # uncomment if debugging
        self.ws.send(msg)
    def respond(self, battle, msg):
        self.send('{room}|{msg}'.format(room = battle, msg = msg))

    def newBattle(self, name):
        self.activeBattles[name] = Battle(name)

    def lead(self, battle, poke, rqid):
        self.send('{room}|/team {mon}|{rqid}'.format(room = battle, mon = poke, rqid = rqid))
    def act(self, battle, action, move, rqid):
        self.send('{room}|/choose {act} {move}|{rqid}'.format(room = battle, act = action, move = str(move), rqid = rqid))

    def makeMove(self, battle):
        try:
            action, actionType = getAction(battle, battle.name.split('-')[1])
            self.act(battle.name, actionType, action, battle.rqid)
        # There's a lot of very quiet bugs in the BattleLogic.getAction code
        # so catch all the exceptions to get information about them.
        except Exception as e:
            import traceback
            print('{}: {}'.format(type(e).__name__, e))
            traceback.print_tb(e.__traceback__)

    def handleOutcome(self, battle, won):
        if won:
            self.respond(battle.name, 'O-oh, I won?')
        else:
            self.respond(battle.name, 'I guess that was expected...')
        print('Battle: {outcome} against {opponent}'.format(outcome = 'Won' if won else 'Lost', opponent = battle.other.name))

    def getRandomTeam(self, metagame):
        try:
            teamCount = len(self.teams[metagame])
            return self.teams[metagame][randint(0, teamCount - 1)]
        except:
            # No valid team for this format. It shouldn't happen but just in case
            return ''

    def setLadderFormat(self, format):
        '''Sets the format used for laddering.

        Args:
            format: string, the format that is going to be laddered in.
        Returns:
            Bool: True if setting the team was successful, False otherwise.
        Raises:
            None.
        '''
        if not format in self.teams: return False
        self.ladderFormat = format
        return True
    def clearLadderFormat(self):
        self.ladderFormat = False

    def getSpecies(self, details):
        pokemon = details.split(',')[0].replace('-*', '')
        if pokemon in Pokedex: return pokemon
        pokemon = pokemon.split('-')[0]
        return pokemon

def init(robot, room, roomtype):
    if roomtype == 'battle': robot.bh.newBattle(room.title)

def title(robot, room, title):
    if robot.name in title:
        print('Battle: New battle between {}'.format(title))

def deinit(robot, room):
    handler = robot.bh
    battle = handler.activeBattles.pop(room.title)
    if handler.ladderFormat and battle.ladderGame:
        # Look for a new battle since the last one ended
        robot.send('|/utm {}'.format(handler.getRandomTeam(handler.ladderFormat)))
        robot.send('|/search {}'.format(handler.ladderFormat))

# Decorator for all the battle protocol functions
def battleprotocol(func):
    def wrapper(robot, room, *params):
        battle = robot.bh.activeBattles[room.title] if room.title in robot.bh.activeBattles else None
        if not battle or battle.spectating: return
        func(robot, robot.bh, battle, *params)
    return wrapper

@battleprotocol
def request(robot, bh, battle, data):
    try:
        # This is where all the battle picking happen
        request = json.loads(data)
    except ValueError as e:
        return e
    if 'rqid' in request:
        battle.rqid = request['rqid']
    sidedata = request['side']
    teamSlot = 1
    for poke in sidedata['pokemon']:
        battle.me.updateTeam(
            Pokemon(bh.getSpecies(poke['details']),poke['details'],poke['condition'],poke['active'],
                    poke['stats'],poke['moves'],poke['baseAbility'],poke['item'], False, teamSlot, battle.me))
        teamSlot += 1
    if 'active' in request:
        battle.myActiveData = request['active']
        for pokemon in request['side']['pokemon']:
            if pokemon['active']:
                battle.me.setActive(battle.me.getPokemon(bh.getSpecies(pokemon['details'])))
        if 'canMegaEvo' in request['active'][0]:
            battle.me.active.canMega = battle.me.canMegaPokemon
        if 'canUltraBurst' in request['active'][0]:
            battle.me.active.canUltraBurst = battle.me.canUltraBurst

    if 'forceSwitch' in request and request['forceSwitch'][0]:
        bh.act(battle.name, 'switch', getSwitch(battle.me, battle.me.active, battle.other.active), battle.rqid)

@battleprotocol
def rated(robot, bh, battle, rating):
    if not rating.startswith('Tournament'):
        battle.isLadderMatch()

@battleprotocol
def rule(robot, bh, battle, rule):
    if rule.startswith('Species Clause') or rule.startswith('Endless Battle Clause'):
        battle.isNotHackmons()
    if rule.startswith('Dynamax Clause'):
        battle.dynamaxAllowed(False)

@battleprotocol
def generation(robot, bh, battle, gen):
    battle.generation = int(gen)
    if battle.generation < 8:
        battle.dynamaxAllowed(False)

@battleprotocol
def pokemon(robot, bh, battle, id, pokemon, item = ''):
    if not battle.me.id == id:
        species = bh.getSpecies(pokemon)
        stats = {'atk':1,'def':1,'spa':1,'spd':1,'spe':1}
        moves = ['','','','']
        hasMega = True if 'hasMega' in Pokedex[species] else False
        battle.other.updateTeam(
            Pokemon(
                species, pokemon, '100/100', False,
                stats, moves, Pokedex[species]['abilities']['0'],
                '', hasMega, len(battle.other.team) + 1, battle.other))

@battleprotocol
def player(robot, bh, battle, pid, name, avatar = '', *rest):
    if name == robot.name:
        battle.setMe(name, pid)
        bh.respond(battle.name, '/timer on')
    else:
        battle.setOther(name, pid)

@battleprotocol
def teampreview(robot, bh, battle, *args):
    if not battle.me.id:
        battle.spectating = True
    else:
        poke = getLead(battle.me.team, battle.other.team)
        bh.lead(battle.name, poke, battle.rqid)

@battleprotocol
def turn(robot, bh, battle, number):
    bh.makeMove(battle)

@battleprotocol
def switch(robot, bh, battle, pid, details, hpstatus, cause = ''):
    if pid.startswith(battle.me.id):
        lastActive = battle.me.active
        if lastActive:
            lastActive.dynamax = False
        newActive = battle.me.getPokemon(bh.getSpecies(details))
        battle.me.setActive(newActive)
        battle.me.changeTeamSlot(lastActive, battle.me.active)
    else:
        if battle.other.active:
            battle.other.active.dynamax = False
        mon = bh.getSpecies(details)
        if mon not in battle.other.team:
            battle.other.updateTeam(Pokemon(bh.getSpecies(details), details, '100/100', False,
                        {'atk':1,'def':1,'spa':1,'spd':1,'spe':1}, ['','','',''], '', '',
                        False, len(battle.other.team) + 1, battle.other))
        battle.other.setActive(battle.other.getPokemon(mon))

@battleprotocol
def end(robot, bh, battle, winner):
    bh.handleOutcome(battle, winner == robot.name)
    bh.respond(battle.name, '/leave')

@battleprotocol
def tie(robot, bh, battle):
    bh.handleOutcome(battle, False)
    bh.respond(battle.name, '/leave')

# |-start|POKEMON|EFFECT
@battleprotocol
def start(robot, bh, battle, pid, effect, *rest):
    if effect == 'Dynamax':
        side = battle.me if pid.startswith(battle.me.id) else battle.other
        side.active.dynamaxed = True
        side.canDynamax = False

# |-end|POKEMON|EFFECT
@battleprotocol
def endEffect(robot, bh, battle, pid, effect, *rest):
    if effect == 'Dynamax':
         side = battle.me if pid.startswith(battle.me.id) else battle.other
         side.active.dynamaxed = False

# |-mega|POKEMON|SPECIES|MEGASTONE
@battleprotocol
def mega(robot, bh, battle, pid, pokemon, megastone):
    megapoke = pokemon + '-Mega'
    if pokemon in ['Charizard', 'Mewtwo']:
        megapoke += '-' + megastone.split()[1]
    side = battle.me if pid.startswith(battle.me.id) else battle.other
    side.removeBaseForm(pokemon, megapoke)
    side.canMegaPokemon = False
    side.active.canMega = False

# |-burst|POKEMON|SPECIES|ITEM
@battleprotocol
def burst(robot, bh, battle, pid, pokemon, stone):
    ultraburst = 'Necrozma-Ultra'
    side = battle.me if pid.startswith(battle.me.id) else battle.other
    # Find the necrozma (works for species clause metas only!)
    for p in side.team:
        if p.startswith(pokemon):
            pokemon = p
    side.removeBaseForm(pokemon, ultraburst)
    side.canUltraBurst = False
    side.active.canUltraBurst = False

# |-primal|POKEMON|SPECIES|MEGASTONE
@battleprotocol
def primal(robot, bh, battle, pid, pokemon='', megastone=''):
    primalpoke = pokemon + '-Primal'
    side = battle.me if pid.startswith(battle.me.id) else battle.other
    side.removeBaseForm(pokemon, primalpoke)

@battleprotocol
def formechange(robot, bh, battle, pid, forme, *rest):
    if forme.endswith('Gmax'):
        side = battle.me if pid.startswith(battle.me.id) else battle.other
        side.active.dynamaxed = 'gmax'
        side.canDynamax = False

@battleprotocol
def zmove(robot, bh, battle, pid):
    if pid.startswith(battle.me.id):
        battle.me.usedZmove()
    else:
        battle.other.usedZmove()

@battleprotocol
def move(robot, bh, battle, pid, usedmove, target, modifier = '', animation = ''):
    moveid = robot.toId(usedmove)
    if not pid.startswith(battle.me.id):
        if moveid not in battle.other.active.moves:
            battle.other.active.moves.append(moveid)
        battle.other.active.markLastUsedMove(moveid)
    else:
        battle.me.active.markLastUsedMove(moveid)

@battleprotocol
def boost(robot, bh, battle, pid, stat, amount, modifier = ''):
    if pid.startswith(battle.me.id):
        battle.me.active.boosts[stat] += int(amount)
    else:
        battle.other.active.boosts[stat] += int(amount)

@battleprotocol
def unboost(robot, bh, battle, pid, stat, amount, modifier = ''):
    if pid.startswith(battle.me.id):
        battle.me.active.boosts[stat] -= int(amount)
    else:
        battle.other.active.boosts[stat] -= int(amount)

@battleprotocol
def heal(robot, bh, battle, pid, hpstatus, by = '', help = ''):
    hp, status = (hpstatus.split() + [''])[:2] # Always get 2 values back from the split operation
    if not pid.startswith(battle.me.id):
        battle.other.active.setCondition(hp, status)
        if '[from]' == by:
            thing = by[len('[from] '):]
            if 'item:' in thing:
                battle.other.active.item = thing[len('item: '):]
            elif 'ability' in thing:
                pass

@battleprotocol
def status(robot, bh, battle, pid, condition, cause = '', of = ''):
    if not pid.startswith(battle.me.id):
        battle.other.active.setCondition(battle.other.active.condition, condition)

@battleprotocol
def faint(robot, bh, battle, pid):
    if not pid.startswith(battle.me.id):
        battle.other.active.setCondition('0', 'fnt')

@battleprotocol
def error(robot, bh, battle, cause, *information):
    if '[Invalid choice]' == cause:
        battle.me.active.trapped = True
        # Only reason for an invalid choice should be because we're trapped...
        trappingAbilities = ['Shadow Tag', 'Arena Trap', 'Magnet Pull']
        otherActiveAbilities = Pokedex[battle.other.active.species]['abilities']
        for option in otherActiveAbilities:
            if otherActiveAbilities[option] in trappingAbilities:
                battle.other.active.ability = otherActiveAbilities[option]
        print('{battle}| {active} got invalid choice, trying something else'.format(battle = battle, active = battle.me.active.species))
        bh.makeMove(battle) # Try again

def startLaddering(bot, cmd, msg, user):
    reply = ReplyObject('', reply = True)
    if not user.isOwner: return reply.response('Only owner is allowed to do this.')
    if bot.toId(msg) == 'false':
        bot.bh.clearLadderFormat()
        return reply.response('Stopped laddering.')
    if not bot.bh.setLadderFormat(msg): return reply.response('Starting to ladder failed, no valid teams for format: {}.'.format(msg))
    # Now that we know that we have valid teams for laddering, and the settings
    # to restart after finishing a game are set, we can now begin.

    # Note: To ladder in formats with random teams, add an empty string to that format in teams.yaml.
    bot.send('|/utm {}'.format(bot.bh.getRandomTeam(bot.bh.ladderFormat)))
    bot.send('|/search {}'.format(bot.bh.ladderFormat))
    return reply.response('Started laddering in format: {}'.format(bot.bh.ladderFormat))

def acceptTeam(bot, cmd, msg):
    reply = ReplyObject('', reply = True, broadcast = True)
    meta, team = msg.replace(' ', '').split(',')
    if not team: return reply.response('You forgot a team')


    # Resolve links to teams
    if team.startswith('http'):
        team = PasteImporter.getPasteContent(team)
    if not team:
        return reply.response('Unsupported paste type (probably)')
    # If the pasted team was an importable instead of packed, pack it
    if not team.startswith('|'):
        team = BattleHandler.PSPackTeam(team)
    # Double check so it actually is packed
    if not team.startswith('|'): return reply.response("This team doesn't look like a valid packed team :(")

    meta = bot.toId(meta)
    if not meta in bot.bh.teams:
        bot.bh.teams[meta] = []
    if not team in bot.bh.teams[meta]:
        bot.bh.teams[meta].append(team)
    else:
        return reply.response('I already have that team! :D')
    if not meta in bot.bh.supportedFormats:
        bot.bh.supportedFormats.append(meta)
    with open('plugins/battling/teams.yaml', 'w+') as file:
        yaml.dump(bot.bh.teams, file, default_flow_style = False, explicit_start = True)
    return reply.response('Saved that team for you so that I can play with it :)')

# Exports
handlers = {
    'init': init,
    'title': title,
    'deinit': deinit,
    'rated': rated,
    'gen': generation,
    'request': request,
    'rule': rule,
    'poke': pokemon,
    'player': player,
    'teampreview': teampreview,
    'turn': turn,
    'switch': switch,
    'win': end,
    'tie': tie,
    # In-battle events
    # Most of these events just keep track of how the game is progressing
    # as a lot of information about the own team is sent by the request for action
    '-mega': mega,
    '-burst': burst,
    '-primal': primal,
    '-zmove': zmove,
    '-zpower': zmove,
    # Dynamaxing goes by -start and -end events
    # Other volatile statuses (confusion, taunt, substitute, etc.) also use this
    '-start': start,
    '-end': endEffect,
    # Gmaxing currently only thing handled here
    '-formechange': formechange,
    # This keeps track of what moves the opponent has revealed and the last used move from either side
    'move': move,
    '-boost': boost,
    '-unboost': unboost,
    # Because of how they're treated, taking damage and healing are the same thing
    '-heal': heal,
    '-damage': heal,
    '-status': status,
    '-faint': faint,
    'error': error
}

commands = [
    Command(['storeteam'], acceptTeam),
    Command(['ladder'], startLaddering)
]
