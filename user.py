import re
class User:
    Groups = {' ':0,'+':1,'★':1,'%':2,'@':3,'&':4,'#':5,'~':6}
    def __init__(self, name, rank, owner = False):
        self.name = name
        self.id = re.sub(r'[^a-zA-z0-9]', '', name).lower()
        self.rank = rank
        self.owner = owner

    def hasRank(self, rank):
        return self.owner or User.Groups[self.rank] >= User.Groups[rank]
    def isOwner(self):
        return self.owner