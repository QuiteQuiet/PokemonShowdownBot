from random import randint

from data.moves import Moves
from data.pokedex import Pokedex
from data.types import Types

blacklist = {'focuspunch','fakeout','snore','dreameater','lastresort','explosion','selfdestruct','synchronoise','belch','trumphcard','wringout'}
chargemoves = {'hyperbeam','gigaimpact','frenzyplant','blastburn','hydrocannon','rockwrecker','roaroftime','bounce','dig','dive','fly','freezeshock','geomancy','iceburn','phantomforce','razorwind','shadowforce','skullbash','skyattack','skydrop','solarbeam'}
waterImmune = ['dryskin','waterabsorb','stormdrain']
grassImmune = ['sapsipper']
fireImmune = ['flashfire']
groundImmune = ['levitate']

def getAction(battle, playing):
    active = battle.me.active
    moveData = battle.myActiveData[0]['moves']
    moves = []
    if len(moveData) == 1:
        moves = [moveData[0]['move'].replace(' ','').lower()]
    else:
        moves = [m['move'].replace(' ','').lower() for m in moveData if not m['disabled']]
    if playing == 'challengecup1v1':
        return getCC1v1Move(moves, active, battle.other.active), 'move'
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
    return score
def pickAction(me, other):
    matchups = {}
    for mon in me.team:
        if not me.team[mon].condition == '0 fnt':
            matchups[mon] = calcMatchup(me.team[mon], other)
    if matchups[me.active.species] > 140:
        return 'move'
    if not randint(0,5):
        return 'move'
    best = [poke for poke,res in matchups.items() if res == max(matchups.values())]
    if best[0] == me.active.species:
        return 'move'
    fainted = 0
    for mon in me.team:
        if me.team[mon].condition == '0 fnt':
            fainted += 1
    if fainted == 5:
        return 'move'
    return 'switch'
def getMove(moves, active, opponent):
    move = getCC1v1Move(moves, active, opponent)
    if active.canMega:
        move += ' mega'
    return move
def getSwitch(myTeam, myActive, opponent):
    print('getting switch...')
    scores = {}
    for poke in myTeam:
        scores[poke] = 0
        if myTeam[poke].condition == '0 fnt':
            scores[poke] = -1000
            continue
        moves = myTeam[poke].moves
        for move in moves:
            scores[poke] += calcScore(move, myTeam[poke], opponent.species)
    m = max(scores.values())
    picks = [poke for poke,score in scores.items() if score == m]
    print(picks)
    pick = 0 # Default switch to the next member
    if len(picks) == 1:
        if myActive not in picks:
            pick = myTeam[picks[0]].teamSlot
    else:
        if myActive in picks:
            picks.remove(myActive)
        pick = myTeam[picks[randint(0,len(picks)-1)]].teamSlot
    if pick <= 1:
        notFaintedMons = []
        for mon in myTeam:
            if not myTeam[mon].condition == '0 fnt' and not myTeam[mon].teamSlot == 1:
                notFaintedMons.append(myTeam[mon].teamSlot)
        print(pick, notFaintedMons)
        pick = notFaintedMons[randint(0,len(notFaintedMons)-1)]
    return pick

def getCC1v1Move(moves, pokemon, opponent):
    # Moves is a list of 4 moves, possibly good or bad moves...
    values = {}
    for m in moves:
        m = m.replace('-','')
        # This begins a score system for the moves, naively trying to pick the best moves without calculating damage
        # Based on the move's base power
        values[m] = Moves[m]['basePower']
        if m in blacklist or m in chargemoves:
            values[m] = 0
            continue

        if Moves[m]['type'] in Pokedex[pokemon.species]['types']:
            values[m] *= 1.5
        # Multiply with the effectiveness of the move
        eff = 1
        if len(Pokedex[opponent.species]['types']) > 1:
            types = Pokedex[opponent.species]['types']
            eff = Types[types[0]][Moves[m]['type']] * Types[types[1]][Moves[m]['type']]
        else:
            eff = Types[ Pokedex[opponent.species]['types'][0] ][Moves[m]['type']]
        values[m] *= eff
        # Abilities that give immunities
        if Moves[m]['type'] == 'Water' and Pokedex[opponent.species]['abilities'][0] in waterImmune:
            values[m] = 0
        if Moves[m]['type'] == 'Fire' and Pokedex[opponent.species]['abilities'][0] in fireImmune:
            values[m] = 0
        if Moves[m]['type'] == 'Grass' and Pokedex[opponent.species]['abilities'][0] in grassImmune:
            values[m] = 0
        if Moves[m]['type'] == 'Ground' and (Pokedex[opponent.species]['abilities'][0] in groundImmune or opponent.item == 'airballon'):
            values[m] = 0
    options = [m for m,v in values.items() if v == max(values.values())]
    return options[randint(0, len(options)-1)]
 
def getLead(team, opposing):
    scores = {}
    for mon in team:
        scores[mon] = 0
        moves = team[mon].moves
        for opp in opposing:
            for move in moves:
                scores[mon] += calcScore(move, team[mon], opp)
    try:
        m = max(scores.values())
        options = [poke for poke,score in scores.items() if score == m]
        return team[options[randint(0,len(options)-1)]].teamSlot
    except ValueError:
        return randint(1,6)

def calcScore(move, mon, opponents):
    ''' Calculates an arbitrary score for a move against an opponent to decide how good it is '''
    if 'hiddenpower' in  move:
        move = move[:-2]
    move = move.replace("'",'')
    move = Moves[move]
    opp = Pokedex[opponents]

    score = move['basePower'] - (100 - move['accuracy'])
    # Bias
    oBias = 'Physical' if mon.stats['atk'] > mon.stats['spa'] else 'Special'
    if mon.stats['atk'] == mon.stats['spa']:
        oBias = 'No bias'
    dBias = 'Physical' if opp['baseStats']['atk'] > opp['baseStats']['spa'] else 'Special'
    if opp['baseStats']['atk'] == opp['baseStats']['spa']:
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
    # Ignore items
    return score
