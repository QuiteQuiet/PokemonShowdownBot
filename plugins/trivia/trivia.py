from threading import Thread
import time

from plugins.trivia.questions import QuestionGenerator
# This class will put itself in a pseudo-while loop that is non-blocking
# to the rest of the program.
class Question:
    def __init__(self, q, a):
        self.text = q
        self.ans = a
class Trivia:
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
            # This breaks the pseudo-while loop and kills the Trivia session
            return
        newQ = self.generator.makeQuestion()
        self.question = Question(newQ['q'], newQ['a'])
        self.notify('Next question:')
        self.notify(self.question.text)
        # Create the waiting thread that'll time out after 40 seconds
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
