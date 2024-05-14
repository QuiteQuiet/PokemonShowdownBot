from random import randint, choice
from copy import deepcopy

from data.moves import Moves
from data.pokedex import Pokedex
from data.types import Types

blacklist = {'focuspunch','fakeout','snore','dreameater','lastresort','explosion','selfdestruct','synchronoise','belch','trumphcard','wringout'}
zmoves = {'fairiumz':'twinkletackle',
    'groundiumz':'tectonicrage',
    'flyiniumz':'supersonicskystrike',
    'iciumz':'subzeroslammer',
    'psychiumz':'shatteredpsyche',
    'ghostiumz':'neverendingnightmare',
    'firiumz':'infernooverdrive',
    'wateriumz':'hydrovortex',
    'buginiumz':'savagespinout',
    'electriumz':'gigavolthavoc',
    'dragoniumz':'devastatingdrake',
    'steeliumz':'corkscrewcrash',
    'rockiumz':'continentalcrush',
    'normaliumz':'breakneckblitz',
    'grassiumz':'bloomdoom',
    'darkiniumz':'blackholeeclipse',
    'fightiniumz':'alloutpummeling',
    'poisoniumz':'aciddownpour',
    'aloraichiumz':'stokedsparksurfer',
    'marshadiumz':'soulstealing7starstrike',
    'decidiumz':'sinisterarrowraid',
    'snorliumz':'pulverizingpancake',
    'primariumz':'oceanicoperetta',
    'inciniumz':'maliciousmoonsault',
    'tapuniumz':'guardianofalola',
    'mewniumz':'genesissupernova',
    'eeviumz':'extremeevoboost',
    'pikaniumz':'catastropika',
    'pikashuniumz':'10000000voltthunderbolt',
    'kommoniumz':'clangoroussoulblaze',
    'lunaliumz':'menacingmoonrazemaelstrom',
    'lycaniumz':'splinteredstormshards',
    'mimikiumz':'letssnuggleforever',
    'solganiumz':'searingsunrazesmash',
    'ultranecroziumz':'lightthatburnsthesky'
}
dynamaxmoves = {
    "Flying": 'maxairstream',
    "Dark": 'maxdarkness',
    "Fire": 'maxflare',
    "Bug": 'maxflutterby',
    "Water": 'maxgeyser',
    "Status": 'maxguard',
    "Ice": 'maxhailstorm',
    "Fighting": 'maxknuckle',
    "Electric": 'maxlightning',
    "Psychic": 'maxmindstorm',
    "Poison": 'maxooze',
    "Grass": 'maxovergrowth',
    "Ghost": 'maxphantasm',
    "Ground": 'maxquake',
    "Rock": 'maxrockfall',
    "Fairy": 'maxstarfall',
    "Steel": 'maxsteelspike',
    "Normal": 'maxstrike',
    "Dragon": 'maxwyrmwind',
}
waterImmune = ['Dry Skin','Water Absorb','Storm Drain']
grassImmune = ['Sap Sipper']
fireImmune = ['Flash Fire', 'Well-Baked Body']
groundImmune = ['Levitate', 'Earth Eater']

def anyAbilitiyMatches(species, abilities):
    return any(abil in abilities for abil in Pokedex[species]['abilities'].values())

