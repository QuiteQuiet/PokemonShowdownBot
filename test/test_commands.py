from commands import Command, ReplyObject
from room import Room
from user import User
from app import PSBot
from data.pokedex import Pokedex
import re


psb = PSBot()

""" Tests the commands that are within the Command method
"""


def testPokemonSmogonAnalysis():
    test_room = Room('test')
    regular_user = User('user', False)
    for p in Pokedex.keys():
        pok = re.sub('-(?:mega(?:-(x|y))?|primal)', '', p, flags=re.I).replace(' ', '').lower()
        substitutes = {'gourgeist-s':'gourgeist-small',  # This doesn't break Arceus-Steel like adding |S to the regex would
                       'gourgeist-l':'gourgeist-large',  # and gourgeist-s /pumpkaboo-s still get found, because it matches the
                       'gourgeist-xl':'gourgeist-super', # entry for gougeist/pumpkaboo-super
                       'pumpkaboo-s':'pumpkaboo-small',
                       'pumpkaboo-l':'pumpkaboo-large',
                       'pumpkaboo-xl':'pumpkaboo-super',
                       'giratina-o':'giratina-origin',
                       'mr.mime':'mr_mime',
                       'mimejr.':'mime_jr'}
        pok2 = pok
        if pok in substitutes:
            pok2 = substitutes[pok]
        reply = Command(psb, p.replace(' ', '').lower(), test_room, '', regular_user)
        answer = ReplyObject('Analysis: http://www.smogon.com/dex/sm/pokemon/{poke}/'.format(poke=pok2), True)
        assert reply.text == answer.text, '{poke} was not recognized; {rep} == {ans}'.format(poke=pok, rep=reply.text, ans=answer.text)

