from random import randint, choice
from copy import deepcopy

from data.moves import Moves
from data.pokedex import Pokedex
from data.types import Types

blacklist = {'focuspunch','fakeout','snore','dreameater','lastresort','explosion','selfdestruct','synchronoise','belch','trumphcard','wringout'}
chargemoves = {'hyperbeam','gigaimpact','frenzyplant','blastburn','hydrocannon','rockwrecker','roaroftime','bounce','dig','dive','fly','freezeshock','geomancy','iceburn','phantomforce','razorwind','shadowforce','skullbash','skyattack','skydrop','solarbeam'}
zmoves = {'fairiumz':'twinkletackle', 'groundiumz':'tectonicrage', 'flyiniumz':'supersonicskystrike', 'iciumz':'subzeroslammer', 'aloraichiumz':'stokedsparksurfer', 'marshadiumz':'soulstealing7starstrike', 'decidiumz':'sinisterarrowraid', 'psychiumz':'shatteredpsyche', 'buginiumz':'savagespinout', 'snorliumz':'pulverizingpancake', 'primariumz':'oceanicoperetta', 'ghostiumz':'neverendingnightmare', 'inciniumz':'maliciousmoonsault', 'firiumz':'infernooverdrive', 'wateriumz':'hydrovortex', 'tapuniumz':'guardianofalola', 'electriumz':'gigavolthavoc', 'mewniumz':'genesissupernova', 'eeviumz':'extremeevoboost', 'dragoniumz':'devastatingdrake', 'steeliumz':'corkscrewcrash', 'rockiumz':'continentalcrush', 'pikaniumz':'catastropika', 'normaliumz':'breakneckblitz', 'grassiumz':'bloomdoom', 'darkiniumz':'blackholeeclipse', 'fightiniumz':'alloutpummeling', 'poisoniumz':'aciddownpour', 'pikashuniumz':'10000000voltthunderbolt'}
waterImmune = ['Dry Skin','Water Absorb','Storm Drain']
grassImmune = ['Sap Sipper']
fireImmune = ['Flash Fire']
groundImmune = ['Levitate']

def getUsableZmove(pokemon):
    zcrystals = zmoves.keys()
    if not pokemon.item in zcrystals: return None
    zmovedata = deepcopy(Moves[zmoves[pokemon.item]])
    if zmovedata['basePower'] == 1:
        for move in pokemon.moves:
            for var in ('return', 'frustration'):
                if move.startswith(var):
                    move = var
            if Moves[move]['type'] == zmovedata['type']:
                zmovedata['baseMove'] = move
                if Moves[move]['category'] == 'Status':
                    zmovedata['basePower'] = 0
                    zmovedata['category'] = 'Status'
                    if Moves[move]['zMoveBoost']:
                        zmovedata['boosts'] = Moves[move]['zMoveBoost']
                else:
                    zmovedata['basePower'] = Moves[move]['zMovePower']
        # If no move matches this isn't a Z-Crystal we can use
        if zmovedata['basePower'] == 1: return None
        # Status Z-Moves are technically fine to use
        return zmovedata
    else:
        # Only need this right here
        def addBase(zmove, base):
            zmove['baseMove'] = base
            return zmove
        # Only special Z-Moves like Sinister Arrow Raid has a base power so check if they're usable
        if zmovedata['id'] == 'catastropika' and pokemon.species == 'Pikachu' and 'thunderbolt' in pokemon.moves: return addBase(zmovedata, 'thunderbolt')
        if zmovedata['id'] == 'extremeevoboost' and pokemon.species == 'Eevee' and 'lastresort' in pokemon.moves: return addBase(zmovedata, 'lastresort')
        if zmovedata['id'] == 'genesissupernova' and pokemon.species == 'Mew' and 'psychic' in pokemon.moves: return addBase(zmovedata, 'psychic')
        if zmovedata['id'] == 'sinisterarrowraid' and pokemon.species == 'Deucideye' and 'spiritshackle' in pokemon.moves: return addBase(zmovedata, 'spiritshackle')
        if zmovedata['id'] == 'stokedsparksurfer' and pokemon.species == 'Raichu-Alola' and 'thunderbolt' in pokemon.moves: return addBase(zmovedata, 'thunderbolt')
        if zmovedata['id'] == 'pulverizingpancake' and pokemon.species == 'Snorlax' and 'gigaimpact' in pokemon.moves: return addBase(zmovedata, 'gigaaimpact')
        if zmovedata['id'] == 'maliciousmoonsault' and pokemon.species == 'Incineroar' and 'darkestlariat' in pokemon.moves: return addBase(zmovedata, 'darklariat')
        if zmovedata['id'] == 'oceanicoperetta' and pokemon.species == 'Primarina' and 'sparklingaria' in pokemon.moves: return addBase(zmovedata, 'sparklingaria')
        if zmovedata['id'] == 'soulstealing7starstrike' and pokemon.species == 'Marshadow' and 'spectralthief' in pokemon.moves: return addBase(zmovedata, 'spectralthief')
        if zmovedata['id'] == 'guardianofalola' and pokemon.species in ('Tapu Koko', 'Tapu Bulu', 'Tapu Fini', 'Tapu Lele') and 'naturesmadness' in pokemon.moves: return addBase(zmovedata, 'naturesmadness')
    # Shouldn't ever get here, but just in case do an explicit return with a specific falsy value
    return False

