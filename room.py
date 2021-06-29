# Each PS room joined creates an object here.
# Objects control settings on a room-per-room basis, meaning every room can
# be treated differently.
import json
import time
import sys
import requests
from datetime import timedelta, datetime
from collections import deque

from invoker import ReplyObject, Command
from user import User
from plugins.tournaments import Tournament
from plugins.moderation import ModerationHandler
from plugins.eventscheduler import EventScheduler
from plugins.activityTracker import ActivityTracker
from data.tiers import oldgenNUBanlists

class Room:
    """ Contains all important information for a pokemon showdown room.

    The only variable of note is the activity object. This variable does not
    follow a strict typing as it can allow for several class types. What should
    be noted is that there can only be 1 instance of activity per room, so
    having a situation with a Workshop and RoomGame running at the same time
    is impossible.

    Attributes:
        users: map, maps user ids (str) to user objects.
        loading: Bool, if this room is still loading information.
        title: string, name of the room.
        rank: string, the rank of this bot in this room.
        isPM: Bool, if this room is considered a private message.
        moderation: ModerationHandler, handler object for moderating user content.
        allowGames: Bool, if this bot will allow games in this room.
        tour: Bool, if this bot will allow tours in this room.
        activity: GenericGame, object which implements the standard behaviour for a Game,
                  all activities do not strictly have the same type.
        tourwhitelist: list of str, users who are not moderators but who have
                       permission to start a tour.
    """
    def __init__(self, room):

        self.users = {}
        self.loading = True
        self.joinTime = int(time.time())
        self.title = room
        self.formatedName = ''
        self.isPM = room.lower() == 'pm'
        self.rank = ' '
        self.allowGames = False
        self.tour = None
        self.activity = None
        self.lastCommand = ''
        self.pastTours = deque([], maxlen=10)
        self.tourwhitelist = []
        self.officialFormats = set()
        self.formatWatchlist = set()
        self.showrankings = False
        self.chatlog = deque({'user': None, 'message': '', 'timestamp': ''}, 20)
        moderationDefaults = {
            'anything': False,
            'spam': False,
            'banword': False,
            'stretching': False,
            'caps': False,
            'groupchats': False,
            'urls': False
        }
        self.moderation = ModerationHandler(moderationDefaults, self)
        self.scheduler = EventScheduler(self)
        self.activityTracker = ActivityTracker(25)

    def doneLoading(self, joindata=None):
        self.loading = False
        # Update with autojoin data after room is loaded if it exists
        if self.title in joindata:
            details = joindata[self.title]
            self.allowGames = details['allow games']
            self.tourwhitelist = details['tourwhitelist']
            self.officialFormats = set(details['officialformats'])
            self.formatWatchlist = set(details['formatwatchlist'])
            self.showrankings = details['showrankings']
            self.moderation = ModerationHandler(details['moderate'], self)

    def isHistory(self, timestamp, message):
        if not self.loading: return False
        if int(timestamp) > self.joinTime:
            self.loading = False
        return self.loading

    def addUser(self, user):
        if self.moderation.isBannedFromRoom(user): return
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
        self.activityTracker.countActivity(self, user)

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
        self.tour = Tournament(ws,
                               self,
                               form,
                               battleHandler,
                               form in self.officialFormats)
    def getTourWinner(self, msg):
        things = json.loads(msg)
        winner = things['results'][0]
        return winner, things['format']
    def endTour(self):
        self.pastTours.append(self.tour)
        if self.showrankings:
            data = Tournament.getTournamentData(self.title, self.tour.format, official=self.tour.official)
            html = Tournament.buildRankingsTable(data, self.tour.format, 25)
        else:
            html = None
        self.tour = None
        return html

# Commands
def leaveroom(bot, cmd, params, user, room):
    """ Independent command for making this bot leave a room.

    Args:
        bot: PokemonShowdownBot, the instance of PokemonShowdownBot that called this function.
        cmd: string, the command that was send.
        room: Room, the room object that the command was sent from.
        params: string, optional parameter like room name, if left empty
                function attempts to leave room where this command was invoked.
        user: User, the user object of the user who sent the command.
    Returns:
        ReplyObject.
    """
    reply = ReplyObject()
    params = bot.removeSpaces(params)
    if not params: params = room.title
    if bot.leaveRoom(params):
        return reply.response('Leaving room {r} succeeded'.format(r = params))
    return reply.response('Could not leave room: {r}'.format(r = params))

