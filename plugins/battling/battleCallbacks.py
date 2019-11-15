import math

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
    if defender.condition or defender.ability == "Comatose": return cur * 2
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
