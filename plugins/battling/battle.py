class Pokemon:
    def __init__(self, ident, details, condition, active, stats, moves, baseAbility, item, canMegaEvo):
        self.species = ident
        self.details = details
        self.condition = condition
        self.active = active
        self.stats = stats
        self.moves = moves
        self.baseAbility = baseAbility
        self.item = item
        self.canMega = canMegaEvo

class Player:
    def __init__(self):
        self.name = ''
        self.id = ''
        self.active = None
        self.team = {}
    def setActive(self, poke):
        self.active = poke
    def updateTeam(self, poke):
        self.team[poke.species] = poke
    def getPokemon(self, species):
        for poke in self.team:
            if self.team[poke].species == species:
                return self.team[poke]

class Battle:
    def __init__(self, name):
        self.rqid = 1
        self.myActiveData = {}
        self.me = Player()
        self.other = Player()

    def setMe(self, me, pId):
        self.me.name = me
        self.me.id = pId
    def setOther(self, other, pId):
        self.other.name = other
        self.other.id = pId
    
