import re
from datetime import datetime, timedelta
from urllib.request import urlopen

urlShorteners = ["spo.ink","goo.my","0rz.tw","1link.in","1url.com","2.gp","2big.at","2tu.us","3.ly","307.to","4ms.me","4sq.com","4url.cc","6url.com","7.ly","a.gg","a.nf","aa.cx","abcurl.net","ad.vu","adf.ly","adjix.com","afx.cc","all.fuseurl.com","alturl.com","amzn.to","ar.gy","arst.ch","atu.ca","azc.cc","b23.ru","b2l.me","bacn.me","bcool.bz","binged.it","bit.ly","bizj.us","bloat.me","bravo.ly","bsa.ly","budurl.com","canurl.com","chilp.it","chzb.gr","cl.lk","cl.ly","clck.ru","cli.gs","cliccami.info","clickthru.ca","clop.in","conta.cc","cort.as","cot.ag","crks.me","ctvr.us","cutt.us","dai.ly","decenturl.com","dfl8.me","digbig.com","digg.com","disq.us","dld.bz","dlvr.it","do.my","doiop.com","dopen.us","easyuri.com","easyurl.net","eepurl.com","eweri.com","fa.by","fav.me","fb.me","fbshare.me","ff.im","fff.to","fire.to","firsturl.de","firsturl.net","flic.kr","flq.us","fly2.ws","fon.gs","freak.to","fuseurl.com","fuzzy.to","fwd4.me","fwib.net","g.ro.lt","gizmo.do","gl.am","go.9nl.com","go.ign.com","go.usa.gov","goo.gl","goshrink.com","gurl.es","hex.io","hiderefer.com","hmm.ph","href.in","hsblinks.com","htxt.it","huff.to","hulu.com","hurl.me","hurl.ws","icanhaz.com","idek.net","ilix.in","is.gd","its.my","ix.lt","j.mp","jijr.com","kl.am","klck.me","korta.nu","krunchd.com","l9k.net","lat.ms","liip.to","liltext.com","linkbee.com","linkbun.ch","liurl.cn","ln-s.net","ln-s.ru","lnk.gd","lnk.ms","lnkd.in","lnkurl.com","lru.jp","lt.tl","lurl.no","macte.ch","mash.to","merky.de","migre.me","miniurl.com","minurl.fr","mke.me","moby.to","moourl.com","mrte.ch","myloc.me","myurl.in","n.pr","nbc.co","nblo.gs","nn.nf","not.my","notlong.com","nsfw.in","nutshellurl.com","nxy.in","nyti.ms","o-x.fr","oc1.us","om.ly","omf.gd","omoikane.net","on.cnn.com","on.mktw.net","onforb.es","orz.se","ow.ly","ping.fm","pli.gs","pnt.me","politi.co","post.ly","pp.gg","profile.to","ptiturl.com","pub.vitrue.com","qlnk.net","qte.me","qu.tc","qy.fi","r.im","rb6.me","read.bi","readthis.ca","reallytinyurl.com","redir.ec","redirects.ca","redirx.com","retwt.me","ri.ms","rickroll.it","riz.gd","rt.nu","ru.ly","rubyurl.com","rurl.org","rww.tw","s4c.in","s7y.us","safe.mn","sameurl.com","sdut.us","shar.es","shink.de","shorl.com","short.ie","short.to","shortlinks.co.uk","shorturl.com","shout.to","show.my","shrinkify.com","shrinkr.com","shrt.fr","shrt.st","shrten.com","shrunkin.com","simurl.com","slate.me","smallr.com","smsh.me","smurl.name","sn.im","snipr.com","snipurl.com","snurl.com","sp2.ro","spedr.com","srnk.net","srs.li","starturl.com","su.pr","surl.co.uk","surl.hu","t.cn","t.co","t.lh.com","ta.gd","tbd.ly","tcrn.ch","tgr.me","tgr.ph","tighturl.com","tiniuri.com","tiny.cc","tiny.ly","tiny.pl","tinylink.in","tinyuri.ca","tinyurl.com","tk.","tl.gd","tmi.me","tnij.org","tnw.to","tny.com","to.","to.ly","togoto.us","totc.us","toysr.us","tpm.ly","tr.im","tra.kz","trunc.it","twhub.com","twirl.at","twitclicks.com","twitterurl.net","twitterurl.org","twiturl.de","twurl.cc","twurl.nl","u.mavrev.com","u.nu","u76.org","ub0.cc","ulu.lu","updating.me","ur1.ca","url.az","url.co.uk","url.ie","url360.me","url4.eu","urlborg.com","urlbrief.com","urlcover.com","urlcut.com","urlenco.de","urli.nl","urls.im","urlshorteningservicefortwitter.com","urlx.ie","urlzen.com","usat.ly","use.my","vb.ly","vgn.am","vl.am","vm.lc","w55.de","wapo.st","wapurl.co.uk","wipi.es","wp.me","x.vu","xr.com","xrl.in","xrl.us","xurl.es","xurl.jp","y.ahoo.it","yatuc.com","ye.pe","yep.it","yfrog.com","yhoo.it","yiyd.com","youtu.be","yuarel.com","z0p.de","zi.ma","zi.mu","zipmyurl.com","zud.me","zurl.ws","zz.gd","zzang.kr"]
whitelistedUrls = [
    'smogon.com','pokemonshowdown.com','.psim.us',
    'youtube.com','lmgtfy.com',
    'pastebin.com','hastebin.com',
    'puu.sh','i.imgur.com','prntscr.com','gyazo.com',
    'bulbapedia.bulbagarden.net','serebii.net'
    ]