def getBaseSpecies(species):
    if species in Pokedex: return species
    species = species.split('-')[0]
    return species

def getAction(battle, playing):
    active = battle.me.active
    moveData = battle.myActiveData[0]['moves']
    moves = []
    if len(moveData) == 1:
        moves = [moveData[0]['move'].replace(' ','').lower()]
    else:
        moves = [m['move'].replace(' ','').lower() for m in moveData if not m['disabled']]
    if playing == 'gen7challengecup1v1':
        return getMove(moves, active, battle.other.active), 'move'
    else:
        act = pickAction(battle.me, battle.other.active)
        if act == 'switch':
            return getSwitch(battle.me.team, battle.me.active.species, battle.other.active), 'switch'
        else:
            return getMove(moves, active, battle.other.active), 'move'
def calcMatchup(me, other):
    score = 0
    for m in me.moves:
        score += calcScore(m, me, other.species)
    zmove = getUsableZmove(me)
    if zmove:
        score += calcScore(zmove, me, other.species)
    return score
def pickAction(me, other):
    matchups = {}
    for mon in me.team:
        if not me.team[mon].status == 'fnt':
            matchups[mon] = calcMatchup(me.team[mon], other)
    if matchups[me.active.species] > 140:
        return 'move'
    best = [poke for poke,res in matchups.items() if res == max(matchups.values())]
    if best[0] == me.active.species:
        return 'move'
    fainted = 0
    for mon in me.team:
        if me.team[mon].status == 'fnt':
            fainted += 1
    if fainted == 5:
        return 'move'
    if not randint(0,5):
        return 'move'
    return 'switch'
def getMove(moves, active, opponent):
    action = ''
    move = getCC1v1Move(moves, active, opponent)
    if 'isZ' in move and active.side.canZmove:
        action += '{} zmove'.format(move['baseMove'])
    else:
        action += move['id']
    if active.canMega and active.side.canMegaPokemon:
        action += ' mega'
    return action
def getSwitch(myTeam, myActive, opponent):
    scores = {}
    for poke in myTeam:
        scores[poke] = 0
        if myTeam[poke].status == 'fnt':
            scores[poke] = -1000
            continue
        moves = myTeam[poke].moves
        for move in moves:
            scores[poke] += calcScore(move, myTeam[poke], opponent.species)
    m = max(scores.values())
    picks = [poke for poke,score in scores.items() if score == m]
    pick = 0
    try:
        if len(picks) == 1:
            if myActive not in picks:
                pick = myTeam[picks[0]].teamSlot
        else:
            if myActive in picks:
                picks.remove(myActive)
            pick = choice(myTeam).teamSlot
        if pick <= 1:
            notFaintedMons = []
            for mon in myTeam:
                if not myTeam[mon].status == 'fnt' and not myTeam[mon].teamSlot == 1:
                    notFaintedMons.append(myTeam[mon].teamSlot)
            pick = choice(notFaintedMons)
        return pick
    except Exception as e:
        print(e)
        return randint(1, 6)

