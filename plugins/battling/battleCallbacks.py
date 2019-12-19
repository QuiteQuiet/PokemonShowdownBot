import math

from data.pokedex import Pokedex

def getBaseSpecies(species):
    if species in Pokedex: return species
    species = species.split('-')[0]
    return species

def relativeWeightBasedBasePower(attacker, defender):
	aWeight = attacker['weightkg']
	dWeight = defender['weightkg']
	if aWeight > dWeight * 5: return 120
	if aWeight > dWeight * 4: return 100
	if aWeight > dWeight * 3: return 80
	if aWeight > dWeight * 2: return 60
	return 40

def absoluteWeightBasedBasePower(_, defender):
    weight = defender['weightkg']
    if weight >= 2000: return 120
    if weight >= 1000: return 100
    if weight >= 500: return 80
    if weight >= 250: return 60
    if weight >= 100: return 40
    return 20

def noItemBoost(cur, attacker, _):
    if not attacker.item:
        return cur * 2
    return cur

def targetStatusBoosted(cur, _, target):
    if target.condition or target.ability == "Comatose": return cur * 2
    return cur

def variableBasedOnHpPercentageRemaining(cur, attacker, _):
    hp, maxhp = map(int, attacker.condition.split('/'))
    return cur * (hp / maxhp)

def variableBasedOnHpRatioRemaining(cur, attacker, _):
    hp, maxhp = map(int, attacker.condition.split('/'))
    ratio = hp * 48 / maxhp
    if ratio < 2: return 200
    if ratio < 5: return 150
    if ratio < 10: return 100
    if ratio < 17: return 80
    if ratio < 33: return 40
    return 20

def doublesAgainstDynamax(cur, _, defender):
    return cur * 2 if defender.dynamaxed else cur

def doublesIfMovingFirst(cur, attacker, defender):
    # Approximation, but good enough
    atkSpeed = Pokedex[getBaseSpecies(attacker.species)]['baseStats']['spe']
    defSpeed = Pokedex[getBaseSpecies(defender.species)]['baseStats']['spe']
    boostTable = [1, 1.5, 2, 2.5, 3, 3.5, 4]
    if attacker.boosts['spe'] > 0:
        atkSpeed *= boostTable[attacker.boosts['spe']]
    if defender.boosts['spe'] > 0:
        defSpeed *= boostTable[defender.boosts['spe']]
    if attacker.boosts['spe'] < 0:
        atkSpeed /= boostTable[attacker.boosts['spe']]
    if defender.boosts['spe'] < 0:
        defSpeed /= boostTable[defender.boosts['spe']]
    if attacker.item == 'choicescarf':
        atkSpeed *= 1.5
    if defender.item == 'choicescarf':
        defSpeed *= 1.5
    if atkSpeed > defSpeed:
        return cur * 2
    return cur
