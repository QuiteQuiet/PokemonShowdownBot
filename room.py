# Each PS room joined creates an object here.
# Objects control settings on a room-per-room basis, meaning every room can
# be treated differently.
import json
from plugins.tournaments import Tournament
import robot as r

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
    reply = r.ReplyObject()
    if not user.hasRank('#'): return reply.response('You do not have permission to change this. (Requires #)')
    msg = bot.removeSpaces(msg)
    things = msg.split(',')
    if not len(things) == 2: return reply.response('Too few/many parameters. Command is ~allowgames [room],True/False')
    if things[0] not in bot.rooms: return reply.response('Cannot allow chatgames without being in the room')
    if things[1] in ['true','yes','y','True']:
        if bot.getRoom(things[0]).allowGames: return reply.response('Chatgames are already allowed in {room}'.format(room = things[0]))
        bot.getRoom(things[0]).allowGames = True
        return reply.response('Chatgames are now allowed in {room}'.format(room = things[0]))

    elif things[1] in ['false', 'no', 'n',' False']:
        bot.getRoom(things[0]).allowGames = False
        return reply.response('Chatgames are no longer allowed in {room}'.format(room = things[0]))
    return reply.response('{param} is not a supported parameter'.format(param = things[1]))

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