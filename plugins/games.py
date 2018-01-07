# Generic game class that can test for permissions and things for games.
class GenericGame:
    def __init__(self, ws, room):
        self.ws = ws
        self.room = room
    def isThisGame(self, game):
        return type(self) == game
