import requests

class Workshop:
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
        with open('logs/{room}-workshop-{host}.txt'.format(room = room, host = self.host), 'a') as log:
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