def allowgames(bot, cmd, params, user, room):
    """ Independent command for changing permissions for games in this room.

    Reserved for room owners. They can decide to allow games/activities in their room.

    Args:
        bot: PokemonShowdownBot, the instance of PokemonShowdownBot that called this function.
        cmd: string, the command that was send.
        room: Room, the room object that the command was sent from.
        params: string, required parameter indicating the status of games in this room.
        user: User, the user object of the user who sent the command.
    Returns:
        ReplyObject.
    """
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

def tour(bot, cmd, params, user, room):
    """ Independent command for initiating tours in this room.

    This is only possible for rooms where this bot has at least '@' rank. Intended
    trusted users who do not have the required room rank.

    Args:
        bot: PokemonShowdownBot, the instance of PokemonShowdownBot that called this function.
        cmd: string, the command that was send.
        room: Room, the room object that the command was sent from.
        params: string, parameter(s) you'd give a normal /tour command on showdown.
        user: User, the user object of the user who sent the command.
    Returns:
        ReplyObject.
    """
    reply = ReplyObject('', True, True, True)
    if room.isPM: return reply.response("You can't use this command in a pm.")
    if not room.isWhitelisted(user): return reply.response('You are not allowed to use this command. (Requires whitelisting by a Room Owner)')
    if params in {'gscnu', 'advnu'}:
        gen, name = ('gen3ou', 'ADV NU') if params == 'advnu' else ('gen2ou', 'GSC NU')
        params = 'new {gen}, elimination\n/tour rules {bans}\n/tour name {name}'.format(gen = gen, bans = oldgenNUBanlists[params], name = name)
    return reply.response('/tour {rest}\n/modnote From {user}'.format(rest = params, user = user.name))

def gettourwl(bot, cmd, params, user, room):
    reply = ReplyObject('', True, True)
    targetRoom = bot.getRoom(params)
    if not targetRoom: targetRoom = room
    user = targetRoom.getUser(user.id)
    if not user.hasRank('@'): return reply.response('You don\'t have permission to view the tour whitelist for {}'.format(targetRoom.title))
    if not targetRoom.tourwhitelist: return reply.response('No whitelist for room {}'.format(targetRoom.title))
    return reply.response('Whitelisted users in {room}: {users}'.format(room = targetRoom.title, users = ', '.join(targetRoom.tourwhitelist)))


def tourwl(bot, cmd, params, user, room):
    """ Independent command for a user to tours whitelist.

    Reserved for room owners.

    Args:
        bot: PokemonShowdownBot, the instance of PokemonShowdownBot that called this function.
        cmd: string, the command that was send.
        room: Room, the room object that the command was sent from.
        params: string, the name of the user.
        user: User, the user object of the user who sent the command.
    Returns:
        ReplyObject.
    """
    reply = ReplyObject('', True)
    targetRoom = room
    params = params.replace(', ', ',').split(',')
    if len(params) > 1:
        targetRoom = bot.getRoom(params[0])
        user = targetRoom.getUser(user.id)
        params.pop(0)
    if not user.hasRank('#'): return reply.response('You do not have permission to change this. (Requires #)')
    target = bot.toId(params[0])
    if not room.addToWhitelist(target): return reply.response('This user is already whitelisted in that room.')
    bot.saveDetails()
    return reply.response('{name} added to the whitelist in this room.'.format(name = params))

def untourwl(bot, cmd, params, user, room):
    """ Independent command for removing a user from the tours whitelist.

    Reserved for room owners.

    Args:
        bot: PokemonShowdownBot, the instance of PokemonShowdownBot that called this function.
        cmd: string, the command that was send.
        room: Room, the room object that the command was sent from.
        params: string, the name of the user.
        user: User, the user object of the user who sent the command.
    Returns:
        ReplyObject.
    """
    reply = ReplyObject('', True)
    targetRoom = room
    params = params.replace(', ', ',').split(',')
    if len(params) > 1:
        targetRoom = bot.getRoom(params[0])
        user = targetRoom.getUser(user.id)
        params.pop(0)
    if not user.hasRank('#'): return reply.response('You do not have permission to change this. (Requires #)')
    target = bot.toId(params[0])
    if not room.delFromWhitelist(target): return reply.response('This user is not whitelisted in that room.')
    bot.saveDetails()
    return reply.response('{name} removed from the whitelist in this room.'.format(name = params))

