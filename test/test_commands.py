from invoker import CommandInvoker, ReplyObject
from commands import URL
from room import Room
from user import User
from app import PSBot
from data.pokedex import Pokedex
import re


psb = PSBot()
test_room = Room('test')
test_user = User('user')

""" Tests the commands that are within the CommandInvoker
"""

def testInvalidCommand():
    reply = psb.invoker.execute(psb, 'test_command', test_room, '', test_user)
    assert reply == ReplyObject('test_command is not a valid command.'), 'Invalid command not properly recognized; {}'.format(reply.text)

def testExternalLoader():
    reply = psb.invoker.execute(psb, 'source', test_room, '', test_user)
    assert reply == ReplyObject('Source code can be found at: {}'.format(URL()), True), 'Commands not properly loaded'
