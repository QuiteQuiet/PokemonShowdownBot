from datetime import datetime, timedelta
import os
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

        # Check if the room already has configured events and set
        # them up again if that is the case
        # TODO: do this

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
        if not self.thread:
            self.robot = robot
            self.thread = threading.Thread(target=self.runForever, daemon=True)
        return True

    def addJob(self, moment, periodicity, job):
        firstJob = self.scheduler.empty()

        if job.startswith('http'):
            job = PasteImporter.getPasteContent(job).strip()

        # Schedule first run of this event
        periodicity = float(periodicity)
        timestamp = self.getNextStartTime(datetime.strptime(moment.strip(), '%Y/%m/%d %H:%M'), periodicity)
        self.scheduler.enterabs(timestamp,
                                1,
                                self.runEvent,
                                kwargs={'jobtime':timestamp,
                                        'job': job,
                                        'periodicity': periodicity})
        if firstJob:
            try:
                self.thread.start()
            except RuntimeError:
                # Thread is already running
                pass

    def clearEvents(self):
        # Clears all events from the queue by calling sched.cancel on each event
        list(map(self.scheduler.cancel, self.scheduler.queue))

    def getNextStartTime(self, startTime, periodicity):
        '''Find the next valid start time after the current time

        Args:
            startTime: (datetime) Starttime for the first run
                                  of the event.
            periodicity: (float)  Period for how often the event
                                  should run.
        '''
        if periodicity <= 0: return startTime

        currentTime = datetime.now()
        if periodicity < 1:
            delta = timedelta(days=1) * periodicity
        else:
            delta = timedelta(days=periodicity)

        nextValidTime = startTime
        while currentTime >= nextValidTime:
            nextValidTime += delta

        return calendar.timegm(nextValidTime.timetuple())

    def getEvents(self):
        return [(event.time, event.action.__name__) for event in self.scheduler.queue]

    def runEvent(self, jobtime, periodicity, job):
        if not self.robot: return # Just in case. This will not reschedule the job either

        instructions = job.split('\n')

        for instruction in instructions:
            self.robot.say(self.room, instruction)
            time.sleep(.5) # Don't spam too much

        if periodicity > 0:
            # Reschedule next run in periodicity days
            nextStart = self.getNextStartTime(datetime.utcfromtimestamp(jobtime), periodicity)
            self.scheduler.enterabs(nextStart,
                                    1,
                                    self.runEvent,
                                    kwargs={'jobtime':nextStart,
                                            'job': job,
                                            'periodicity': periodicity})

def addEvent(robot, cmd, params, user, room):
    reply = ReplyObject('', reply=True, pmreply=True)
    if not user.hasRank('#'): return reply.response("Permission denied, only Room Owners (#) and up can use this command.")

    # First event added, create the thread
    if not room.scheduler.thread:
        room.scheduler.configureEventScheduler(robot)

    with open('added-jobs-{}.csv'.format(room.title), 'a+') as jobs:
        jobs.write('{user},{job}\n'.format(user=user.id, job=params))

    date, frequency, joblist = params.replace('| ', '|').split('|')
    # Validate date string format first
    if not EventScheduler.validateDateString(date):
        return reply.response('Invald date format. Expected format is YYYY/MM/DD HH:MM.')

    room.scheduler.addJob(date, frequency, joblist)
    return reply.response('New event scheduled for {date}, repeating every {freq} days.'.format(date=date, freq=frequency))

def clearEvents(robot, cmd, params, user, room):
    reply = ReplyObject('', reply=True, pmreply=True)
    if not user.hasRank('#'): return reply.response("Permission denied, only Room Owners (#) and up can use this command.")

    try:
        os.remove('added-jobs-{}.csv'.format(room.title))
    except FileNotFoundError:
        # This is fine
        pass
    room.scheduler.clearEvents()

    return reply.response('All events cleared')

# Exports
commands = [
    Command(['addevent'], addEvent),
    Command(['clearevents'], clearEvents)
]