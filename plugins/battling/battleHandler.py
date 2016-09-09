import re
import json
from random import randint

from data.pokedex import Pokedex
from plugins.battling.battle import Battle, Pokemon
from plugins.battling.battleLogic import getAction, getSwitch, getLead

supportedFormats = ['challengecup1v1', 'battlefactory', 'randombattle']

# This currently only work in singles and not doubles / triples
class BattleHandler:
    def __init__(self, ws, name):
        self.ws = ws
        self.botName = name
        self.activeBattles = {}

    def send(self, msg):
        self.ws.send(msg)
    def lead(self, battle, poke, rqid):
        self.send('{room}|/team {mon}|{rqid}'.format(room = battle, mon = poke, rqid = rqid))
    def act(self, battle, action, move, rqid, mega = ''):
        print('{room}|/choose {act} {move}|{rqid}'.format(room = battle, act = action, move = str(move) + mega, rqid = rqid))
        self.send('{room}|/choose {act} {move}|{rqid}'.format(room = battle, act = action, move = str(move) + mega, rqid = rqid))
    def respond(self, battle, msg):
        self.send('{room}|{msg}'.format(room = battle, msg = msg))
    def handleOutcome(self, battle, won):
        if won:
            self.respond(battle, 'O-oh, I won? Sorry :(')
        else:
            self.respond(battle, "It's okay, I didn't think I'd win anyway :>")
        print('Battle: {outcome}'.format(outcome = 'win' if won else 'loss'))

    def getSpecies(self, details):
        pokemon = details.split(',')[0].replace('-*', '')
        if pokemon == 'Floette-Eternal': pokemon = 'Floette-Eternal-Flower'
        return pokemon

    def parse(self, battle, message):
        if not message: return
        if battle in self.activeBattles and 'init' in message: return

        msg = message.split('|')
        btl = self.activeBattles[battle] if battle in self.activeBattles else None

        if not btl: return
        if 'init' == msg[1] and 'battle' == msg[2]:
            self.activeBattles[battle] = Battle(battle)
            self.respond(battle, '/timer')

        elif 'request' == msg[1]:
            # This is where all the battle picking happen
            request = json.loads(msg[2])
            if 'rqid' in request:
                self.activeBattles[battle].rqid = request['rqid']
            sidedata = request['side']
            teamSlot = 1
            for poke in sidedata['pokemon']:
                btl.me.updateTeam(
                    Pokemon(self.getSpecies(poke['details']),poke['details'],poke['condition'],poke['active'],
                            poke['stats'],poke['moves'],poke['baseAbility'],poke['item'], False, teamSlot))
                teamSlot += 1
            if 'active' in request:
                btl.myActiveData = request['active']
                for pokemon in request['side']['pokemon']:
                    if pokemon['active']:
                        btl.me.setActive(btl.me.getPokemon(self.getSpecies(pokemon['details'])))
                if 'canMegaEvo' in request['active'][0]:
                    for poke in btl.me.team:
                        if btl.me.team[poke].active:
                            btl.me.team[poke].canMega = True

            if 'forceSwitch' in request:
                if request['forceSwitch'][0]:
                    self.act(battle, 'switch', getSwitch(btl.me.team, btl.me.active.species, btl.other.active), btl.rqid)

        elif 'poke' == msg[1]:
            if not self.activeBattles[battle].me.id == msg[2]:
                species = self.getSpecies(msg[3])
                stats = {'atk':1,'def':1,'spa':1,'spd':1,'spe':1}
                moves = ['','','','']
                hasMega = True if 'hasMega' in Pokedex[species] else False
                btl.other.updateTeam(
                    Pokemon(species, msg[3], '100/100', False, stats, moves, Pokedex[species]['abilities'][0], '', hasMega, len(self.activeBattles[battle].other.team)+1))
        elif 'player' == msg[1]:
            if len(msg) < 4: return
            if msg[3] == self.botName:
                btl.setMe(msg[3], msg[2])
            else:
                btl.setOther(msg[3], msg[2])
        elif 'teampreview' == msg[1]:
            poke = getLead(btl.me.team, btl.other.team)
            self.lead(battle, poke, btl.rqid)
        elif 'turn' == msg[1]:
            action, actionType = getAction(btl, battle.split('-')[1])
            self.act(battle, actionType, action, btl.rqid)
        elif 'switch' == msg[1]:
            if msg[2].startswith(btl.me.id):
                lastActive = btl.me.active
                btl.me.setActive(btl.me.getPokemon(self.getSpecies(msg[3])))
                if not btl.me.active:
                    print('Error: No new active Pokemon!!')
                    print('Message:', msg)
                btl.me.changeTeamSlot(lastActive, btl.me.active)
            else:
                mon = self.getSpecies(msg[3])
                if mon not in btl.other.team:
                    btl.other.updateTeam(
                        Pokemon(self.getSpecies(msg[3]), msg[3], '100/100', False,
                                {'atk':1,'def':1,'spa':1,'spd':1,'spe':1}, ['','','',''], '', '', False, len(btl.other.team)+1))
                btl.other.setActive(btl.other.getPokemon(mon))
        elif msg[1] in ['win', 'tie']:
            self.handleOutcome(battle, msg[2] == self.botName)
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
                btl.me.active.canMega = False
            else:
                btl.other.removeBaseForm(msg[3], mega)

        # This keeps track of what moves the opponent has revealed
        elif 'move' == msg[1]:
            move = re.sub(r'[^a-zA-Z0-9]', '', msg[3])
            if not msg[2].startswith(btl.me.id):
                if move not in btl.other.active.moves:
                    btl.other.active.moves.append(move)

        # Boosting moves
        elif '-boost' == msg[1]:
            stat = msg[3]
            if msg[2].startswith(btl.me.id):
                btl.me.active.boosts[stat] += int(msg[4])
            else:
                btl.other.active.boosts[stat] += int(msg[4])

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

        elif 'faint' == msg[1]:
            if not msg[2].startswith(btl.me.id):
                btl.other.active.setCondition('0', 'fnt')
