from random import randint

from data.moves import Moves
from data.pokedex import Pokedex
from data.types import Types

blacklist = {'focuspunch','fakeout','snore','dreameater','lastresort','explosion','selfdestruct','synchronoise','belch','trumphcard','wringout'}
chargemoves = {'hyperbeam','gigaimpact','frenzyplant','blastburn','hydrocannon','rockwrecker','roaroftime','bounce','dig','dive','fly','freezeshock','geomancy','iceburn','phantomforce','razorwind','shadowforce','skullbash','skyattack','skydrop','solarbeam'}
def getMove(moves, pokemon, opponent):
    # Moves is a list of 4 moves, possibly good or bad moves...
    options = []
    for m in moves:
        m = m.replace('-','')
        if m in blacklist or m in chargemoves:
            continue
        # Anything under 40 base power is probably useless (priority is 40)
        if (Moves[m]['basePower'] > 40 or m in ['grass knot', 'low kick']):
            options.append(m)
        if Moves[m]['type'] in Pokedex[pokemon.species]['types'] and Moves[m]['basePower'] > 30:
            options.append(m)
        if m not in options:
            continue
        # Resisted moves get 0 or 1 entry (1 only if STAB and over 40 base power)
        if len(Pokedex[opponent.species]['types']) > 1:
            types = Pokedex[opponent.species]['types']
            eff = Types[types[0]][Moves[m]['type']] * Types[types[1]][Moves[m]['type']]
            if eff < 1:
                options.remove(m)
        else:
            eff = Types[ Pokedex[opponent.species]['types'][0] ][Moves[m]['type']]
            if eff < 1:
                options.remove(m)
    if len(options) == 0:
        return moves[randint(0, len(moves)-1)]
    # This will pick moves that have a much higher possible damage output than guessing
    # since it will always use the better attacking stat (hopefully with a good base power move)
    for o in options:
        if pokemon.stats['atk'] > (50 + pokemon.stats['spa']) and Moves[m]['category'] == 'Physical':
            return o
        if (pokemon.stats['atk'] + 50) < pokemon.stats['spa'] and Moves[m]['category'] == 'Special':
            return o
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
        return randint(1.6)


def calcScore(move, mon, opponents):
    ''' Calculates an arbitrary score for a move against an opponent to decide how good it is '''
    if 'hiddenpower' in  move:
        move = move[:-2]
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
