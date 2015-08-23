class Workshop:
    def __init__(self, host):
        self.host = host
        self.team = []

    def addPokemon(self, poke):
        if len(self.team) >= 6:
            return 'team is full'
        self.team.append(poke)
        return '{mon} added'.format(mon = poke)
    def removePokemon(self, poke):
        if poke in self.team:
            self.team.remove(poke)
            return '{mon} removed'.format(mon = poke)
        return '{mon} is not in the team'.format(mon = poke)
    def getTeam(self):
        if len(self.team) <= 0:
            return 'team is empty'
        return ' / '.join(self.team)
    def clearTeam(self):
        self.team = []
        return 'team cleared'
