from invoker import ReplyObject, Command

import re
from collections import deque
from datetime import datetime, timedelta
import urllib
import yaml

class PunishedUser:
    def __init__(self, name, score, now):
        self.name = name
        self.points = score
        self.lastPunished = now
        self.lastAction = ''

class ModerationHandler:

    @staticmethod
    def MIN_CAPS_LENGTH(): return 12
    @staticmethod
    def CAPS_PROPORTION(): return 0.9
    @staticmethod
    def MESSAGES_FOR_SPAM(): return 5
    @staticmethod
    def MIN_MESSAGE_TIME(): return timedelta(milliseconds = 300) * ModerationHandler.MESSAGES_FOR_SPAM()
    @staticmethod
    def SPAM_INTERVAL(): return timedelta(seconds = 6)
    @staticmethod
    def toId(stuff): return re.sub(r'[^a-zA-Z0-9]', '', stuff).lower()

    # Static variables
    URL_REGEX = re.compile(r'\b(?:(?:(?:https?://|www[.])[a-z0-9\-]+(?:[.][a-z0-9\-]+)*|[a-z0-9\-]+(?:[.][a-z0-9\-]+)*[.](?:com?|org|net|edu|info|us|jp|[a-z]{2,3}(?=[:/])))(?:[:][0-9]+)?\b(?:/(?:(?:[^\s()<>]|[(][^\s()<>]*[)])*(?:[^\s`()<>\[\]{}\'".,!?;:]|[(][^\s()<>]*[)]))?)?|[a-z0-9.]+\b@[a-z0-9\-]+(?:[.][a-z0-9\-]+)*[.][a-z]{2,3})', flags = re.I)
    STRETCH_REGEX = re.compile(r'((.)\2{9,})|((..+)\4{5,})', flags = re.I)
    GROUP_REGEX = re.compile(r'(/groupchat-.+?-.+?\b)|(<<groupchat-.+?-.+?>>)', flags = re.I)
    InfractionScore = {
            'groupchat': 0,
            'caps': 1,
            'stretching': 1,
            'badlink': 2,
            'flooding': 3,
            'banword': 3,
            'roomban': 10
    }
    ActionReplies = {
            'groupchat': "Don't link groupchats in here please.",
            'caps': 'Would you mind not using caps so much, please.',
            'stretching': "Please don't stretch unnecessarily.",
            'badlink': 'The link has nothing to do with NU.',
            'flooding': "Don't spam, please :c",
            'banword': "You can't say that in here, so please don't.",
            'roomban': "You are banned from this room."
    }
    UrlShorteners = ["spo.ink","goo.my","0rz.tw","1link.in","1url.com","2.gp","2big.at","2tu.us","3.ly","307.to","4ms.me","4sq.com","4url.cc","6url.com","7.ly","a.gg","a.nf","aa.cx","abcurl.net","ad.vu","adf.ly","adjix.com","afx.cc","all.fuseurl.com","alturl.com","amzn.to","ar.gy","arst.ch","atu.ca","azc.cc","b23.ru","b2l.me","bacn.me","bcool.bz","binged.it","bit.ly","bizj.us","bloat.me","bravo.ly","bsa.ly","budurl.com","canurl.com","chilp.it","chzb.gr","cl.lk","cl.ly","clck.ru","cli.gs","cliccami.info","clickthru.ca","clop.in","conta.cc","cort.as","cot.ag","crks.me","ctvr.us","cutt.us","dai.ly","decenturl.com","dfl8.me","digbig.com","digg.com","disq.us","dld.bz","dlvr.it","do.my","doiop.com","dopen.us","easyuri.com","easyurl.net","eepurl.com","eweri.com","fa.by","fav.me","fb.me","fbshare.me","ff.im","fff.to","fire.to","firsturl.de","firsturl.net","flic.kr","flq.us","fly2.ws","fon.gs","freak.to","fuseurl.com","fuzzy.to","fwd4.me","fwib.net","g.ro.lt","gizmo.do","gl.am","go.9nl.com","go.ign.com","go.usa.gov","goo.gl","goshrink.com","gurl.es","hex.io","hiderefer.com","hmm.ph","href.in","hsblinks.com","htxt.it","huff.to","hulu.com","hurl.me","hurl.ws","icanhaz.com","idek.net","ilix.in","is.gd","its.my","ix.lt","j.mp","jijr.com","kl.am","klck.me","korta.nu","krunchd.com","l9k.net","lat.ms","liip.to","liltext.com","linkbee.com","linkbun.ch","liurl.cn","ln-s.net","ln-s.ru","lnk.gd","lnk.ms","lnkd.in","lnkurl.com","lru.jp","lt.tl","lurl.no","macte.ch","mash.to","merky.de","migre.me","miniurl.com","minurl.fr","mke.me","moby.to","moourl.com","mrte.ch","myloc.me","myurl.in","n.pr","nbc.co","nblo.gs","nn.nf","not.my","notlong.com","nsfw.in","nutshellurl.com","nxy.in","nyti.ms","o-x.fr","oc1.us","om.ly","omf.gd","omoikane.net","on.cnn.com","on.mktw.net","onforb.es","orz.se","ow.ly","ping.fm","pli.gs","pnt.me","politi.co","post.ly","pp.gg","profile.to","ptiturl.com","pub.vitrue.com","qlnk.net","qte.me","qu.tc","qy.fi","r.im","rb6.me","read.bi","readthis.ca","reallytinyurl.com","redir.ec","redirects.ca","redirx.com","retwt.me","ri.ms","rickroll.it","riz.gd","rt.nu","ru.ly","rubyurl.com","rurl.org","rww.tw","s4c.in","s7y.us","safe.mn","sameurl.com","sdut.us","shar.es","shink.de","shorl.com","short.ie","short.to","shortlinks.co.uk","shorturl.com","shout.to","show.my","shrinkify.com","shrinkr.com","shrt.fr","shrt.st","shrten.com","shrunkin.com","simurl.com","slate.me","smallr.com","smsh.me","smurl.name","sn.im","snipr.com","snipurl.com","snurl.com","sp2.ro","spedr.com","srnk.net","srs.li","starturl.com","su.pr","surl.co.uk","surl.hu","t.cn","t.co","t.lh.com","ta.gd","tbd.ly","tcrn.ch","tgr.me","tgr.ph","tighturl.com","tiniuri.com","tiny.cc","tiny.ly","tiny.pl","tinylink.in","tinyuri.ca","tinyurl.com","tk.","tl.gd","tmi.me","tnij.org","tnw.to","tny.com","to.","to.ly","togoto.us","totc.us","toysr.us","tpm.ly","tr.im","tra.kz","trunc.it","twhub.com","twirl.at","twitclicks.com","twitterurl.net","twitterurl.org","twiturl.de","twurl.cc","twurl.nl","u.mavrev.com","u.nu","u76.org","ub0.cc","ulu.lu","updating.me","ur1.ca","url.az","url.co.uk","url.ie","url360.me","url4.eu","urlborg.com","urlbrief.com","urlcover.com","urlcut.com","urlenco.de","urli.nl","urls.im","urlshorteningservicefortwitter.com","urlx.ie","urlzen.com","usat.ly","use.my","vb.ly","vgn.am","vl.am","vm.lc","w55.de","wapo.st","wapurl.co.uk","wipi.es","wp.me","x.vu","xr.com","xrl.in","xrl.us","xurl.es","xurl.jp","y.ahoo.it","yatuc.com","ye.pe","yep.it","yfrog.com","yhoo.it","yiyd.com","youtu.be","yuarel.com","z0p.de","zi.ma","zi.mu","zipmyurl.com","zud.me","zurl.ws","zz.gd","zzang.kr"]
    WhitelistedUrls = [
            'smogon.com','pokemonshowdown.com','.psim.us',
            'youtube.com','lmgtfy.com',
            'pastebin.com','hastebin.com',
            'puu.sh','i.imgur.com','prntscr.com','gyazo.com',
            'bulbapedia.bulbagarden.net','serebii.net'
    ]
    def __init__(self, config):
        self.roomtitle = config['room']
        self.config = config
        self.nextReset = datetime.now().date() + timedelta(days = 2)
        self.spamTracker = {}
        self.punishedUsers = {}
        self.banned = {}
        with open('plugins/bans.yaml', 'a+') as yf:
            yf.seek(0, 0)
            self.banned = yaml.load(yf)
            if not self.banned:
                self.banned = {}
            if self.roomtitle not in self.banned:
                self.banned[self.roomtitle] = {'phrase': [], 'user': []}
            self.banned = self.banned[self.roomtitle]

    def assignRoom(self, room):
        self.room = room

    def toggleRoomModeration(self):
        self.config['anything'] = not self.config['anything']

    def addBan(self, t, ban):
        if t == 'user':
            ban = ModerationHandler.toId(ban)
        else:
            ban = ban.lower()
        if ban in self.banned[t]:
                return '{} already banned in this room'.format(t)
        self.banned[t].append(ban)
        with open('plugins/bans.yaml', 'r') as yf:
            bans = yaml.load(yf)
            if not bans: bans = {}
            bans[self.roomtitle] = self.banned
        with open('plugins/bans.yaml', 'w') as yf:
            yaml.dump(bans, yf)

    def removeBan(self, t, ban):
        if t == 'user':
            ban = ModerationHandler.toId(ban)
        else:
            ban = ban.lower()
        if ban not in self.banned[t]:
                return '{} not banned'.format(t)
        self.banned[t].remove(ban)
        with open('plugins/bans.yaml', 'r') as yf:
            bans = yaml.load(yf)
            if not bans: bans = {}
            bans[self.roomtitle] = self.banned
        with open('plugins/bans.yaml', 'w') as yf:
            yaml.dump(bans, yf)

    def shouldBan(self, user):
        return self.isBannedFromRoom(user)
    def isBannedFromRoom(self, user):
        return user.name in self.banned['user']

    def recentlyPunished(self, user, now):
        if user.id not in self.punishedUsers:
            return False
        timeDiff = now - self.punishedUsers[user.id].lastPunished
        return timeDiff < timedelta(seconds = 3)


    def getUrl(self, text):
        match = re.search(ModerationHandler.URL_REGEX, text.replace(' ',''))
        if match:
            return match.group(0)
        else:
            return False
    def containUrl(self, msg):
        if self.getUrl(msg):
            return True
        return False
    def badLink(self, link):
        if any(u in link for u in ModerationHandler.UrlShorteners):
            if not link.startswith('http://'): link = 'http://' + link
            resp = urllib.request.urlopen(link)
            if 200 <= resp.getcode() > 400:
                link = resp.url()
            else:
                return False
        if not any(u in link for u in ModerationHandler.WhitelistedUrls):
            if not link.startswith('http://'): link = 'http://' + link
            if 'youtube.com' in link:
                # check youtube links better than the others because videos might still
                # be inappropriate, even if YouTube isn't
                pass
            return True
        return False

    def isBanword(self, msg):
        for ban in self.banned['phrase']:
            if ban.lower() in msg:
                return True
        return False
    def isSpam(self, msg, user, now):
        if user.id not in self.spamTracker:
            self.spamTracker[user.id] = deque('', 50)
        self.spamTracker[user.id].append(now)
        times = self.spamTracker[user.id]
        timesLen = len(times)
        if timesLen < ModerationHandler.MESSAGES_FOR_SPAM(): return False
        timeDiff = now - times[timesLen - ModerationHandler.MESSAGES_FOR_SPAM()]
        if timeDiff <= ModerationHandler.SPAM_INTERVAL() and timeDiff > ModerationHandler.MIN_MESSAGE_TIME():
        # For it to be spam, the following conditions has to be met:
        # 1: At least 5 messages in the last 6 seconds
        # 2: At least 300ms between every message
            return True
        return False
    def isStretching(self, msg, users):
        for user in users:
            # If a username trigger the stretching, remove the username from the message
            # to stop malicious usernames
            if re.search(ModerationHandler.STRETCH_REGEX, user):
                msg = msg.replace(user, '')
            if re.search(ModerationHandler.STRETCH_REGEX, users[user].name):
                msg = msg.replace(users[user].name, '')

        if re.search(ModerationHandler.STRETCH_REGEX, msg):
            return True
        return False
    def isCaps(self, msg, users):
        # To make sure no username triggers this, replace them with empty strings before
        # doing the actual check
        for user in users:
            msg = msg.replace(users[user].name, '')
        capsCount = len(re.findall(r'[A-Z]', re.sub(r'[^A-Za-z]', '', msg)))
        return capsCount and len(re.sub(r' ','',msg)) > ModerationHandler.MIN_CAPS_LENGTH() and capsCount >= int(len(re.sub(r' ','',msg)) * ModerationHandler.CAPS_PROPORTION())
    def isGroupMention(self, msg):
        if re.search(ModerationHandler.GROUP_REGEX, msg):
            return True
        return False

    def getAction(self, room, user, wrong, unixTime):
        # This assumes unixTime is a valid unix timestamp
        now = datetime.utcfromtimestamp(int(unixTime))

        if user.id not in self.punishedUsers:
            self.punishedUsers[user.id] = PunishedUser(user.id, ModerationHandler.InfractionScore[wrong], now)
        else:
            self.punishedUsers[user.id].points += ModerationHandler.InfractionScore[wrong]
            self.punishedUsers[user.id].lastPunished = now

        score =  self.punishedUsers[user.id].points
        action = ''
        # Under 3 points are low and warning is enough
        if score < 3:
            action = 'warn'
        # Under 6 points is moderately bad and should be punished
        # For minor things, this will lead to a lot of mutes before hourmuting happens
        elif score < 6:
            action = 'mute'
        # Under 9 points and you're just an awful user and rulebreaker
        # Even minor action will get to hourmutes eventually
        elif score < 9:
            action = 'hourmute'
        # Just ban them then...
        else:
            action = 'roomban'
        # If the current rank doesn't support roomban, keep muting them
        if action == 'roomban' and room.botHasBanPermission():
            action = 'hourmute'
        self.punishedUsers[user.id].lastAction = action
        return action, ModerationHandler.ActionReplies[wrong]

    def shouldAct(self, msg, user, unixTime):
        now = datetime.utcfromtimestamp(int(unixTime))
        # Clear the punishment scores every two days
        if now.date() >= self.nextReset:
            self.punishedUsers.clear()
            self.nextReset = now.date() + timedelta(days = 2)

        if self.config['anything'] and self.isBannedFromRoom(user):
            return 'roomban'
        if self.config['spam'] and self.isSpam(msg, user, now):
            return 'flooding'
        if self.config['banword'] and self.isBanword(msg.lower()):
            return 'banword'
        if self.recentlyPunished(user, now):
            return False
        if self.config['stretching'] and self.isStretching(msg, self.room.users):
            return 'stretching'
        if self.config['caps'] and self.isCaps(msg, self.room.users):
            return 'caps'
        if self.config['groupchats'] and self.isGroupMention(msg):
            return 'groupchat'
        if self.config['urls'] and self.containUrl(msg.lower()):
            url = self.getUrl(msg[4])
            if self.badLink(url):
                return 'badlink'
        return False


