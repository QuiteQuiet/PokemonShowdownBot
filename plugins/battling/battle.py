class Pokemon:
    def __init__(self, ident, details, condition, active, stats, moves, baseAbility, item, teraType, canMegaEvo, hasTera, slot, side):
        self.species = ident
        self.details = details
        self.condition = condition.split()[0]
        self.status = condition.split()[1] if ' ' in condition else ''
        self.active = active
        self.stats = stats
        self.moves = moves
        self.ability = baseAbility
        self.item = item
        self.teamSlot = slot
        self.side = side
        self.canMega = canMegaEvo and self.side.canMegaPokemon
        self.canUltraBurst = False # Necrozma-Ultra only
        self.dynamaxed = False
        self.terastallized = bool(hasTera)
        self.teraType = teraType
        self.volatiles = set()
        self.boosts = {'atk':0, 'def':0, 'spa':0, 'spd':0, 'spe':0, 'evasion':0, 'accuracy':0}
        self.lastMoveUsed = None
        self.trapped = False

    def clearBoosts(self):
        self.boosts = {'atk':0, 'def':0, 'spa':0, 'spd':0, 'spe':0, 'evasion':0, 'accuracy':0}

    def markLastUsedMove(self, move):
        self.lastMoveUsed = move

    def clearLastUsedMove(self):
        self.lastMoveUsed = None

    def setCondition(self, cond, status):
        self.condition = cond
        self.status = status

    def setTera(self, teraType):
        self.teraType = teraType
        self.terastallized = True
        self.side.usedTera()

    def isChoiceLocked(self):
        return self.lastMoveUsed and self.item.startswith('choice') and not self.dynamaxed

class Player:
    def __init__(self):
        self.name = ''
        self.id = ''
        self.canZmove = True
        self.canMegaPokemon = True
        self.canUltraBurst = True
        self.canDynamax = True
        self.canTera = True
        self.active = None
        self.team = {}

    def setActive(self, poke):
        if self.active:
            self.active.clearBoosts()
            self.active.clearLastUsedMove()
        self.active = poke
        self.active.clearBoosts()
    def updateTeam(self, poke):
        if poke.species in self.team:
            poke.boosts = self.team[poke.species].boosts
        self.team[poke.species] = poke
    def changeTeamSlot(self, old, new):
        if not old:
            for m in self.team:
                if self.team[m]:
                    old = self.team[m]
        old.teamSlot, new.teamSlot = new.teamSlot, old.teamSlot
    def getPokemon(self, species):
        for poke in self.team:
            if self.team[poke].species == species:
                return self.team[poke]
        # Logically this shouldn't happen, but apparently it does sometimes?
        raise AttributeError('{mon} isn\'t in the team'.format(mon = species))
    def removeBaseForm(self, pokemon, mega):
        self.team[mega] = self.team.pop(pokemon, None)
        self.team[mega].species = mega

    def usedZmove(self):
        self.canZmove = False

    def usedTera(self):
        self.canTera = False

class Battle:
    def __init__(self, name):
        self.rqid = 1
        self.name = name
        self.generation = 8 # Default generation
        self.myActiveData = {}
        self.me = Player()
        self.other = Player()
        self.field = {}
        self.spectating = False
        self.ladderGame = False
        self.allowDynamax = True # Default dynamax allowed
        self.allowTera = True # Default tera is allowed
        self.hackmons = True # Assume hackmons until told otherwise

    def setMe(self, me, pId):
        self.me.name = me
        self.me.id = pId

    def setOther(self, other, pId):
        self.other.name = other
        self.other.id = pId

    def isLadderMatch(self):
        self.ladderGame = True

    def notHackmons(self):
        self.hackmons = False

    def cantDynamax(self):
        self.allowDynamax = False
        self.me.canDynamax = False
        self.other.canDynamax = False

    def cantTera(self):
        self.teraAllowed = False
        self.me.canTera = False
        self.other.canTera = False

    def setFieldCond(self, cond):
        # TODO: do this
        pass

