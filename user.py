import re
class User:
    Groups = {' ':0,'+':1,'★':1,'%':2,'@':3,'*':3.1,'&':4,'#':5,'~':6}
    @staticmethod
    def compareRanks(rank1, rank2):
        try:
            return User.Groups[rank1] >= User.Groups[rank2]
        except:
            if not rank1 in User.Groups:
                print('{rank} is not a supported usergroup'.format(rank = rank1))
            if not rank2 in User.Groups:
                print('{rank} is not a supported usergroup'.format(rank = rank2))
            return False

    def __init__(self, name, rank, owner = False):
        self.name = name
        self.id = re.sub(r'[^a-zA-z0-9]', '', name).lower()
        self.rank = rank
        self.owner = owner

    def hasRank(self, rank):
        return self.owner or User.compareRanks(self.rank, rank)
    def isOwner(self):
        return self.owner