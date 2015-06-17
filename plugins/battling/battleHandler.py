import re
import json
from random import randint

from data.pokedex import Pokedex
from plugins.battling.battle import Battle, Pokemon
from plugins.battling.battleLogic import getAction, getSwitch, getLead

supportedFormats = ['challengecup1v1', 'battlefactory', 'randombattle']

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

    def getSpecies(self, details):
        return details.split(',')[0].replace('-*', '')

    def parse(self, battle, msg):
        if not msg: return
        if battle in self.activeBattles and 'init' in msg: return
        msg = msg.split('|')
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
                self.activeBattles[battle].me.updateTeam(
                    Pokemon(self.getSpecies(poke['details']),poke['details'],poke['condition'],poke['active'],
                            poke['stats'],poke['moves'],poke['baseAbility'],poke['item'],poke['canMegaEvo'], teamSlot))
                teamSlot += 1
            if 'active' in request:
                self.activeBattles[battle].myActiveData = request['active']
            # This doesn't work for fainting
            if 'forceSwitch' in request:
                if request['forceSwitch'][0]:
                    curBattle = self.activeBattles[battle]
                    self.act(battle, 'switch', getSwitch(curBattle.me.team, curBattle.me.active, curBattle.other.active), curBattle.rqid)
                
        elif 'poke' == msg[1]:
            if not self.activeBattles[battle].me.id == msg[2]:
                species = self.getSpecies(msg[3])
                stats = {'atk':1,'def':1,'spa':1,'spd':1,'spe':1}
                moves = ['','','','']
                hasMega = True if 'hasMega' in Pokedex[species] else False
                self.activeBattles[battle].other.updateTeam(
                    Pokemon(species, msg[3], '100/100', False, stats, moves, Pokedex[species]['abilities'][0], '', hasMega, len(self.activeBattles[battle].other.team)+1))
        elif 'player' == msg[1]:
            if len(msg) < 4: return
            if msg[3] == self.botName:
                self.activeBattles[battle].setMe(msg[3], msg[2])
            else:
                self.activeBattles[battle].setOther(msg[3], msg[2])
        elif 'teampreview' == msg[1]:
            poke = getLead(self.activeBattles[battle].me.team, self.activeBattles[battle].other.team)
            self.lead(battle, poke, self.activeBattles[battle].rqid)
        elif 'turn' == msg[1]:
            action, actionType = getAction(self.activeBattles[battle], battle.split('-')[1])
            self.act(battle, actionType, action, self.activeBattles[battle].rqid)
        elif 'switch' == msg[1]:
            btl = self.activeBattles[battle]
            if msg[2].startswith(btl.me.id):
                btl.me.setActive(btl.me.getPokemon(self.getSpecies(msg[3])))
                btl.me.updateTeamSlots()
            else:
                mon = self.getSpecies(msg[3])
                if mon not in btl.other.team:
                    self.activeBattles[battle].other.updateTeam(
                        Pokemon(self.getSpecies(msg[3]), msg[3], '100/100', False,
                                {'atk':1,'def':1,'spa':1,'spd':1,'spe':1}, ['','','',''], '', '', False, len(self.activeBattles[battle].other.team)+1))
                btl.other.setActive(btl.other.getPokemon(mon))
        elif msg[1] in ['win', 'tie']:
            if msg[2] == self.botName:
                self.respond(battle, 'O-oh, I won? Sorry :(')
            else:
                self.respond(battle, "It's okay, I didn't think I'd win anyway :>")
            self.respond(battle, '/leave')
