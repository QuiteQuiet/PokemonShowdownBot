from room import Room
from user import User
import pytest
from datetime import datetime

def testAddBannedWord():
    test_room = Room('test')
    test_room.moderation.addBan('phrase', 'CATFISH')
    assert test_room.moderation.isBanword('catfish'), 'catfish should be a banned phrase'

def testRemoveBannedWord():
    test_room = Room('test')
    test_room.moderation.addBan('phrase', 'CATFISH')
    test_room.moderation.removeBan('phrase', 'catfish')
    assert not test_room.moderation.isBanword('catfish'), 'catfish should not be a banned phrase'

def testFindingURL():
    test_room = Room('test')
    assert test_room.moderation.containUrl('http://github.com is a good website'), 'Should find an url in this string'

def testStretching():
    test_room = Room('test')
    assert test_room.moderation.isStretching('oioioioioioio', test_room.users), 'Should be recognized as stretching'

def testCaps():
    test_room = Room('test')
    assert test_room.moderation.isCaps('GITHUB IS A GOOD WEBSITE', test_room.users), 'should recognize it as caps'

def testSpam():
    test_room = Room('test')
    test_user = User('user')
    assert not test_room.moderation.isSpam('1', test_user, datetime.utcfromtimestamp(1)), 'should not be spam'
    assert not test_room.moderation.isSpam('2', test_user, datetime.utcfromtimestamp(2)), 'should not be spam'
    assert not test_room.moderation.isSpam('3', test_user, datetime.utcfromtimestamp(3)), 'should not be spam'
    assert not test_room.moderation.isSpam('4', test_user, datetime.utcfromtimestamp(4)), 'should not be spam'
    assert test_room.moderation.isSpam('5', test_user, datetime.utcfromtimestamp(5)), 'should be spam now'

def testSpam2():
    test_room = Room('test')
    test_user = User('user')
    assert not test_room.moderation.isSpam('1', test_user, datetime.utcfromtimestamp(1)), 'should not be spam'
    assert not test_room.moderation.isSpam('2', test_user, datetime.utcfromtimestamp(5)), 'should not be spam'
    assert not test_room.moderation.isSpam('3', test_user, datetime.utcfromtimestamp(6)), 'should not be spam'
    assert not test_room.moderation.isSpam('4', test_user, datetime.utcfromtimestamp(7)), 'should not be spam'
    assert not test_room.moderation.isSpam('5', test_user, datetime.utcfromtimestamp(8)), 'should not be spam'
    assert test_room.moderation.isSpam('6', test_user, datetime.utcfromtimestamp(9)), 'should be spam now'

def testConfig():
    test_room = Room('test', {
        'moderate': {
            'room': 'test',
                'anything': True,
                'spam': False,
                'banword': False,
                'stretching': False,
                'caps': True,
                'groupchats': False,
                'urls': False
            },
        'allow games':False,
        'tourwhitelist':[]}
    )
    test_user = User('user')
    assert 'caps' == test_room.moderation.shouldAct('OIOIOIOIOIOIOIOI', test_user, 0), 'should be punished for caps not stretching'

def testPunishmentIncrease():
    test_room = Room('test')
    test_user = User('user')
    first_action, reply = test_room.moderation.getAction(test_room, test_user, 'caps', 0)
    second_action, reply = test_room.moderation.getAction(test_room, test_user, 'flooding', 0)
    assert not first_action == second_action, '{} == {}; should get escalated punishment'.format(first_action, second_action)