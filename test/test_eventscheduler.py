from invoker import ReplyObject
from commands import URL
from room import Room
from user import User
from app import PSBot
import re
from datetime import datetime, timedelta


psb = PSBot()
test_room = Room('test')
test_user = User('user', rank='#')

def testAddEvent():
    reply = psb.invoker.execute(psb, 'addevent', '2000/02/02 00:00|0|test', test_user, test_room)
    expected_reply = ReplyObject('New event scheduled for 2000/02/02 00:00, repeating every 0 days.', reply=True, pmreply=True)
    assert reply == expected_reply, 'Failed to add event; {}'.format(reply.text)

def testRescheduling():
    current_time = datetime.now().replace(microsecond=0)
    scheduled_time = current_time - timedelta(days=2)
    period = 0.5
    new_time = datetime.utcfromtimestamp(test_room.scheduler.getNextStartTime(scheduled_time, period))
    expected_new_start = current_time + timedelta(days=1) * period
    assert new_time == expected_new_start, "Unexpected new start time; {} == {}".format(new_time, expected_new_start)