def getUsableZmove(pokemon):
    zcrystals = zmoves.keys()
    if not pokemon.item in zcrystals: return None
    zmovedata = deepcopy(Moves[zmoves[pokemon.item]])
    if zmovedata['basePower'] == 1:
        for move in pokemon.moves:
            if 'hiddenpower' in move:
                move = move[:-2] if not move == 'hiddenpower' else move
            for var in ('return', 'frustration'):
                if move.startswith(var):
                    move = var
            if Moves[move]['type'] == zmovedata['type']:
                zmovedata['baseMove'] = move
                if Moves[move]['category'] == 'Status':
                    zmovedata['basePower'] = 0
                    zmovedata['category'] = 'Status'
                    if 'zMoveBoost' in Moves[move]:
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
        if zmovedata['id'] == 'clangoroussoulblaze' and pokemon.species == 'Kommo-o' and 'clangingscales' in pokemon.moves: return addBase(zmovedata, 'clangingscales')
        if zmovedata['id'] == 'lightthatburnsthesky' and pokemon.species == 'Necrozma-Ultra' and 'photongeyser' in pokemon.moves: return addBase(zmovedata, 'photongeyser')
        if zmovedata['id'] == 'letssnuggleforever' and pokemon.species in ('Mimikyu', 'Mimikyu-Busted') and 'playrough' in pokemon.moves: return addBase(zmovedata, 'playrough')
        if zmovedata['id'] == 'menacingmoonrazemaelstrom' and pokemon.species in ('Lunala', 'Necrozma-Dawn-Wings') and 'moongeistbeam' in pokemon.moves: return addBase(zmovedata, 'moongeistbeam')
        if zmovedata['id'] == 'searingsunrazesmash' and pokemon.species in ('Lunala', 'Necrozma-Dusk-Mane') and 'sunsteelstrike' in pokemon.moves: return addBase(zmovedata, 'sunsteelstrike')
        if zmovedata['id'] == 'splinteredstormshards' and pokemon.species in ('Lycanroc', 'Lycanroc-Midnight', 'Lycanroc-Dusk') and 'stoneedge' in pokemon.moves: return addBase(zmovedata, 'stoneedge')
        if zmovedata['id'] == 'guardianofalola' and pokemon.species in ('Tapu Koko', 'Tapu Bulu', 'Tapu Fini', 'Tapu Lele') and 'naturesmadness' in pokemon.moves: return addBase(zmovedata, 'naturesmadness')
    # Shouldn't ever get here, but just in case do an explicit return with a specific falsy value
    return False

def getDynamaxMoves(pokemon, canDynamax=False):
    if not pokemon.dynamaxed and not canDynamax:
        return []
    maxmoves = []
    for move in pokemon.moves:
        if 'hiddenpower' in move:
            move = move[:-2] if not move == 'hiddenpower' else move
        for var in ('return', 'frustration'):
            if move.startswith(var):
                move = var
        baseMoveData = Moves[move]
        maxmove = dynamaxmoves[baseMoveData['type']]
        if baseMoveData['category'] == 'Status':
            maxmove = dynamaxmoves['Status']
        if pokemon.dynamaxed == 'gmax':
            try:
                gmaxmove = Pokedex[pokemon.species + '-Gmax']['gmaxMove']
                if Moves[gmaxmove]['type'] == baseMoveData['type']:
                    maxmove = gmaxmove
            except KeyError:
                # If a Gmax doesn't have their Gmax move yet
                pass
        # Copy to not affect the data
        maxmoveCopy = deepcopy(Moves[maxmove])
        maxmoveCopy['baseMove'] = move

        maxmoveCopy['category'] = baseMoveData['category']
        if baseMoveData['category'] != 'Status':
            try:
                gmaxPower = baseMoveData['gmaxPower']
            except KeyError:
                # No gmax power set, calculate it
                basePower = baseMoveData['basePower']
                moveType = maxmoveCopy['type']
                if not basePower:
                    gmaxPower = 100
                if moveType in ('Fighting', 'Poison'):
                    if basePower >= 150:
                        gmaxPower = 100
                    elif basePower >= 110:
                        gmaxPower = 95
                    elif basePower >= 75:
                        gmaxPower = 90
                    elif basePower >= 65:
                        gmaxPower = 85
                    elif basePower >= 45:
                        gmaxPower = 75
                    else:
                        gmaxPower = 70
                else:
                    if basePower >= 150:
                        gmaxPower = 150
                    elif basePower >= 110:
                        gmaxPower = 140
                    elif basePower >= 75:
                        gmaxPower = 130
                    elif basePower >= 65:
                        gmaxPower = 120
                    elif basePower >= 55:
                        gmaxPower = 110
                    elif basePower >= 45:
                        gmaxPower = 100
                    else:
                        gmaxPower = 90
            maxmoveCopy['basePower'] = gmaxPower
        maxmoves.append(maxmoveCopy)
    return maxmoves

def getBaseSpecies(species):
    if species in Pokedex: return species
    species = species.split('-')[0]
    return species

def getAction(battle, playing):
    active = battle.me.active
    moves = battle.myActiveData[0]['moves']
    if playing.endswith('challengecup1v1'):
        return getMove(moves, active, battle.other.active, battle), 'move'
    else:
        act = pickAction(battle, battle.me, battle.other.active)
        if act == 'switch':
            return getSwitch(battle.me, active.species, battle.other.active), 'switch'
        else:
            return getMove(moves, active, battle.other.active, battle), 'move'

