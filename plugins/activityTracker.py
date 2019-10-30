import os
import pickle
from collections import defaultdict
from datetime import datetime, timedelta

def _initDict():
    return defaultdict(int)

class ActivityTracker:
    def __init__(self, dumpInterval):
        self.lastDump = 0 # For periodic dumping
        self.dumpInterval = dumpInterval
        self.date = datetime.today().strftime('%Y-%m-%d')
        self.currentDay = self.loadActivity()
        if not self.currentDay:
            self.currentDay = defaultdict(_initDict)

    def countActivity(self, room, user):
        # New day started, restart counting
        today = datetime.today().strftime('%Y-%m-%d')
        if self.date != today:
            self.dumpActivity()
            self.currentDay = defaultdict(_initDict)
            self.date = today
        self.currentDay[room.title][user.id] += 1
        self.lastDump += 1
        if self.lastDump > self.dumpInterval:
            self.dumpActivity()
            self.lastDump = 0

    def dumpActivity(self):
        today = datetime.today().strftime('%Y-%m-%d')
        month = '-'.join(today.split('-')[:2])
        logPath = 'logs/{month}/'.format(month = month)
        os.makedirs(logPath, exist_ok=True)
        logFile = '{path}/{file}.pickle'.format(path=logPath, file=today)
        with open(logFile, 'wb') as f:
            pickle.dump(self.currentDay, f)

    def loadActivity(self, date = ''):
        today = date if date else datetime.today().strftime('%Y-%m-%d')
        month = '-'.join(today.split('-')[:2])
        # Make logdir if it doesn't exist
        logPath = 'logs/{month}/'.format(month = month)
        os.makedirs(logPath, exist_ok=True)
        logFile = '{path}/{file}.pickle'.format(path=logPath, file=today)
        try:
            with open(logFile, 'rb') as f:
                logData = pickle.load(f)
        except FileNotFoundError:
            logData = None
        return logData

    def getActivityForPeriod(self, period, room, targetUser):
        combinedActivity = defaultdict(int)
        date = datetime.today()
        for _ in range(period):
            dateStr = date.strftime('%Y-%m-%d')
            data = self.loadActivity(dateStr)
            if data:
                for user in data[room.title]:
                    if targetUser == user:
                        combinedActivity[dateStr] += data[room.title][user]
                    elif not targetUser:
                        combinedActivity[user] += data[room.title][user]
            if targetUser and not dateStr in combinedActivity:
                combinedActivity[dateStr] = 0
            date = date - timedelta(1)
        if not targetUser:
            # No target user, sort by lines
            return sorted(combinedActivity.items(), key=lambda e: e[1], reverse=True)
        else:
            # Have a target user, sort by date
            return sorted(combinedActivity.items(), key=lambda e: e[0], reverse=True)

