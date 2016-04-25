# Each PS room joined creates an object here.
# Objects control settings on a room-per-room basis, meaning every room can
# be treated differently.
import re
from plugins.tournaments import Tournament

class Room:
    def __init__(self, room, data = None):
        if not data:
            # This is a hack to support both strings and dicts as input to the class
            data = {'moderate':False, 'allow games':False, 'tourwhitelist':[]}
        self.users = {}
        self.loading = True
        self.title = room
        self.rank = ' '
        self.moderate = data['moderate']
        self.allowGames = data['allow games']
        self.tour = None
        self.game = None
        self.tourwhitelist = data['tourwhitelist']
    def doneLoading(self):
        self.loading = False

    def makeUserlist(self, userlist):
        # User 0 is always yourself but adding yourself to the userlist
        # is handled elsewhere
        for user in userlist.split(',')[1:]:
            self.addUser(user[1:], user[0])

    def addUser(self, username, auth):
        userid = self.toId(username)
        if userid not in self.users:
            self.users[userid] = {'rank': auth, 'username': username}
    def removeUser(self, user):
        if user in self.users:
            self.users.pop(user)
    def renamedUser(self, old, new):
        self.removeUser(old)
        self.addUser(new[1:], new[0])

    def toId(self, thing):
        return re.sub(r'[^a-zA-z0-9,]', '', thing).lower()

    def isWhitelisted(self, user):
        return user in self.tourwhitelist
    def addToWhitelist(self, user):
        if user in self.tourwhitelist: return False
        self.tourwhitelist.append(user)
        return True
    def delFromWhitelist(self, target):
        if target not in self.tourwhitelist: return False
        self.tourwhitelist.remove(target)
        return True
    def createTour(self, ws, form):
        self.tour = Tournament(ws, self.title, form)
    def endTour(self):
        self.tour = None
