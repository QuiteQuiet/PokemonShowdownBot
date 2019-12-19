import json
import time

from robot import PokemonShowdownBot, Room, User
from invoker import CommandInvoker
from plugins.messages import MessageDatabase


class PSBot(PokemonShowdownBot):
    """Mainly a wrapper class for the Robot class, implementing required methods.

    You should expect to be somewhat familiar with the PS protocols outlined here:
    https://github.com/Zarel/Pokemon-Showdown/blob/master/PROTOCOL.md

    For the sake of simplicity, we assume that the command char used is ~ in the documentation.
    Utility like functions are placed in the PokemonShowdownBot class, to make this handler
    class look cleaner.

    Attributes:
        invoker: Command method, handles command behaviour (i.e. ~git returns a url to this project)
        usernotes: MessageDatabase, which handles/logs all PMs sent from users
    """
    def __init__(self):
        """Initializes the PSBot class

        Setups up the commands, usernotes, and opens the websocket to the
        main pokemonshowdown server hosted on https://play.pokemonshowdown.com.
        """
        self.usernotes = MessageDatabase()
        PokemonShowdownBot.__init__(self,
                                    'ws://sim.smogon.com:8000/showdown/websocket')
        self.addExtraHandlers()
        self.invoker = CommandInvoker()

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
        if room.loading: return
        if self.userIsSelf(message[1:]):
            room.rank = message[0]
            room.doneLoading()
        user = User(message, message[0], self.isOwner(message))
        if not room.addUser(user):
            return self.takeAction(room.title, user, 'roomban', "You are blacklisted from this room, so please don't come here.")

    def addExtraHandlers(self):
        """Adds several handlers for chat messages that we need for this to function

        Args:
            None.
        Returns:
            None.
        Raises:
            None.
        """
        # A lot of local functions that'll only be used for the handlers
        # are found below.

        # Accept / Decline challenges
        def updatechallenges(self, room, challenges):
            challs = json.loads(challenges)
            if challs['challengesFrom']:
                opp = [name for name, form in challs['challengesFrom'].items()][0]
                format = challs['challengesFrom'][opp]
                if format in self.bh.supportedFormats:
                    team = self.bh.getRandomTeam(format)
                    self.send('|/utm {}'.format(team))
                    self.send('|/accept {name}'.format(name = opp))
                else:
                    self.sendPm(opp, "Sorry, I can't accept challenges in that format :(")

        def raw(self, room, *rawmessage):
            message = '|'.join(rawmessage)
            if message.startswith('<div class="infobox"> You joined '):
                room.doneLoading()

        def popup(self, room, *popup):
            popup = '|'.join(popup).replace('||', '\n\t')
            print('{}: {}'.format(room, popup))
            if popup.startswith('You have been inactive'):
                self.send('|/back')

        # Joined new room
        def users(self, room, users):
            for user in users.split(',')[1:]:
                rank = user[0]
                user = self.removeAfkMessage(user[1:])
                room.addUser(User(user, rank, self.isOwner(user)))
            # If PS doesn't tell us we joined, this still give us our room rank
            room.rank = users[users.index(self.name) - 1]

        def leave(self, room, user):
            if room.loading: return
            user = self.removeAfkMessage(user[1:])
            if self.userIsSelf(user):
                # This is just a failsafe in case the bot is forcibly removed from a room.
                # Any other memory release required is handeled by the room destruction
                self.rooms.pop(room.title, None)
                return
            userid = self.toId(user)
            room.removeUser(userid)

        def rename(self, room, new, old):
            if room.loading: return
            rank = new[0]
            new = self.removeAfkMessage(new[1:])
            # Keep track of your own rank
            # When demoting / promoting a user the server sends a |N| message to update the userlist
            if self.userIsSelf(new):
                room.rank = rank
            newUser = User(new, rank, self.isOwner(new))
            room.renamedUser(self.toId(old), newUser)
            self.handleJoin(room, rank + new)

        # Chat messages
        def timestampchat(self, room, timestamp, user, *text):
            user = room.getUser(self.toId(user))
            if not user: return
            if self.userIsSelf(user.id): return

            message = '|'.join(text)
            if room.isHistory(timestamp, message): return

            room.logChat(user, message, timestamp)

            if message.startswith(self.commandchar) and message[1:] and (message[1].isalpha() or message[1] == '!'):
                command = self.extractCommand(message)
                self.log('Command', message, user.id)

                res = self.invoker.execute(self, command, message[len(command) + 1:].lstrip(), user, room)
                if not res.text or res.text == 'NoAnswer': return

                if self.userHasPermission(user, self.details['broadcastrank']) or res.ignoreBroadcastPermission:
                    if not res.ignoreEscaping:
                        res.text = self.escapeText(res.text)
                    self.reply(room.title, user, res.text, res.samePlace, res.ignoreMultiline)

                elif res.canPmReply:
                    self.sendPm(user.id, self.escapeText(res.text), res.ignoreMultiline)
                else:
                    self.sendPm(user.id, 'Please pm the command for a response.')

        def chat(self, room, user, *text):
            timestampchat(self, room, time.time(), user, *text)

        def pm(self, room, sender, receiver, *message):
            user = User(sender[1:], sender[0], self.isOwner(sender))
            if self.userIsSelf(user.id): return

            message = '|'.join(message)
            if message.startswith('/invite'):
                if not message[8:] == 'lobby':
                    if user.hasRank('+'):
                        self.joinRoom(message[8:])
                        self.log('Invite', message, user.id)
                    else:
                        self.sendPm(user.id, 'Only global voices (+) and up can add me to rooms, sorry :(')

            if message.startswith(self.commandchar) and message[1:] and (message[1].isalpha() or message[1] == '!'):
                command = self.extractCommand(message)
                self.log('Command', message, user.id)
                params = message[len(command) + len(self.commandchar):].lstrip()

                response = self.invoker.execute(self, command, params, user, Room('pm'))

                if not response.text or response.text == 'NoAnswer': return
                self.sendPm(user.id, response.text, response.ignoreMultiline)

        # Add handlers
        self.addHandler('deinit', lambda self, r:  self.rooms.pop(r.title, None))
        self.addHandler('noinit', lambda self, r:  self.rooms.pop(r.title, None))
        self.addHandler('j', lambda self, r, name: self.handleJoin(r, name))
        self.addHandler('join', lambda self, r, name: self.handleJoin(r, name))
        self.addHandler('l', leave)
        self.addHandler('leave', leave)
        self.addHandler('n', rename)
        self.addHandler('name', rename)
        self.addHandler('c', chat)
        self.addHandler('chat', chat)
        self.addHandler('c:', timestampchat)
        self.addHandler('pm', pm)
        self.addHandler('popup', popup)
        self.addHandler('updatechallenges', updatechallenges)
        self.addHandler('raw', raw)
        self.addHandler('users', users)

if __name__ == '__main__':
    psb = PSBot()
    restartCount = 0
    while restartCount < 10:
        # This function has a loop that runs as long as the websocket is connected
        psb.listen()
        # If we get here, the socket is closed and disconnected
        # so we have to reconnect and restart (after waiting a bit of course, say half a minute)
        time.sleep(3**(restartCount + 1))
        print('{} seconds since last disconnect. Retrying connection...'.format(3**(restartCount + 1)))
        psb.openConnection()
        restartCount += 1
        print('Restart Count:', restartCount)
