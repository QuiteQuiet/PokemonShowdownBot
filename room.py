# Each PS room joined creates an object here.
# Objects control settings on a room-per-room basis, meaning every room can
# be treated differently.
from plugins.tournaments import Tournament

class Room:
    def __init__(self, room, data):
        if not data:
            # This is a hack to support both strings and dicts as input to the class
            data = {'moderate':False, 'allow games':False}
        self.users = {}
        self.loading = True
        self.title = room
        self.moderate = data['moderate']
        self.allowGames = data['allow games']
        self.tour = None
        self.game = None
    def doneLoading(self):
        self.loading = False

    def addUserlist(self, users):
        self.users = {u[1:]:u[0] for u in users.split(',')}
    def addUser(self, user, auth):
        if user not in self.users:
            self.users[user] = auth
    def removeUser(self, user):
        if user in self.users:
            self.users.pop(user)
    def renamedUser(self, old, new):
        self.removeUser(old)
        self.addUser(new[1:], new[0])

    def createTour(self, ws):
        self.tour = Tournament(ws, self.title)
    def endTour(self):
        self.tour = None