# Important regexes
URL_REGEX = re.compile(r'\b(?:(?:(?:https?://|www[.])[a-z0-9\-]+(?:[.][a-z0-9\-]+)*|[a-z0-9\-]+(?:[.][a-z0-9\-]+)*[.](?:com?|org|net|edu|info|us|jp|[a-z]{2,3}(?=[:/])))(?:[:][0-9]+)?\b(?:/(?:(?:[^\s()<>]|[(][^\s()<>]*[)])*(?:[^\s`()<>\[\]{}\'".,!?;:]|[(][^\s()<>]*[)]))?)?|[a-z0-9.]+\b@[a-z0-9\-]+(?:[.][a-z0-9\-]+)*[.][a-z]{2,3})', flags = re.I)
STRETCH_REGEX = re.compile(r'((.)\2{7,})|((..+)\4{4,})', flags = re.I)

# Importat variables
spamTracker = {}
infractionScore = {
    'caps': 1,
    'stretching': 1,
    'badlink': 2,
    'flooding': 3,
    'banword': 3
}
punishedUsers = {}
bannedPhrases = [
    'sd*skarmory fuckin spanked pokeaim in this ubers match'
    ]
actionReplies = {
        'caps': 'Would you mind not using caps so much, please.',
        'stretching': "Please don't stretch words unnecessarily.",
        'badlink': 'The link has nothing to do with NU.',
        'flooding': "Please type slower and don't spam.",
        'banword': "You can't say that in here, so please don't."
    }
# Constants
def MIN_CAPS_LENGTH(): return 12
def CAPS_PROPORTION(): return 0.8
def MESSAGES_FOR_SPAM(): return 5
def MIN_MESSAGE_TIME(): return timedelta(milliseconds = 300) * MESSAGES_FOR_SPAM()
def SPAM_INTERVAL(): return timedelta(seconds = 6)

def canPunish(self, room): return self.Groups[self.details['rooms'][room].rank] >= self.Groups['%']
def canBan(self, room): return self.Groups[self.details['rooms'][room].rank] >= self.Groups['@']

# User Punishment Class
class PunishedUser:
    def __init__(self, name, score, now):
        self.name = name
        self.points = score
        self.lastPunished = now
        self.lastAction = ''
# Everything else
def getUrl(text):
    match = re.search(URL_REGEX, text.replace(' ',''))
    if match:
        return match.group(0)
    else:
        return False

