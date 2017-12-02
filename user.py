import re


class User:
    """ Container class for basic user information collected from rooms.

    This information consists of user.id, user.rank, and user.name. user.id is
    a format-removed id of user.name with only a-z lowercase and 0-9 present.

    user.rank contain the auth level of the user, as a single character string of
    either ' ', +, ☆, %, @, *, &, #, or ~. Note that ☆ is only relevant for
    battle rooms.

    To compare groups against each other User.Groups have the information required
    when used like: User.Groups[user.rank] for a numeric value.

    Lastly, user.name is the unaltered name as seen in the chat rooms, and can be
    used for things like replying. Comparison between users should make use of
    user.id since users can change their frequently.

    Attributes:
        Groups: map string to int, ranks precedence of user ranks by symbols.
        name: string, username.
        id: string, simplified unique username.
        rank: string, user rank.
        owner: Bool, is this you.
    """
    Groups = {'‽': -1, '!': -1, ' ': 0, '+': 1, '☆': 1, '%': 2, '@': 3, '*': 3.1, '&': 4, '#': 5, '~': 6}

    @staticmethod
    def compareRanks(rank1, rank2):
        try:
            return User.Groups[rank1] >= User.Groups[rank2]
        except KeyError:
            if rank1 not in User.Groups:
                print('{rank} is not a supported usergroup'.format(rank = rank1))
            if rank2 not in User.Groups:
                print('{rank} is not a supported usergroup'.format(rank = rank2))
            return False

    def __init__(self, name, rank = ' ', owner = False):
        self.name = name
        self.id = re.sub(r'[^a-zA-Z0-9]', '', name).lower()
        self.rank = rank
        self.owner = owner

    def hasRank(self, rank):
        return self.owner or User.compareRanks(self.rank, rank)
    def isOwner(self):
        return self.owner