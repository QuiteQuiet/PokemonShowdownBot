# This file is an collection import to collect every future chatgame under the namespace
# games.[the game]. Additional games should be imported in here and not directly referenced in
# either commands-py or __init__.py.
#
# New games should be created as a complete class per game, to be imported as
# from data.games import [your game], with the entry in this file following that of the
# hangman example.
from plugins.hangman import Hangman
