from robot import PokemonShowdownBot
from room import Room
from user import User
import yaml
import pytest

bot = PokemonShowdownBot('')

# This tests helper functions contained within PokemonShowdownBot but not its core functionality
# due to the requirement of being connected to Pokemon Showdown for that.
def testToId():
    assert 'testmessage' == bot.toId('TEST MESSAGE!!'), 'PokemonShowdownBot.toId improperly modified the id text'

def testExtractCommand():
    message = '{}test param1, param2, param3'.format(bot.commandchar)
    command = bot.extractCommand(message)
    assert 'test' == command, 'Command not properly extracted from the message; test == {}'.format(command)

def testSelfPermissionCheck():
    test_room = Room('test')
    test_room.rank = '@'
    assert bot.canPunish(test_room), 'Not properly recognizing it can punish users in the room'

def testUserPermissionCheck():
    test_user = User('user', '+')
    assert bot.userHasPermission(test_user, '+'), 'Not properly recognizing a user has the correct permission'