def getactivity(bot, cmd, params, user, room):
    """ Independent command for getting the activity of user(s) in a room.

    Args:
        bot: PokemonShowdownBot, the instance of PokemonShowdownBot that called this function.
        cmd: string, the command that was send.
        room: Room, the room object that the command was sent from.
        params: string, the name of the user.
        user: User, the user object of the user who sent the command.
    Returns:
        ReplyObject.
    """
    reply = ReplyObject('', escape = True, pmreply = True, ignoreml = True)
    params = params.replace(', ', ',').split(',')
    targetRoom = room
    if room.isPM or bot.getRoom(params[0]):
        targetRoom = bot.getRoom(params.pop(0))
    user = '' if len(params) == 0 or params[0].isdigit() or params[0] == 'all' else params.pop(0)
    user = bot.toId(user)
    period = 30 if len(params) == 0 else sys.maxsize if params[0] == 'all' else int(params.pop(0))

    activityData = targetRoom.activityTracker.getActivityForPeriod(period, targetRoom, user)
    if len(activityData) == 0:
        return reply.response('No activity data found for room {room}'.format(room = targetRoom.title))
    lines = ['Activity in {room} for {user} the last {period} days:'.format(room = targetRoom.title, period = period, user = '{} in'.format(user))]
    for entry, count in activityData:
        lines.append('  {datename}: {count} lines'.format(datename = entry, count = count))
    if bot.canBroadcast(room):
        return reply.response('!code ' + '\n'.join(lines))
    else:
        r = requests.post('https://pastebin.com/api/api_post.php',
            data = {
                'api_dev_key': bot.apikeys['pastebin'],
                'api_option':'paste',
                'api_paste_code': '\n'.join(lines),
                'api_paste_private': 0,
                'api_paste_expire_date':'N'
                })
        if 'Bad API request' in r.text:
            return reply.response('Something went wrong ({error})'.format(error = r.text))
        return reply.response(r.text)

def addofficial(bot, cmd, tier, user, room):
    if not user.hasRank('@'): return ReplyObject('Permission denied. (Requires @)', True)
    room.officialFormats.add(tier)
    bot.saveDetails()
    return ReplyObject('Added {} as official format'.format(tier), True)

def trackformat(bot, cmd, tier, user, room):
    if not user.hasRank('#'): return ReplyObject('Permission denied. (Requires #)', True)
    room.formatWatchlist.add(tier)
    bot.saveDetails()
    return ReplyObject('Added {} as official format'.format(tier), True)

def togglerankings(bot, cmd, params, user, room):
    if not user.hasRank('@'): return ReplyObject('Permission denied. (Require @)', True)

    shouldPrint = cmd == 'showrankings'
    try:
        bot.getRoom(params).showrankings = shouldPrint
        configured = params
    except AttributeError:
        room.showrankings = shouldPrint
        configured = room.title
    return ReplyObject('Official leaderboards for {room} will {toggle}be printed after tours.'.format(
                        room=configured, toggle=('now ' if shouldPrint else 'no longer ')), True)

def errorHandler(robot, room, *error):
    # This should be good enough, we're not in that many rooms
    for room in robot.rooms.values():
        if not room.lastCommand: continue
        timeDiff = datetime.now() - room.lastCommand[1]
        if room.lastCommand[0] == 'tour' and timeDiff < timedelta(seconds=5):
            robot.say(room.title, '|'.join(error))

def setRoomTitle(robot, room, title):
    room.formatedName = title

# Exports
handlers = {
    'error': errorHandler,
    'title': setRoomTitle,
}

commands = [
    Command(['leave'], leaveroom),
    Command(['allowgames'], allowgames),
    Command(['tour', '!tour'], tour),
    Command(['tourwhitelist', 'tourwl'], tourwl),
    Command(['untourwhitelist', 'untourwl'], untourwl),
    Command(['gettourwhitelist', 'gettourwl'], gettourwl),
    Command(['getactivity'], getactivity),
    Command(['addofficial'], addofficial),
    Command(['trackformat'], trackformat),
    Command(['showrankings', 'hiderankings'], togglerankings),
]
