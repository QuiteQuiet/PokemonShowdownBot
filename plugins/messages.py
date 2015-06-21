class Message:
    def __init__(self, sent, msg):
        self.sent = sent
        self.msg = msg
    def replyFormat(self):
        return 'From {user}: {msg}'.format(user = self.sent, msg = self.msg)

class MessageDatabase:
    def __init__(self):
        self.messages = {}
    def addMessage(self, to, sent, msg):
        if to in self.messages:
            return False
        self.messages[to] = Message(sent, msg)
        return True
    def getMessage(self, user):
        ''' This gets and delete the message from storage '''

        # No need to test for existance, this assumes a message exists
        # and usage should first test for existance.
        return self.removeMessage(user).replyFormat()
    def hasMessage(self, user):
        return user in self.messages
    def removeMessage(self, to):
        return self.messages.pop(to, None)

