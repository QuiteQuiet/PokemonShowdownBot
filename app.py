import json
import time

from robot import PokemonShowdownBot, Room, User
from invoker import CommandInvoker
from plugins.messages import MessageDatabase
from plugins.workshop import Workshop


class PSBot(PokemonShowdownBot):
    """Mainly a wrapper class for the Robot class, implementing required methods.

    This implements the major method required: splitMessage. Also manages the
    delegation of tasks to their respective handlers. Most of the underlying
    functionality and/or function calls can be found in the inherited class
    PokemonShowdownBot in robot.py.

    You should expect to be somewhat familiar with the PS protocols outlined here:
    https://github.com/Zarel/Pokemon-Showdown/blob/master/PROTOCOL.md

    For the sake of simplicity, we assume that the command char used is ~ in the documentation.
    Utility like functions are placed in the PokemonShowdownBot class, to make this handler
    class look cleaner.

    Attributes:
        do: Command method, handles command behaviour (i.e. ~git returns a url to this project)
        usernotes: MessageDatabase, which handles/logs all PMs sent from users
    """
    def __init__(self):
        """Initializes the PSBot class

        Setups up the commands, usernotes, and opens the websocket to the
        main pokemonshowdown server hosted on https://play.pokemonshowdown.com.
        """
        self.usernotes = MessageDatabase()
        PokemonShowdownBot.__init__(self,
                                    'ws://sim.psim.us:8000/showdown/websocket',
                                    self.splitMessage)
        self.invoker = CommandInvoker()

    def splitMessage(self, ws, message):
        """ Decides bot behaviour wth the server based on the content from the websocket.

        This method is the modified splitMessage that is passed to the open
        websocket in the PokemonShowdownBot class. This method splits the string given
        by the websocket and delegates the tasks to the corresponding interfaces.

        Args:
            ws: websocket, websocket object we are receiving information from.
            message: string,  information given by the websocket.
        Returns:
            None.
        Raises:
            By default, nothing is raised. But handlers which this method delegates tasks to
            may produce exceptions, so best follow the path to the individual module.
        """
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
                import traceback
                print('AttributeError: {}'.format(e))
                traceback.print_tb(e.__traceback__)
                print('MESSAGE THAT CAUSED IT:\n{}'.format(msg))
            return

        for m in msg:
            self.parseMessage(m, room)

    def handleJoin(self, room, message):
        """ Handles new users entering a room.

        Args:
            room: Room object, room this message was received from.
            message: string, string produced from user joining this room.
        Returns:
            None.
        Raises:
            None.
        """
        if self.userIsSelf(message[1:]):
            room.rank = message[0]
            room.doneLoading()
        user = User(message, message[0], self.isOwner(message))
        if not room.addUser(user):
            return self.takeAction(room.title, user, 'roomban', "You are blacklisted from this room, so please don't come here.")

        # If the user have a message waiting, tell them that in a pm
        if self.usernotes.shouldNotifyMessage(user.id):
            self.sendPm(user.id, self.usernotes.pendingMessages(user.id))

    def parseMessage(self, msg, roomName):
        """Parses the message given by a user and delegates the tasks further

        This is where we handle the parsing of all the non-battle related PS protocols.
        Tasks like user related queries (i.e. commands) are delegated to the Command method.
        And Showdown tournaments are handled in their own handler in the plugins module.
        Likewise for the MessageDatabase interface.

        Args:
            msg: String, string produced from interacting with the websocket connected
                 to the PS server. Example: "|c:|1467521329| bb8nu|random chat message".
            roomName: String, name of the room that the message came from.
        Returns:
            None.
        Raises:
            None.
        """
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
            # This gets sent before `updatechallenges` does when receiving a battle, but it's
            # not useful for anything, so just return straight away
            return

        # This is a safeguard for l and n in case that a moderation action happen
        elif 'unlink' == message[1] or 'uhtml' in message[1] or 'html' == message[1]:
            return

        # Room was left in some way other than through ~leave
        elif 'deinit' == message[1]:
            self.rooms.pop(room.title)

        elif 'noinit' == message[1]:
            # we didn't join the room for some other reason (doesn't exist/roombanned)
            self.rooms.pop(room.title, None)

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
            if room.loading: return
            self.handleJoin(room, message[2])

        elif 'l' == message[1].lower() or 'leave' == message[1].lower():
            if room.loading: return
            if self.userIsSelf(message[2][1:]):
                # This is just a failsafe in case the bot is forcibly removed from a room.
                # Any other memory release required is handeled by the room destruction
                if roomName in self.rooms:
                    self.rooms.pop(room.title)
                return
            userid = self.toId(message[2])
            room.removeUser(userid)
        elif 'n' in message[1].lower() and len(message[1]) < 3:
            if room.loading: return
            # Keep track of your own rank
            # When demoting / promoting a user the server sends a |N| message to update the userlist
            if self.userIsSelf(message[2][1:]):
                room.rank = message[2][0]
            newUser = User(message[2][1:], message[2][0], self.isOwner(message[2]))
            room.renamedUser(self.toId(message[3]), newUser)
            self.handleJoin(room, message[2])

        # Chat messages
        elif 'c' in message[1].lower():
            if room.loading: return
            user = room.getUser(self.toId(message[3]))
            if not user: return
            if self.userIsSelf(user.id): return

            room.logChat(user, message[4], message[2])

            saidMessage = '|'.join(message[4:])
            if saidMessage.startswith(self.commandchar) and saidMessage[1:] and (saidMessage[1].isalpha() or saidMessage[1] == '!'):
                command = self.extractCommand(saidMessage)
                self.log('Command', saidMessage, user.id)

                res = self.invoker.execute(self, command, saidMessage[len(command) + 1:].lstrip(), user, room)
                if not res.text or res.text == 'NoAnswer': return

                if self.userHasPermission(user, self.details['broadcastrank']) or res.ignoreBroadcastPermission:
                    if not res.ignoreEscaping:
                        res.text = self.escapeText(res.text)
                    self.reply(room.title, user, res.text, res.samePlace)

                elif res.canPmReply:
                    self.sendPm(user.id, self.escapeText(res.text))
                else:
                    self.sendPm(user.id, 'Please pm the command for a response.')

            # Test room punishments after commands
            anything = room.moderation.shouldAct(message[4], user, message[2])
            if anything and self.canPunish(room):
                action, reason = room.moderation.getAction(room, user, anything, message[2])
                self.takeAction(room.title, user, action, reason)

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
            if message[4].startswith(self.commandchar) and message[4][1:] and (message[4][1].isalpha() or message[4][1] == '!'):
                command = self.extractCommand(message[4])
                self.log('Command', message[4], user.id)
                params = message[4][len(command) + len(self.commandchar):].lstrip()

                response = self.invoker.execute(self, command, params, user, Room('pm'))

                if not response.text or response.text == 'NoAnswer': return
                self.sendPm(user.id, response.text)

        # Tournaments
        elif 'tournament' == message[1]:
            if 'create' in message[2]:
                room.createTour(self.ws, message[3], self.bh)

                if room.loading: return
                # Tour was created, join it if in supported formats
                if self.details['joinTours'] and room.tour.format in self.bh.supportedFormats:
                    room.tour.joinTour()
            elif 'end' == message[2]:
                if not room.loading:
                    winners, tier = room.getTourWinner(message[3])
                    if self.name in winners:
                        message = 'I won the {form} tournament :o'.format(form = tier)
                        if len(winners) > 1:
                            winners.remove(self.name)
                            message += '\nCongratulations to {others} for also winning :)'.format(others = ', '.join(winners))
                        self.say(room.title, message)
                    else:
                        self.say(room.title, 'Congratulations to {name} for winning :)'.format(name = ', '.join(winners)))
                room.endTour()
            elif 'forceend' in message[2]:
                room.endTour()
            else:
                # This is for general tournament updates
                if not room.tour or room.loading: return
                room.tour.onUpdate(message[2:])

if __name__ == '__main__':
    psb = PSBot()
    restartCount = 0
    while restartCount < 100:
        # This function has a loop that runs as long as the websocket is connected
        psb.listen()
        # If we get here, the socket is closed and disconnected
        # so we have to reconnect and restart (after waiting a bit of course, say half a minute)
        time.sleep(30)
        print('30 seconds since last disconnect. Retrying connection...')
        psb.openConnection()
        restartCount += 1
        print('Restart Count:', restartCount)