def calcMatchup(me, other):
    score = 0
    if me.item.startswith('choice') and me.lastMoveUsed:
        score = calcScore(me.lastMoveUsed, me, other.species)
    else:
        for m in me.moves:
            score += calcScore(m, me, other.species)
        zmove = getUsableZmove(me)
        if zmove:
            score += calcScore(zmove, me, other.species)
        for m in getDynamaxMoves(me, canDynamax=me.side.canDynamax):
            score += calcScore(m, me, other.species)
    return score
def pickAction(battle, me, other):
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
    if 'trapped' in battle.myActiveData[0] or me.active.trapped:
        return 'move'
    return 'switch'
def getMove(moves, active, opponent, battle):
    action = ''
    move = getCC1v1Move(moves, active, opponent)
    if 'isZ' in move and active.side.canZmove:
        if battle.hackmons:
            # Call this move by its 1-indexed index not name
            for i, val in enumerate(moves):
                if val['id'] == move['id']:
                    action += '{}'.format(i + 1)
                    break
        else:
            action += '{} zmove'.format(move['baseMove'])
    elif 'isMax' in move:
        try:
            action += move['baseMove']
        except KeyError as e:
            print(moves)
            print(move)
            print(e)
        if not active.dynamaxed:
            action += ' dynamax'
    else:
        action += move['id']
    if active.side.canTera:
        action += ' terastallize'
    if active.canMega:
        action += ' mega'
    if active.canUltraBurst:
        action += ' ultra'
    return action

def getSwitch(mySide, myActiveSpecies, opponent):
    scores = {}
    myTeam = mySide.team
    for poke in myTeam:
        scores[poke] = 0
        if myTeam[poke].status == 'fnt':
            scores[poke] = -1000
            continue
        moves = myTeam[poke].moves
        for move in moves:
            scores[poke] += calcScore(move, myTeam[poke], opponent.species)
        zmove = getUsableZmove(myTeam[poke])
        if zmove:
            scores[poke] += calcScore(zmove, myTeam[poke], opponent.species)
        for move in getDynamaxMoves(myTeam[poke], canDynamax=mySide.canDynamax):
            scores[poke] += calcScore(move, myTeam[poke], opponent.species)
    m = max(scores.values())
    picks = [poke for poke,score in scores.items() if score == m]
    pick = 0
    if len(picks) == 1:
        if myActiveSpecies not in picks:
            pick = myTeam[picks[0]].teamSlot
    else:
        if myActiveSpecies in picks:
            picks.remove(myActiveSpecies)
        pick = myTeam[choice(picks)].teamSlot
    if pick <= 1:
        notFaintedMons = []
        for mon in myTeam:
            if not myTeam[mon].status == 'fnt' and not myTeam[mon].teamSlot == 1:
                notFaintedMons.append(myTeam[mon].teamSlot)
        pick = choice(notFaintedMons)
    return pick