def getCC1v1Move(moves, pokemon, opponent):
    # Moves is a list of 4 moves, possibly good or bad moves...

    # Copy this list so we don't ruin the original one when we append the Z-Move
    movescopy = []
    for m in moves:
        for fault in ['-', "'"]:
            m = m.replace(fault,'')
        if m == 'recharge': return m
        for var in ['return', 'frustration']:
            if m.startswith(var):
                m = var
        movescopy.append(Moves[m])
    zmove = getUsableZmove(pokemon)
    if zmove:
        movescopy.append(zmove)
    values = {}
    for move in movescopy:
        moveid = move['id']
        mySpecies = getBaseSpecies(pokemon.species)
        oppSpecies = getBaseSpecies(opponent.species)

        if 'isZ' in move and not pokemon.side.canZmove:
            values[moveid] = 0
            continue
        # This begins a score system for the moves, naively trying to pick the best moves without calculating damage
        # Based on the move's base power
        values[moveid] = move['basePower'] if not 'calculateBasePower' in move else move['calculateBasePower'](Pokedex[mySpecies], Pokedex[oppSpecies])

        if moveid in blacklist or moveid in chargemoves:
            values[moveid] = 0
            continue

        # STAB-bonus
        if move['type'] in Pokedex[mySpecies]['types']:
            values[moveid] *= 1.5

        # Stat drops and raises
        boostTable = [1, 1.5, 2, 2.5, 3, 3.5, 4]
        category = 'atk' if move['category'] == 'Physical' else 'spa'
        if pokemon.boosts[category] > 0 or opponent.boosts[category] < 0:
            values[moveid] *= boostTable[pokemon.boosts[category]]
        if pokemon.boosts[category] < 0 or opponent.boosts[category] > 0:
            values[moveid] /= boostTable[-pokemon.boosts[category]]


        # Multiply with the effectiveness of the move
        eff = 1
        if len(Pokedex[oppSpecies]['types']) > 1:
            types = Pokedex[oppSpecies]['types']
            eff = Types[types[0]][move['type']] * Types[types[1]][move['type']]
        else:
            eff = Types[ Pokedex[oppSpecies]['types'][0] ][move['type']]
        values[moveid] *= eff
        # Abilities that give immunities
        if move['type'] == 'Water' and Pokedex[oppSpecies]['abilities']['0'] in waterImmune:
            values[moveid] = 0
        if move['type'] == 'Fire' and Pokedex[oppSpecies]['abilities']['0'] in fireImmune:
            values[moveid] = 0
        if move['type'] == 'Grass' and Pokedex[oppSpecies]['abilities']['0'] in grassImmune:
            values[moveid] = 0
        if move['type'] == 'Ground' and Pokedex[oppSpecies]['abilities']['0'] in groundImmune or opponent.item == 'airballon':
            values[moveid] = 0
    options = [m for m,v in values.items() if v == max(values.values())]
    picked = choice(options)
    return [m for m in movescopy if m['id'] == picked][0]

def getLead(team, opposing):
    scores = {}
    for mon in team:
        scores[mon] = 0
        moves = team[mon].moves
        for opp in opposing:
            for move in moves:
                scores[mon] += calcScore(move, team[mon], opp)
    m = max(scores.values())
    options = [poke for poke,score in scores.items() if score == m]
    if len(options) > 0:
        return team[choice(options)].teamSlot
    else:
        print('WARNING: Failed to pick proper lead, using random.')
        return randint(1, 6)

def calcScore(move, mon, opponents):
    ''' Calculates an arbitrary score for a move against an opponent to decide how good it is '''
    if type(move) is str:
        if 'hiddenpower' in  move:
            move = move[:-2]
        for var in ['return', 'frustration']:
            if move.startswith(var):
                move = var
        move = move.replace("'",'')
        move = Moves[move]
    opp = Pokedex[getBaseSpecies(opponents)]

    score = move['basePower'] - (100 - move['accuracy'])

    oBias = 'Physical' if mon.stats['atk'] > mon.stats['spa'] else 'Special'
    if mon.stats['atk'] == mon.stats['spa']:
        oBias = 'No bias'
    dBias = 'Physical' if opp['baseStats']['def'] > opp['baseStats']['spd'] else 'Special'
    if opp['baseStats']['def'] == opp['baseStats']['spd']:
        dBias = 'No bias'
    if move['category'] == oBias:
        score += 10
    if move['category'] == dBias:
        score -= 10
    # Typing
    eff = Types[opp['types'][0]][move['type']]
    if len(opp['types']) > 1:
        eff *= Types[opp['types'][1]][move['type']]
    score *= eff
    # Ability
    if mon.ability == 'sheerforce' and not move['secondary'] == False:
        score *= 1.2
    if mon.ability == 'strongjaw' and 'bite' in move['flags']:
        score *= 1.5
    if mon.ability in ['hugepower','purepower', 'adaptability']:
        score *= 2
    # Ignore items for now
    return score
