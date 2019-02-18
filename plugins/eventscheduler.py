from datetime import datetime, timedelta
import sched
import calendar
import time
import threading

from plugins.pasteImporter import PasteImporter
from invoker import ReplyObject, Command

class EventScheduler:
    """Scheduler to run a set of PS commands at a
    specific date and time. It will run once per week
    at the specified moment."""
    def __init__(self, room):
        self.robot = None
        self.room = room
        self.scheduler = sched.scheduler(time.time, time.sleep)
        self.thread = None

    @staticmethod
    def validateDateString(datestring):
        """Returns true if the date string is in the exact
        format that is expected and false otherwise.

        Args:
            datestring (str): The date string to test .
        Returns:
            Bool
        Raises:
            None
        """
        try:
            if datestring != datetime.strptime(datestring,'%Y/%m/%d %H:%M').strftime('%Y/%m/%d %H:%M'):
                raise ValueError
            return True
        except ValueError:
            return False

    def runForever(self):
        while True:
            self.scheduler.run()
            if self.scheduler.empty():
                time.sleep(60) # Only do periodic checks for new jobs

    def configureEventScheduler(self, robot):
        self.robot = robot
        self.thread = threading.Thread(target=self.runForever, daemon = True)
        return True

    def addJob(self, moment, periodicity, job):
        firstJob = self.scheduler.empty()

        if job.startswith('http'):
            job = PasteImporter.getPasteContent(job)

        # Schedule first run of this event
        timestamp = calendar.timegm(datetime.strptime(moment.strip(), '%Y/%m/%d %H:%M').timetuple())
        self.scheduler.enterabs(timestamp, 1, self.runEvent, kwargs={'jobtime':timestamp, 'job': job, 'periodicity': periodicity})

        if firstJob:
            # Start thread
            self.thread.start()

    def getEvents(self):
        return [(event.time, event.action.__name__) for event in self.scheduler.queue]

    def runEvent(self, jobtime, periodicity, job):
        if not self.robot: return # Just in case. This will not reschedule the job either

        instructions = job.split('\n')

        for instruction in instructions:
            self.robot.say(self.room.title, instruction)
            time.sleep(.5) # Don't spam too much

        # Reschedule next run in periodicity days
        periodicity = int(periodicity)
        if periodicity > 0:
            newJobTime = datetime.strptime(jobtime, '%Y/%m/%d %H:%M') + timedelta(days=periodicity)
            timestamp = calendar.timegm(newJobTime.timetuple())
            self.scheduler.enterabs(timestamp, 1, self.runEvent, kwargs={'jobtime':timestamp, 'job': job, 'periodicity': periodicity})

def addEvent(robot, cmd, params, user, room):
    reply = ReplyObject('', reply = True, pmreply = True)
    if not user.hasRank('#'): return reply.response("Permission denied, only Room Owners (#) and up can use this command.")

    with open('added-jobs.csv', 'a+') as jobs:
        jobs.write('{user},{job}\n'.format(user = user.id, job = params))

    date, frequency, joblist = params.replace('| ', '|').split('|')
    # Validate date string format first
    if not EventScheduler.validateDateString(date): return reply.response('Invald date format. Expected format is YYYY/MM/DD HH:MM.')

    room.scheduler.addJob(date, frequency, joblist)
    return reply.response('New event scheduled for {date}, repeating every {freq} days.'.format(date = date, freq = frequency))


# Exports
commands = [
    Command(['initevents'], lambda s, c, p, u, r: ReplyObject(r.scheduler.configureEventScheduler(s))),
    Command(['addevent'], addEvent)
]