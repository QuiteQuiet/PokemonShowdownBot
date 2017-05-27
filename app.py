# This is the entry point for the Pokemon Showdown Bot, and contain most of the
# permission checks for chat returns.
#
# It's derived from the base class PokemonShowdownBot, and as such hide a lot of
# it's core functions by simply calling functions from the base class.
# For any function called here not defined in this file, look in robot.py.
#
# Changes to this file should be made with caution, as much of the extended functions
# depend on this being structured in a specific way.
#
# Extended notes:
# user:
#     user objects are objects containing some information about the user who said anything.
#     This information consists of user.id, user.rank, and user.name. user.id is
#     a format-removed id of the speaker with only a-z lowercase and 0-9 present.
#
#     user.rank contain the auth level of the user, as a single character string of
#     either ' ', +, %, @, *, &, #, or ~. To compare groups against each other self.Groups have
#     the information required when used like: User.Groups[user.rank] for a numeric value.
#
#     Lastly, user.name is the unaltered name as seen in the chatrooms, and can be used
#     for things like replying, but shouldn't be used for comparisions.

import json
import time

from robot import PokemonShowdownBot, Room, User
from commands import Command
from plugins import moderation
from plugins.messages import MessageDatabase
from plugins.workshop import Workshop

class PSBot(PokemonShowdownBot):
    def __init__(self):
        self.do = Command
        self.usernotes = MessageDatabase()
        PokemonShowdownBot.__init__(self,
                                    'ws://sim.psim.us:8000/showdown/websocket',
                                    self.splitMessage)

    def splitMessage(self, ws, message):
        if not message: return
        if '\n' not in message: self.parseMessage(message, '')

        room = ''
        msg = message.split('\n')
        if msg[0].startswith('>'):
            room = msg[0][1:]
        msg.pop(0)

        if room.startswith('battle-'):
            if room not in self.rooms:
                # Battle rooms don't need the same interface as chatrooms
                self.rooms[room] = True
            if 'deinit' in msg[0]:
                self.rooms.pop(room)
            # Go to battle handler instead of regular rooms
            # (I don't allow commands in battle rooms anyway)
            try:
                for m in msg:
                    self.bh.parse(room, m)
            except AttributeError as e:
                print('AttributeError: {}'.format(e))
                print('MESSAGE THAT CAUSED IT:\n{}'.format(msg))
            return

        for m in msg:
            self.parseMessage(m, room)

    def testRoombaned(self, room, user):
        if moderation.shouldBan(self, user, room):
            self.takeAction(room.title, user, 'roomban', "You are blacklisted from this room, so please don't come here.")
            return True
        return False

    def handleJoin(self, room, message):
        if self.userIsSelf(message[1:]):
            room.rank = message[0]
            room.doneLoading()
        user = User(message, message[0], self.isOwner(message))
        if self.testRoombaned(room, user):
            return
        room.addUser(user)
        # If the user have a message waiting, tell them that in a pm
        if self.usernotes.shouldNotifyMessage(user.id):
            self.sendPm(user.id, self.usernotes.pendingMessages(user.id))

    def parseMessage(self, msg, roomName):
        if not msg.startswith('|'): return
        message = self.escapeMessage(msg).split('|')
        room = Room('Empty') if not roomName else self.getRoom(roomName)

        # Logging in
        if message[1] == 'challstr':
            print('{name}: Attempting to login...'.format(name = self.name))
            self.login(message[3], message[2])

        elif message[1] == 'updateuser':
            self.updateUser(message[2], message[3])

        # Challenges
        elif 'updatechallenges' in message[1]:
            challs = json.loads(message[2])
            if challs['challengesFrom']:
                opp = [name for name, form in challs['challengesFrom'].items()][0]
                format = challs['challengesFrom'][opp]
                if format in self.bh.supportedFormats:
                    team = self.bh.getRandomTeam(format)
                    self.send('|/utm {}'.format(team))
                    self.send('|/accept {name}'.format(name = opp))
                else:
                    self.sendPm(opp, "Sorry, I can't accept challenges in that format :(")
        elif 'updatesearch' in message[1]:
            # This gets sent before `updatechallenges` does when recieving a battle, but it's
            # not useful for anything, so just return straight away
            return

        # This is a safeguard for l and n in case that a moderation action happen
        elif 'unlink' == message[1] or 'uhtml' in message[1] or 'html' == message[1]:
            return

        # Room was left in some way other than through ~leave
        elif 'deinit' == message[1]:
            self.rooms.pop(roomName)

        # As long as the room have a roomintro (which even groupchats do now)
        # Roomintros are also the last thing that is sent when joining a room
        # so when this show up, assume the room is loaded
        elif 'raw' == message[1]:
            if message[2].startswith('<div class="infobox infobox-roomintro"><div class="infobox-limited">'):
                room.doneLoading()

        # Joined new room
        elif 'users' in message[1]:
            for user in message[2].split(',')[1:]:
                room.addUser(User(user[1:], user[0], self.isOwner(user)))
            # If PS doesn't tell us we joined, this still give us our room rank
            room.rank = message[2][message[2].index(self.name) - 1]

        elif 'j' in message[1].lower():
            self.handleJoin(room, message[2])

        elif 'l' == message[1].lower() or 'leave' == message[1].lower():
            if self.userIsSelf(message[2][1:]):
                # This is just a failsafe in case the bot is forcibly removed from a room.
                # Any other memory release required is handeled by the room destruction
                if roomName in self.rooms:
                    self.rooms.pop(roomName)
                return
            userid = self.toId(message[2])
            room.removeUser(userid)
        elif 'n' in message[1].lower() and len(message[1]) < 3:
            # Keep track of your own rank
            # When demoting / promoting a user the server sends a |N| message to update the userlist
            if self.userIsSelf(message[2][1:]):
                room.rank = message[2][0]
            newUser = User(message[2][1:], message[2][0], self.isOwner(message[2]))
            room.renamedUser(self.toId(message[3]), newUser)
            self.testRoombaned(room, newUser)


        # Chat messages
        elif 'c' in message[1].lower():
            if room.loading: return
            user = room.getUser(self.toId(message[3]))
            if not user: return
            if self.userIsSelf(user.id): return

            room.logChat(user, message[2])
            if room.moderate and self.canPunish(room):
                anything = moderation.shouldAct(message[4], user, room, message[2])
                if anything:
                    action, reason = moderation.getAction(self, room, user, anything, message[2])
                    self.takeAction(room.title, user, action, reason)

            message[4] = '|'.join(message[4:])
            if message[4].startswith(self.commandchar) and message[4][1:] and message[4][1].isalpha():
                command = self.extractCommand(message[4])
                self.log('Command', message[4], user.id)

                res = self.do(self, command, room, message[4][len(command) + 1:].lstrip(), user)
                if not res.text or res.text == 'NoAnswer': return

                if self.evalPermission(user) or res.ignoreBroadcastPermission:
                    if not res.ignoreEscaping:
                        res.text = self.escapeText(res.text)
                    self.reply(room.title, user, res.text, res.samePlace)

                elif res.canPmReply:
                    self.sendPm(user.id, self.escapeText(res.text))
                else:
                    self.sendPm(user.id, 'Please pm the command for a response.')

            if type(room.activity) == Workshop:
                room.activity.logSession(room.title, user.rank + user.name, message[4])

        elif 'pm' in message[1].lower():
            user = User(message[2][1:], message[2][0], self.isOwner(message[2]))
            if self.userIsSelf(user.id): return

            if message[4].startswith('/invite'):
                if not message[4][8:] == 'lobby':
                    if user.hasRank('+'):
                        self.joinRoom(message[4][8:])
                        self.log('Invite', message[4], user.id)
                    else:
                        self.sendPm(user.id, 'Only global voices (+) and up can add me to rooms, sorry :(')

            message[4] = '|'.join(message[4:])
            if message[4].startswith(self.commandchar) and message[4][1:] and message[4][1].isalpha():
                command = self.extractCommand(message[4])
                self.log('Command', message[4], user.id)
                params = message[4][len(command) + len(self.commandchar):].lstrip()

                response = self.do(self, command, Room('pm'), params, user)

                if not response.text or response.text == 'NoAnswer': return
                self.sendPm(user.id, response.text)

        # Tournaments
        elif 'tournament' == message[1]:
            if room.loading: return
            if 'create' in message[2]:
                room.createTour(self.ws, message[3], self.bh)
                # Tour was created, join it if in supported formats
                if self.details['joinTours'] and room.tour.format in self.bh.supportedFormats:
                    room.tour.joinTour()
            elif 'end' == message[2]:
                winner, tier = room.getTourWinner(message[3])
                if self.name in winner:
                    self.say(room.title, 'I won the {form} tournament :o'.format(form = tier))
                else:
                    self.say(room.title, 'Congratulations to {name} for winning :)'.format(name = ', '.join(winner)))
                room.endTour()
            elif 'forceend' in message[2]:
                room.endTour()
            else:
                # This is for general tournament updates
                if not room.tour: return
                room.tour.onUpdate(message[2:])


psb = PSBot()
restartCount = 0
while restartCount < 100:
    # This function has a loop that runs as long as the websocket is connected
    psb.ws.run_forever()
    # If we get here, the socket is closed and disconnected
    # so we have to reconnect and restart (after waiting a bit of course, say half a minute)
    time.sleep(30)
    print('30 seconds since last disconnect. Retrying connection...')
    psb.openConnection()
    restartCount += 1
    print('Restart Count:', restartCount)

