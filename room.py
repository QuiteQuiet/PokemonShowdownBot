# Each PS room joined creates an object here.
# Objects control settings on a room-per-room basis, meaning every room can
# be treated differently.
import json
from plugins.tournaments import Tournament

class Room:
    def __init__(self, room, data = None):
        if not data:
            # This is to support both strings and dicts as input
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

    def addUser(self, user):
        if user.id not in self.users:
            self.users[user.id] = user
    def removeUser(self, userid):
        if userid in self.users:
            return self.users.pop(userid)
    def renamedUser(self, old, new):
        self.removeUser(old)
        self.addUser(new)
    def getUser(self, name):
        if name in self.users:
            return self.users[name]

    def isWhitelisted(self, user):
        return user.hasRank('@') or user.id in self.tourwhitelist
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
    def getTourWinner(self, msg):
        things = json.loads(msg)
        return things['results'][0], things['format']
    def endTour(self):
        self.tour = None

# Commands
def allowgames(bot, cmd, room, msg, user):
    if not user.hasRank('#'): return 'You do not have permission to change this. (Requires #)', False
    msg = bot.removeSpaces(msg)
    things = msg.split(',')
    if not len(things) == 2: return 'Too few/many parameters. Command is ~allowgames [room],True/False', False
    if things[0] not in bot.rooms: return 'Cannot allow chatgames without being in the room', True
    if things[1] in ['true','yes','y','True']:
        if bot.getRoom(things[0]).allowGames: return 'Chatgames are already allowed in {room}'.format(room = things[0]), True
        bot.getRoom(things[0]).allowGames = True
        return 'Chatgames are now allowed in {room}'.format(room = things[0]), True

    elif things[1] in ['false', 'no', 'n',' False']:
        bot.getRoom(things[0]).allowGames = False
        return 'Chatgames are no longer allowed in {room}'.format(room = things[0]), True
    return '{param} is not a supported parameter'.format(param = things[1]), True

def tour(bot, cmd, room, msg, user):
    if room.title == 'pm': return "You can't use this command in a pm.", False
    if not room.isWhitelisted(user): return 'You are not allowed to use this command. (Requires whitelisting by a Room Owner)', True
    if not bot.canStartTour(room): return "I don't have the rank required to start a tour :(", True
    return '/tour {rest}\n/modnote From {user}'.format(rest = msg, user = user.name), True
def tourwl(bot, cmd, room, msg, user):
    if not user.hasRank('#'): return 'You do not have permission to change this. (Requires #)', False
    target = bot.toId(msg)
    if not room.addToWhitelist(target): return 'This user is already whitelisted in that room.', False
    bot.saveDetails()
    return '{name} added to the whitelist in this room.'.format(name = msg), True
def untourwl(bot, cmd, room, msg, user):
    if not user.hasRank('#'): return 'You do not have permission to change this. (Requires #)', False
    target = bot.toId(msg)
    if not room.delFromWhitelist(target): return 'This user is not whitelisted in that room.', False
    bot.saveDetails()
    return '{name} removed from the whitelist in this room.'.format(name = msg), True

RoomCommands = {
    'allowgames'    : allowgames,
    'tour'          : tour,
    'tourwl'        : tourwl,
    'untourwl'      : untourwl
}