# Commands
def moderate(bot, cmd, msg, user, room):
    reply = ReplyObject('', True)
    if not msg: return reply.response('No parameters given. Command is ~moderate [room],True/False')
    if not user.hasRank('#'): return reply.response('You do not have permission to set this. (Requires #)')
    if not room.moderation.config['anything'] and not msg == 'anything': room.moderation.toggleRoomModeration()
    room.moderation.config[msg] = not room.moderation.config[msg]
    return reply.response('Moderation for {thing} is now turned {setting}'.format(thing = msg, setting = 'on' if room.moderation.config[msg] else 'off'))

def banthing(bot, cmd, msg, user, room):
    reply = ReplyObject('', True, True)
    if not user.hasRank('#'): return reply.response('You do not have permission to do this. (Requires #)')
    if room.isPM: return reply.response("You can't ban things in PMs")
    error = room.moderation.addBan(cmd[3:], msg)
    if not error:
        modnote = '/modnote {user} added {thing} to the blacklist'.format(thing = msg, user = user.name)
        ban = ''
        if msg in room.users:
            ban = '\n/roomban {user}, Was added to blacklist'.format(user = msg)
        return reply.response('Added {thing} to the banlist\n{note}{act}'.format(thing = msg, user = user.name, note = modnote, act = ban))
    return reply.response(error)

def unbanthing(bot, cmd, msg, user, room):
    reply = ReplyObject('', True, True)
    if not user.hasRank('#'): return reply.response('You do not have permission to do this. (Requires #)')
    if room.isPM: return reply.response("You can't unban things in PMs")
    error = room.moderation.removeBan(cmd[5:], msg)
    if not error:
        return reply.response('Removed {thing} from the banlist {room}\n/modnote {user} removed {thing} from the blacklist'.format(thing = msg, room = room.title, user = user.name))
    return reply.response(error)

commands = [
    Command(['moderate'], moderate),
    Command(['banuser', 'banphrase'], banthing),
    Command(['unbanuser', 'unbanphrase'], unbanthing)
]