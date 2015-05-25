# Each PS room joined creates an object here.
# Objects control settings on a room-per-room basis, meaning every room can
# be treated differently.

class Room:
    def __init__(self, room, data):
        if not data:
            # This is a hack to support both strings and dicts as input to the class
            data = {'moderate':False, 'allow games':False}
        self.users = []
        self.loading = True
        self.title = room
        self.moderate = data['moderate']
        self.allowGames = data['allow games']
    def doneLoading(self):
        self.loading = False

    def addUserlist(self, users):
        self.users = [u for u in users.split(',') if users.index(u) > 0]
    def addUser(self, user):
        if user not in self.users:
            self.users.append(user)
    def removeUser(self, user):
        if user in self.users:
            self.users.remove(user)
    def renamedUser(self, old, new):
        self.removeUser(old)
        self.addUser(new)

    def allowGames(self, yesNo):
    	self.allowGames = yesNo
