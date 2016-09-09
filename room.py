# Each PS room joined creates an object here.
# Objects control settings on a room-per-room basis, meaning every room can
# be treated differently.
import json
from collections import deque
from plugins.tournaments import Tournament
import robot as r

class Room:
    def __init__(self, room, data = None):
        if not data: data = {'moderate':False, 'allow games':False, 'tourwhitelist':[]}
        self.users = {}
        self.loading = True
        self.title = room
        self.rank = ' '
        self.moderate = data['moderate']
        self.allowGames = data['allow games']
        self.tour = None
        self.activity = None
        self.tourwhitelist = data['tourwhitelist']
        self.chatlog = deque({'': -1}, 20)
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

    def logChat(self, user, message):
        self.chatlog.append({user.id: len(message)})

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
    reply = r.ReplyObject()
    if not user.hasRank('#'): return reply.response('You do not have permission to change this. (Requires #)')
    if room.title == 'pm': return reply.response("You can't use this command in a pm.")
    msg = bot.removeSpaces(msg)
    if msg in ['true','yes','y','True']:
        if room.allowGames: return reply.response('Chatgames are already allowed in this room.')
        room.allowGames = True
        return reply.response('Chatgames are now allowed in this room.')

    elif msg in ['false', 'no', 'n',' False']:
        room.allowGames = False
        return reply.response('Chatgames are no longer allowed in this room.')
    return reply.response('{param} is not a supported parameter'.format(param = msg))

def tour(bot, cmd, room, msg, user):
    reply = r.ReplyObject('', True, True, True)
    if room.title == 'pm': return reply.response("You can't use this command in a pm.")
    if not room.isWhitelisted(user): return reply.response('You are not allowed to use this command. (Requires whitelisting by a Room Owner)')
    if not bot.canStartTour(room): return reply.response("I don't have the rank required to start a tour :(")
    return reply.response('/tour {rest}\n/modnote From {user}'.format(rest = msg, user = user.name))
def tourwl(bot, cmd, room, msg, user):
    reply = r.ReplyObject('', True)
    if not user.hasRank('#'): return reply.response('You do not have permission to change this. (Requires #)')
    target = bot.toId(msg)
    if not room.addToWhitelist(target): return reply.response('This user is already whitelisted in that room.')
    bot.saveDetails()
    return reply.response('{name} added to the whitelist in this room.'.format(name = msg))
def untourwl(bot, cmd, room, msg, user):
    reply = r.ReplyObject('', True)
    if not user.hasRank('#'): return reply.response('You do not have permission to change this. (Requires #)')
    target = bot.toId(msg)
    if not room.delFromWhitelist(target): return reply.response('This user is not whitelisted in that room.')
    bot.saveDetails()
    return reply.response('{name} removed from the whitelist in this room.'.format(name = msg))

RoomCommands = {
    'allowgames'    : allowgames,
    'tour'          : tour,
    'tourwl'        : tourwl,
    'untourwl'      : untourwl
}