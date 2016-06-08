import requests

from plugins.games import GenericGame

class Workshop(GenericGame):
    def __init__(self, host):
        self.host = host
        self.team = []

    def addPokemon(self, poke):
        if len(self.team) >= 6:
            return 'team is full'
        self.team.append(poke)
        return '{mon} added'.format(mon = poke)
    def removePokemon(self, poke):
        if poke in self.team:
            self.team.remove(poke)
            return '{mon} removed'.format(mon = poke)
        return '{mon} is not in the team'.format(mon = poke)
    def getTeam(self):
        if len(self.team) <= 0:
            return 'team is empty'
        return ' / '.join(self.team)
    def clearTeam(self):
        self.team = []
        return 'team cleared'

    def logSession(self, room, user, message):
        with open('logs/{room}-workshop-{host}.txt'.format(room = room, host = self.host), 'a') as log:
            log.write('{name}: {text}\n'.format(name = user, text = message))

    def pasteLog(self, room, apiKey):
        if apiKey == '0': return 'No paste for the workshop could be generated'
        with open('logs/{room}-workshop-{host}.txt'.format(room = room, host = self.host), 'r') as log:
            r = requests.post('http://pastebin.com/api/api_post.php',
                            data = {
                                'api_dev_key': apiKey,
                                'api_option':'paste',
                                'api_paste_code': log.read(),
                                'api_paste_private': 0,
                                'api_paste_expire_date':'N'
                                })
            if 'Bad API request' in r.text:
                return 'Something went wrong ({error})'.format(error = r.text)
            return r.text
    def hasHostingRights(self, user):
        return self.host == user.id or user.hasRank('@')

def handler(bot, cmd, room, msg, user):
    if msg.startswith('new'):
        if not user.hasRank('@'): return "You don't have permission to start workshops (Requires @)", False
        if room.game: return 'A room game is already in progress', True
        room.game = Workshop(bot.toId(msg[len('new '):]) if msg[len('new '):] else user.id)
        return 'A new workshop session was created', True

    if not (room.game and room.game.isThisGame(Workshop)): return 'No Workshop in progress right now', True
    workshop = room.game
    if msg.startswith('add'):
        if not workshop.hasHostingRights(user): return 'Only the workshop host or a Room Moderator can add Pokemon', True
        return workshop.addPokemon(msg[len('add '):]), True
    elif msg.startswith('remove'):
        if not workshop.hasHostingRights(user): return 'Only the workshop host or a Room Moderator can remove Pokemon', True
        return workshop.removePokemon(msg[len('remove '):]), True
    elif msg == 'clear':
        if not workshop.hasHostingRights(user): return 'Only the workshop host or a Room Moderator can clear the team', True
        return workshop.clearTeam(), True
    elif msg == 'team':
        return workshop.getTeam(), True
    elif msg == 'end':
        if not workshop.hasHostingRights(user): return 'Only the workshop host or a Room Moderator can end the workshop', True
        bot.sendPm(workshop.host, workshop.pasteLog(room.title, bot.details['apikey']))
        room.game = None
        return 'Workshop session ended', True