def getCC1v1Move(moves, pokemon, opponent):
    # Moves is a list of 4 moves, possibly good or bad moves...

    # Copy this list so we don't ruin the original one when we append the Z-Move
    movescopy = []
    if not pokemon.dynamaxed:
        for move in moves:
            if 'pp' in move and move['pp'] <= 0: continue # Skip 0 pp moves
            if 'disabled' in move and move['disabled']: continue
            m = move['move'].replace(' ','').lower()
            for fault in ['-', "'"]:
                m = m.replace(fault,'')
            if m == 'recharge': return {'id': m}
            for var in ['return', 'frustration']:
                if m.startswith(var):
                    m = var
            movescopy.append(Moves[m])

            zmove = getUsableZmove(pokemon)
            if zmove:
                movescopy.append(zmove)

    # Dynamaxed Pokemon have different moves they use
    # This is also going to decide if we should dynamax
    movescopy += getDynamaxMoves(pokemon, pokemon.side.canDynamax)

    if pokemon.isChoiceLocked() and not movescopy[0]['id'] == 'struggle':
        movescopy = [Moves[pokemon.lastMoveUsed]]

    # Early return if there's only one possible option to use
    if len(movescopy) == 1:
        return movescopy[0]
    values = {}
    for move in movescopy:
        try:
            moveid = move['id']
        except KeyError as e:
            print(move)
            raise e
        mySpecies = getBaseSpecies(pokemon.species)
        oppSpecies = getBaseSpecies(opponent.species)

        if 'isZ' in move and not pokemon.side.canZmove:
            values[moveid] = 0
            continue
        # This begins a score system for the moves, naively trying to pick the best moves without calculating damage
        # Based on the move's base power
        values[moveid] = move['basePower'] if not 'calculateBasePower' in move else move['calculateBasePower'](Pokedex[mySpecies], Pokedex[oppSpecies])
        try:
            values[moveid] = move['modifyBasePower'](values[moveid], pokemon, opponent)
        except KeyError:
            pass # expected

        chargeMove = 'recharge' in Moves[moveid]['flags'] or 'charge' in Moves[moveid]['flags']
        if moveid in blacklist or chargeMove or 'mindBlownRecoil' in Moves[moveid]:
            values[moveid] = 0
            continue

        # STAB-bonus
        if move['type'] in Pokedex[mySpecies]['types']:
            values[moveid] *= 1.5

        # Stat drops and raises
        boostTable = [1, 1.5, 2, 2.5, 3, 3.5, 4]
        category = 'atk' if move['category'] == 'Physical' else 'spa'
        if 'useAlternativeOffensiveStat' in move:
            category = move['useAlternativeOffensiveStat']
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
            eff = Types[Pokedex[oppSpecies]['types'][0]][move['type']]
        if 'modifyEffectiveness' in move:
            eff = move['modifyEffectiveness'](pokemon, opponent, move, eff)
        values[moveid] *= eff

        # Abilities that give immunities
        if move['type'] == 'Water' and anyAbilitiyMatches(oppSpecies, waterImmune):
            values[moveid] = 0
        if move['type'] == 'Fire' and anyAbilitiyMatches(oppSpecies, fireImmune):
            values[moveid] = 0
        if move['type'] == 'Grass' and anyAbilitiyMatches(oppSpecies, grassImmune):
            values[moveid] = 0
        if move['type'] == 'Ground' and anyAbilitiyMatches(oppSpecies, groundImmune) or opponent.item == 'airballon':
            values[moveid] = 0

        if 'sound' in move['flags'] and anyAbilitiyMatches(oppSpecies, ['Soundproof']):
            values[moveid] = 0
        if 'wind' in move['flags'] and anyAbilitiyMatches(oppSpecies, ['Wind Rider']):
            values[moveid] = 0

        # Ignore most items for now
        if pokemon.item == 'choiceband' and move['category'] == 'Physical': values[moveid] *= 1.5
        if pokemon.item == 'choicespecs' and move['category'] == 'Special': values[moveid] *= 1.5
        if pokemon.item == 'lifeorb': values[moveid] *= 1.3

        # Status
        if pokemon.status == 'brn' and move['category'] == 'Physical':
            if pokemon.ability == 'guts':
                values[moveid] *= 1.5
            else:
                values[moveid] /= 2

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
            zmove = getUsableZmove(team[mon])
            if zmove:
                scores[mon] += calcScore(zmove, team[mon], opp)
            for move in getDynamaxMoves(team[mon], canDynamax=team[mon].side.canDynamax):
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
            move = move[:-2] if not move == 'hiddenpower' else move
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
    try:
        if mon.ability == 'sheerforce' and (move['secondary'] or "hasSheerForce" in move):
            score *= 1.2
    except KeyError as e:
        print(move)
        raise e
    if mon.ability == 'strongjaw' and 'bite' in move['flags']:
        score *= 1.5
    if mon.ability == 'sharpness' and 'slicing' in move['flags']:
        score *= 1.5
    if mon.ability in ['hugepower','purepower', 'adaptability']:
        score *= 2
    if mon.ability == 'waterbubble' and 'Water' == move['type']:
        score *= 1.5

    # Ignore most items for now
    if mon.item == 'choiceband' and move['category'] == 'Physical': score *= 1.5
    if mon.item == 'choicespecs' and move['category'] == 'Special': score *= 1.5
    if mon.item == 'lifeorb': score *= 1.3

    # Status
    if mon.status == 'brn' and move['category'] == 'Physical': score /= 2

    return score
