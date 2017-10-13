from threading import Thread
import time

from invoker import ReplyObject, Command
from plugins.trivia.questions import QuestionGenerator
from plugins.games import GenericGame
# This class will put itself in a pseudo-while loop that is non-blocking
# to the rest of the program.
class Question:
    def __init__(self, q, a):
        self.text = q
        self.ans = a
class Trivia(GenericGame):
    def __init__(self, ws, room, kind):
        self.ws = ws
        self.room = room
        self.kind = kind
        self.generator = QuestionGenerator()
        self.question = None
        self.solved = False
        self.multiple = False
        self.solver = ''
        self.endSession = False
        # Create the first thread that starts the loop
        self.thread = Thread(target = self.customWait,
                             name = 'customWait',
                             args = (5,),
                             daemon = True)
        self.thread.start()

    def notify(self, msg):
        self.ws.send('{room}|{msg}'.format(room = self.room, msg = msg))

    def customWait(self, secondsToWait):
        ''' Between every question there is a 10 second waiting time '''
        secondsPassed = 0
        while secondsPassed <= secondsToWait or self.endSession:
            time.sleep(1)
            secondsPassed += 1
        if self.endSession:
            # This breaks the while loop and kills the Trivia session
            return
        newQ = self.generator.makeQuestion()
        self.question = Question(newQ['q'], newQ['a'])
        self.notify('Next question:')
        self.notify(self.question.text)
        # Create the waiting thread that'll time out after 30 seconds
        self.thread = Thread(target = self.wait30Sec,
                             name = 'longWait',
                             daemon = True)
        self.thread.start()

    def wait30Sec(self):
        ''' Every question have a 30 second answering period or until someone get the question right '''
        secondsPassed = 0
        while secondsPassed <= 30 or self.endSession:
            time.sleep(1)
            secondsPassed += 1
        if self.solved:
            self.notify('{name} was correct{extra}!'.format(name = self.solver,
                                                          extra = ' first' if self.multiple else ''))
        else:
            self.notify('No one got it right')
        self.notify('The answer was {ans}.'.format(ans = self.question.ans))
        if self.endSession:
            return
        self.clear()
        self.notify('Next round will start soon.')
        self.thread = Thread(target = self.customWait,
                             name = 'customWait',
                             args = (10,),
                             daemon = True)
        self.thread.start()

    def tryAnswer(self, guess):
        if guess.lower() == self.question.ans:
            self.solved = True
        return self.solved

    def wasSolved(self, by):
        self.solver = by
    def clear(self):
        self.solved = False
        self.multiple = False
        self.solver = ''
    def status(self):
        return self.thread.name

def triviaCommands(bot, cmd, msg, user, room):
    reply = ReplyObject('', True, False, False, True, True)
    if room.isPM: return reply.response("Don't try to play games in pm please")
    if cmd == 'trivia':
        if not msg: return reply.response('{msg} is not an valid parameter for trivia')
        if room.activity: return reply.response('There is already a game running in this room')

        params = bot.removeSpaces(msg).split(',')
        if params[0] in ['start', 'begin']:
            if not room.allowGames: return reply.response('This room does not support chatgames.')
            kind = 'first'
            if len(params) > 1:
                kind = params[1]
            if user.hasRank('@'):
                room.activity = Trivia(bot.ws, room.title, kind)
                return reply.response('A new trivia session has started.')
            return reply.response('You do not have permission to set up a trivia session')
        elif params[0] in ['stop', 'end']:
            # The trivia class will solve everything after doing this.
            room.activity.endSession = True
            room.activity = None
            return reply.response('The trivia session has been ended')

    if cmd == 'ta':
        if not (room.activity and room.activity.isThisGame(Trivia)): return reply.response('There is no ongoing trivia session.')
        # Don't give information if wrong or right here, let Trivia deal with that
        if room.activity.tryAnswer(msg):
            if not room.activity.solver:
                room.activity.wasSolved(user.name)
            else:
                room.activity.multiple = True
        return reply.response('NoAnswer')
    return reply.response('')

commands = [Command(['trivia'], triviaCommands)]