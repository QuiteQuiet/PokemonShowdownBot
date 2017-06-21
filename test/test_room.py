from room import Room
from user import User
import pytest

def testAddUser():
    test_room = Room('test')
    test_user = User('user')
    test_room.addUser(test_user)
    assert test_room.getUser('user'), 'Adding user to room failed'

def testRemoveUser():
    test_room = Room('test')
    test_user = User('user')
    test_room.addUser(test_user)
    test_room.removeUser('user')
    assert not test_room.getUser('user'), 'Removing user from room failed'

def testRenameUser():
    test_room = Room('test')
    test_user = User('user')
    test_room.addUser(test_user)
    test_room.renamedUser('user', User('user2'))
    assert not test_room.getUser('user') and test_room.getUser('user2'), 'Renaming user failed'

def testWhitelist():
    test_room = Room('test')
    test_user = User('user')
    assert not test_room.isWhitelisted(test_user), 'Wrongly accepted a not whitelisted user'
    assert test_room.addToWhitelist('user'), 'Failed to add user to whitelist'
    assert test_room.isWhitelisted(test_user), 'Whitelisted user not recognized'