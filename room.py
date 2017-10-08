# Each PS room joined creates an object here.
# Objects control settings on a room-per-room basis, meaning every room can
# be treated differently.
import json
from collections import deque
from plugins.tournaments import Tournament
from invoker import ReplyObject, Command
from user import User
from plugins.moderation import ModerationHandler

class Room:
    def __init__(self, room, data = None):
        if not data: data = {
            'moderate': {
                'room': room,
                'anything': False,
                'spam': False,
                'banword': False,
                'stretching': False,
                'caps': False,
                'groupchats': False,
                'urls': False
            },
            'allow games':False,
            'tourwhitelist':[]}
        self.users = {}
        self.loading = True
        self.title = room
        self.isPM = room.lower() == 'pm'
        self.rank = ' '
        self.moderation = ModerationHandler(data['moderate'])
        self.allowGames = data['allow games']
        self.tour = None
        self.activity = None
        self.tourwhitelist = data['tourwhitelist']
        self.chatlog = deque({'user': None, 'message': '', 'timestamp': ''}, 20)
        self.moderation.assignRoom(self)

    def doneLoading(self):
        self.loading = False

    def addUser(self, user):
        if self.moderation.isBannedFromRoom(user):
            return
        if user.id not in self.users:
            self.users[user.id] = user
        return True
    def removeUser(self, userid):
        if userid in self.users:
            return self.users.pop(userid)
    def renamedUser(self, old, new):
        self.removeUser(old)
        self.addUser(new)
    def getUser(self, name):
        if name in self.users:
            return self.users[name]

    def botHasBanPermission(self):
        return User.compareRanks(self.rank, '@')

    def logChat(self, user, message, time):
        self.chatlog.append({'user': user, 'message': message, 'timestamp': time})

    def isWhitelisted(self, user):
        return user.hasRank('%') or user.id in self.tourwhitelist
    def addToWhitelist(self, user):
        if user in self.tourwhitelist: return False
        self.tourwhitelist.append(user)
        return True
    def delFromWhitelist(self, target):
        if target not in self.tourwhitelist: return False
        self.tourwhitelist.remove(target)
        return True
    def createTour(self, ws, form, battleHandler):
        self.tour = Tournament(ws, self, form, battleHandler)
    def getTourWinner(self, msg):
        things = json.loads(msg)
        winner = things['results'][0]
        if self.tour: self.tour.logWin(winner)
        return winner, things['format']
    def endTour(self):
        self.tour = None

# Commands
def leaveroom(bot, cmd, room, params, user):
    reply = ReplyObject()
    params = bot.removeSpaces(params)
    if not params: params = room.title
    if bot.leaveRoom(params):
        return reply.response('Leaving room {r} succeeded'.format(r = params))
    return reply.response('Could not leave room: {r}'.format(r = params))

def allowgames(bot, cmd, room, params, user):
    reply = ReplyObject(True)
    if not user.hasRank('#'): return reply.response('You do not have permission to change this. (Requires #)')
    if room.isPM: return reply.response("You can't use this command in a pm.")
    params = bot.removeSpaces(params)
    if params in ['true','yes','y','True']:
        if room.allowGames: return reply.response('Chatgames are already allowed in this room.')
        room.allowGames = True
        return reply.response('Chatgames are now allowed in this room.')

    elif params in ['false', 'no', 'n',' False']:
        room.allowGames = False
        return reply.response('Chatgames are no longer allowed in this room.')
    return reply.response('{param} is not a supported parameter'.format(param = params))

def tour(bot, cmd, room, params, user):
    reply = ReplyObject('', True, True, True)
    if room.isPM: return reply.response("You can't use this command in a pm.")
    if not room.isWhitelisted(user): return reply.response('You are not allowed to use this command. (Requires whitelisting by a Room Owner)')
    if not bot.canStartTour(room): return reply.response("I don't have the rank required to start a tour :(")
    return reply.response('/tour {rest}\n/modnote From {user}'.format(rest = params, user = user.name))
def tourwl(bot, cmd, room, params, user):
    reply = ReplyObject('', True)
    if not user.hasRank('#'): return reply.response('You do not have permission to change this. (Requires #)')
    target = bot.toId(params)
    if not room.addToWhitelist(target): return reply.response('This user is already whitelisted in that room.')
    bot.saveDetails()
    return reply.response('{name} added to the whitelist in this room.'.format(name = params))
def untourwl(bot, cmd, room, params, user):
    reply = ReplyObject('', True)
    if not user.hasRank('#'): return reply.response('You do not have permission to change this. (Requires #)')
    target = bot.toId(params)
    if not room.delFromWhitelist(target): return reply.response('This user is not whitelisted in that room.')
    bot.saveDetails()
    return reply.response('{name} removed from the whitelist in this room.'.format(name = params))

commands = [
    Command(['leave'], leaveroom),
    Command(['allowgames'], allowgames),
    Command(['tour', '!tour'], tour),
    Command(['tourwhitelist', 'tourwl'], tourwl),
    Command(['untourwhitelist', 'untourwl'], untourwl)
]
