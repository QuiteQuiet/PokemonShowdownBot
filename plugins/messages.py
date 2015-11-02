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
        if to not in self.messages: self.messages[to] = {}
        if sent in self.messages[to]: return False

        self.messages[to][sent] = Message(sent, msg)
        return True
    def getMessage(self, user):
        ''' This gets and delete every message to this user from storage '''

        # No need to test for existance, this assumes a message exists
        # and usage should first test for existance.
        messages = self.removeMessage(user)
        combine = []
        for msg in messages: combine.append(messages[msg].replyFormat())       
        return '\n'.join(combine)

    def hasMessage(self, user):
        return user in self.messages
    def alreadySentMessage(self, user, frm):
        return user in self.messages and frm in self.messages[user]
    def removeMessage(self, to):
        return self.messages.pop(to, None)