def containUrl(msg):
    if getUrl(msg):
        return True
    return False

def badLink(link):
    if any(u in link for u in urlShorteners):
        if not link.startswith('http://'): link = 'http://' + link
        resp = urlopen(link)
        if 200 <= resp.getcode() > 400:
            link = resp.url()
        else:
            return False
    if not any(u in link for u in whitelistedUrls):
        if not link.startswith('http://'): link = 'http://' + link
        if 'youtube.com' in link:
            # check youtube links better than the others
            pass
        return True
    return False
def recentlyPunished(user, now):
    if user['name'] not in punishedUsers:
        return False
    timeDiff = now - punishedUsers[user['name']].lastPunished
    return timeDiff > timedelta(seconds = 3)
def isBanword(msg):
    for ban in bannedPhrases:
        if ban.lower() in msg:
            return True
    return False
def isSpam(msg, user, room, now):
    if room not in spamTracker:
        spamTracker[room] = {}
    if user['name'] not in spamTracker[room]:
        # The first time this user have talked, so there's no way it's spam now
        spamTracker[room][user['name']] = []
        return False
    spamTracker[room][user['name']].append(now)
    times = spamTracker[room][user['name']]
    timesLen = len(times)
    if timesLen < MESSAGES_FOR_SPAM():
         return False
    timeDiff = now - times[timesLen - MESSAGES_FOR_SPAM()]
    if (
      timesLen >= MESSAGES_FOR_SPAM() and
      timeDiff < SPAM_INTERVAL() and
      timeDiff > MIN_MESSAGE_TIME()
    ):
    # For it to be spam, the following conditions has to be met:
    # 1: At least 5 messages in the last 6 seconds
    # 2: At least 300ms between every message
        return True
    return False
def isStretching(msg):
    if re.match(STRETCH_REGEX, msg):
        return True
    return False
def isCaps(msg):
    capsCount = len(re.findall(r'[A-Z]', re.sub(r'[^A-Za-z]', '', msg)))
    return capsCount and len(re.sub(r' ','',msg)) > MIN_CAPS_LENGTH() and capsCount >= int(len(re.sub(r' ','',msg)) * CAPS_PROPORTION())
def getAction(user, wrong, unixTime):
    # This assumes unixTime is a valid unix timestamp
    now = datetime.utcfromtimestamp(int(unixTime))
    # Judge users based on their past behavior
    if user['name'] not in punishedUsers:
        punishedUsers[user['name']] = PunishedUser(user['name'], infractionScore[wrong], now)
    else:
        punishedUsers[user['name']].points += infractionScore[wrong]
        punishedUsers[user['name']].lastPunished = now

    score =  punishedUsers[user['name']].points
    action = ''
    # Under 3 points are low and warning is enough
    if score < 3:
        action = 'warn'
    # Under 6 points is moderately bad and should be punished
    # For minor things, this will lead to a lot of mutes before hourmuting happens
    elif score < 6:
        action = 'mute'
    # Under 9 points and you're just an awfl user and rulebreaker
    # Even minor action will get to hourmutes eventually
    elif score < 9:
        action = 'hourmute'
    # Just ban them then...
    else:
        action = 'roomban'
    punishedUsers[user['name']].lastAction = action
    return action, actionReplies[wrong]
        
def shouldAct(msg, user, room, unixTime):
    now = datetime.utcfromtimestamp(int(unixTime))
    if recentlyPunished(user, now):
        return False
    if isBanword(msg.lower()):
        return 'banword'
    if isSpam(msg, user, room, now):
        return 'flooding'
    if isStretching(msg):
        return 'stretching'
    if isCaps(msg):
        return 'caps'
    if containUrl(msg.lower()):
        return False # Ignore urls for now
        url = moderation.getUrl(message[4])
        if moderation.badLink(url):
            if self.Groups[user['group']] >= self.Groups['%']: return False
            return 'badlink'
    return False
    
