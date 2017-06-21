from user import User
import pytest

def testHigherRankComparision():
    reg_user = User('user1')
    assert not reg_user.hasRank('~'), 'Invalid rank comparision; it should not get \' \' >= ~'
def testLowerRankComparision():
    reg_user = User('user1', '@')
    assert reg_user.hasRank('+'), 'Invalid rank comparision; it should not get @ < +'

def testOwner():
    reg_user = User('user1', ' ')
    assert not reg_user.isOwner(), 'Regular user recognized as owner'
    owner = User('owner', '~', True)
    assert owner.isOwner(), 'Proper owner not regognized'

def testNonexistingRank():
    false_user = User('user', '=')
    assert not false_user.hasRank(' '), 'Nonexisting ranks should not be recognized as anything'