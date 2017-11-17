import re
import json
import yaml
from random import randint

from invoker import ReplyObject, Command
from data.pokedex import Pokedex
from plugins.pasteImporter import PasteImporter
from plugins.battling.battle import Battle, Pokemon
from plugins.battling.battleLogic import getAction, getSwitch, getLead
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
        self.supportedFormats = ['gen7challengecup1v1', 'gen7hackmonscup', 'battlefactory', 'gen7randombattle']

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
        self.ws.send(msg)
    def respond(self, battle, msg):
        self.send('{room}|{msg}'.format(room = battle, msg = msg))

    def lead(self, battle, poke, rqid):
        self.send('{room}|/team {mon}|{rqid}'.format(room = battle, mon = poke, rqid = rqid))
    def act(self, battle, action, move, rqid):
        print('{room}|/choose {act} {move}|{rqid}'.format(room = battle, act = action, move = str(move), rqid = rqid))
        self.send('{room}|/choose {act} {move}|{rqid}'.format(room = battle, act = action, move = str(move), rqid = rqid))

    def makeMove(self, battle, roomname):
        try:
            action, actionType = getAction(battle, roomname.split('-')[1])
            self.act(roomname, actionType, action, battle.rqid)
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

    def parse(self, battle, message):
        if not message: return
        if not message.startswith('|'): return
        if battle in self.activeBattles and message.startswith('|init'): return

        msg = message.split('|')

        if 'init' == msg[1] and 'battle' == msg[2]:
            self.activeBattles[battle] = Battle(battle)
        if 'deinit' == msg[1]:
            room = self.activeBattles.pop(battle)
            if self.ladderFormat and room.ladderGame:
                # Look for a new battle since the last one ended
                self.send('|/utm {}'.format(self.getRandomTeam(self.ladderFormat)))
                self.send('|/search {}'.format(self.ladderFormat))

        if 'rated' == msg[1]:
            self.activeBattles[battle].isLadderMatch()

        btl = self.activeBattles[battle] if battle in self.activeBattles else None
        if not btl or btl.spectating: return
        if 'request' == msg[1]:
            try:
                # This is where all the battle picking happen
                request = json.loads(msg[2])
            except ValueError as e:
                return e
            if 'rqid' in request:
                self.activeBattles[battle].rqid = request['rqid']
            sidedata = request['side']
            teamSlot = 1
            for poke in sidedata['pokemon']:
                btl.me.updateTeam(
                    Pokemon(self.getSpecies(poke['details']),poke['details'],poke['condition'],poke['active'],
                            poke['stats'],poke['moves'],poke['baseAbility'],poke['item'], False, teamSlot, btl.me))
                teamSlot += 1
            if 'active' in request:
                btl.myActiveData = request['active']
                for pokemon in request['side']['pokemon']:
                    if pokemon['active']:
                        btl.me.setActive(btl.me.getPokemon(self.getSpecies(pokemon['details'])))
                if 'canMegaEvo' in request['active'][0]:
                    btl.me.active.canMega = btl.me.canMegaPokemon
                if 'canUltraBurst' in request['active'][0]:
                    btl.me.active.canUltraBurst = btl.me.canUltraBurst

            if 'forceSwitch' in request and request['forceSwitch'][0]:
                self.act(battle, 'switch', getSwitch(btl.me.team, btl.me.active.species, btl.other.active), btl.rqid)

        elif 'poke' == msg[1]:
            if not self.activeBattles[battle].me.id == msg[2]:
                species = self.getSpecies(msg[3])
                stats = {'atk':1,'def':1,'spa':1,'spd':1,'spe':1}
                moves = ['','','','']
                hasMega = True if 'hasMega' in Pokedex[species] else False
                btl.other.updateTeam(
                    Pokemon(species, msg[3], '100/100', False, stats, moves, Pokedex[species]['abilities']['0'], '', hasMega, len(self.activeBattles[battle].other.team) + 1, btl.other))
        elif 'player' == msg[1]:
            if len(msg) < 4: return
            if msg[3] == self.botName:
                btl.setMe(msg[3], msg[2])
                self.respond(battle, '/timer on')
            else:
                btl.setOther(msg[3], msg[2])
        elif 'teampreview' == msg[1]:
            if not btl.me.id:
                btl.spectating = True
            else:
                poke = getLead(btl.me.team, btl.other.team)
                self.lead(battle, poke, btl.rqid)
        elif 'turn' == msg[1]:
            self.makeMove(btl, battle)
        elif 'switch' == msg[1]:
            if msg[2].startswith(btl.me.id):
                lastActive = btl.me.active
                newActive = btl.me.getPokemon(self.getSpecies(msg[3]))
                btl.me.setActive(newActive)
                btl.me.changeTeamSlot(lastActive, btl.me.active)
            else:
                mon = self.getSpecies(msg[3])
                if mon not in btl.other.team:
                    btl.other.updateTeam(Pokemon(self.getSpecies(msg[3]), msg[3], '100/100', False,
                                {'atk':1,'def':1,'spa':1,'spd':1,'spe':1}, ['','','',''], '', '', False, len(btl.other.team)+1, btl.other))
                btl.other.setActive(btl.other.getPokemon(mon))
        elif msg[1] in ['win', 'tie']:
            self.handleOutcome(btl, msg[2] == self.botName)
            self.respond(battle, '/leave')

        # In-battle events
        # Most of these events just keep track of how the game is progressing
        # but as a lot of information about the own team is sent by the request for action
        elif '-mega' == msg[1]:
            mega = msg[3] + '-Mega'
            if msg[3] in ['Charizard', 'Mewtwo']:
                mega += '-' + msg[4].split()[1]
            if msg[2].startswith(btl.me.id):
                btl.me.removeBaseForm(msg[3], mega)
                btl.me.canMegaPokemon = False
                btl.me.active.canMega = False
            else:
                btl.other.removeBaseForm(msg[3], mega)
                btl.other.canMegaPokemon = False
                btl.other.active.canMega = False
        elif '-ultra' == msg[1]:
            ultraburst = msg[3] + '-Ultra'
            if msg[2].startswith(btl.me.id):
                btl.me.removeBaseForm(msg[3], ultraburst)
                btl.me.canUltraBurst = False
                btl.me.active.canUltraBurst = False
            else:
                btl.other.removeBaseForm(msg[3], ultraburst)
                btl.other.canUltraBurst = False
                btl.other.active.canUltraBurst = False

        elif '-zmove' == msg[1] or '-zpower' == msg[1]:
            if msg[2].startswith(btl.me.id):
                btl.me.usedZmove()
            else:
                btl.other.usedZmove()

        # This keeps track of what moves the opponent has revealed and the last used move from either side
        elif 'move' == msg[1]:
            move = re.sub(r'[^a-zA-Z0-9]', '', msg[3]).lower()
            if not msg[2].startswith(btl.me.id):
                if move not in btl.other.active.moves:
                    btl.other.active.moves.append(move)
                btl.other.active.markLastUsedMove(move)
            else:
                btl.me.active.markLastUsedMove(move)

        # Boosting moves
        elif '-boost' == msg[1]:
            stat = msg[3]
            if msg[2].startswith(btl.me.id):
                btl.me.active.boosts[stat] += int(msg[4])
            else:
                btl.other.active.boosts[stat] += int(msg[4])
        elif '-unboost' == msg[1]:
            stat = msg[3]
            if msg[2].startswith(btl.me.id):
                btl.me.active.boosts[stat] -= int(msg[4])
            else:
                btl.other.active.boosts[stat] -= int(msg[4])

        # Because of how they're treated, taking damage and healing it are done the same things to
        elif msg[1] in ['-heal','-damage']:
            parts = msg[3].split()
            if not msg[2].startswith(btl.me.id):
                btl.other.active.setCondition(parts[0], parts[1] if ' ' in msg[3] else '')
                if '[from]' in message:
                    thing = msg[4][len('[from] '):]
                    if 'item:' in thing:
                        btl.other.active.item = thing[len('item: '):]
                    elif 'ability' in thing:
                        pass
        elif '-status' == msg[1]:
            if not msg[2].startswith(btl.me.id):
                btl.other.active.setCondition(btl.other.active.condition, msg[3])

        # hack to make sure the game progresses if we're trapped and still try to switch
        elif 'callback' == msg[1]:
            # split to account for shorter messages
            if 'trapped' == msg[2]:
                btl.me.active.trapped = True
                # Figure out what ability trapped us (nothing have more than one ability that can trap)
                # This doesn't account for trapping moves but that's okay
                trappingAbilities = ['Shadow Tag', 'Arena Trap', 'Magnet Pull']
                otherActiveAbilities = Pokedex[btl.other.active.species]['abilities']
                for option in otherActiveAbilities:
                    if otherActiveAbilities[option] in trappingAbilities:
                        btl.other.active.ability = otherActiveAbilities[option]
                print('{battle}| {active} is trapped, trying something else'.format(battle = battle, active = btl.me.active.species))
                self.makeMove(btl, battle) # Try again

        elif 'faint' == msg[1]:
            if not msg[2].startswith(btl.me.id):
                btl.other.active.setCondition('0', 'fnt')

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

commands = [
    Command(['storeteam'], acceptTeam),
    Command(['ladder'], startLaddering)
]
