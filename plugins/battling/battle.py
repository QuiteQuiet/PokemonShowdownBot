class Pokemon:
    def __init__(self, ident, details, condition, active, stats, moves, baseAbility, item, canMegaEvo, slot):
        self.species = ident
        self.details = details
        self.condition = condition.split()[0]
        self.status = condition.split()[1] if ' ' in condition else ''
        self.active = active
        self.stats = stats
        self.moves = moves
        self.ability = baseAbility
        self.item = item
        self.canMega = canMegaEvo
        self.teamSlot = slot
        self.boosts = {'atk':0, 'def':0, 'spa':0, 'spd':0, 'spe':0, 'evasion':0, 'accuracy':0}
    def setCondition(self, cond, status):
        self.condition = cond
        self.status = status

class Player:
    def __init__(self):
        self.name = ''
        self.id = ''
        self.active = None
        self.team = {}
        self.side = {}
    def setActive(self, poke):
        self.active = poke
    def updateTeam(self, poke):
        self.team[poke.species] = poke
    def changeTeamSlot(self, old, new):
        if not old:
            for m in self.team:
                if self.team[m]:
                    old = self.team[m]
        print('switching',old.species)
        print('with',new.species)
        old.teamSlot, new.teamSlot = new.teamSlot, old.teamSlot
        for m in self.team:
            print(self.team[m].teamSlot, m)
    def getPokemon(self, species):
        for poke in self.team:
            if self.team[poke].species == species:
                return self.team[poke]
    def removeBaseForm(self, pokemon, mega):
        self.team[mega] = self.team.pop(pokemon, None)
        self.team[mega].species = mega

class Battle:
    def __init__(self, name):
        self.rqid = 1
        self.myActiveData = {}
        self.me = Player()
        self.other = Player()
        self.field = {}

    def setMe(self, me, pId):
        self.me.name = me
        self.me.id = pId
    def setOther(self, other, pId):
        self.other.name = other
        self.other.id = pId
    def setFieldCond(self, cond):
        pass
    
