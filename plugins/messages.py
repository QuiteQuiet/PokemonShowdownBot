import random
import re

class Message:
    def __init__(self, sent, msg):
        self.sent = sent
        self.msg = msg
    def replyFormat(self):
        return 'From {user}: {msg}'.format(user = self.sent, msg = self.msg)

class MessageDatabase:
    def __init__(self):
        self.messages = {}
    def pendingMessages(self, user):
        cnt = len(self.messages[user])
        return 'You have {nr} message{s} waiting for you.\nUse ~read [number] to get [number] of messages shown to you'.format(nr = cnt, s = 's' if cnt > 1 else '')
    def addMessage(self, to, sent, msg):
        if to not in self.messages: self.messages[to] = {}
        if sent in self.messages[to]: return False

        self.messages[to][re.sub(r'[^a-zA-z0-9]', '', sent).lower()] = Message(sent, msg)
        return True

    def getMessage(self, user):
        return self.removeRandomMessage(user).replyFormat()
    def getMessages(self, user, amnt):
        ''' This removes amnt number of messages from the message service '''

        # This can be super-spammy for users with a lot of pending messages
        # as they can opt to look at all at once
        reply = ''
        if amnt > len(self.messages[user]): amnt = len(self.messages[user])
        while amnt > 0:
            reply += self.getMessage(user) + ('\n' if amnt > 1 else '')
            amnt -= 1
        # Remove the user from the list if there's no messages left
        if not self.messages[user]:
            self.messages.pop(user)
        return reply

    def getAllMessages(self, user):
        ''' This gets and delete every message to this user from storage '''

        # No need to test for existance, this assumes a message exists
        # and usage should first test for existance.
        messages = self.removeAllMessages(user)
        combine = []
        for msg in messages:
            combine.append(messages[msg].replyFormat())
        return '\n'.join(combine)

    def hasMessage(self, user):
        return user in self.messages

    def alreadySentMessage(self, user, frm):
        return user in self.messages and frm in self.messages[user]

    def removeRandomMessage(self, to):
        return self.messages[to].pop(random.choice(list(self.messages[to].keys())), None)
    def removeMessage(self, to, frm):
        msg = self.messages[to].pop(frm, None)
        # If the user has no message left, clear the name entry
        if not self.messages[to]: self.messages.pop(to)
        return msg

    # Unused but still supported
    def removeAllMessages(self, to):
        return self.messages.pop(to, None)

