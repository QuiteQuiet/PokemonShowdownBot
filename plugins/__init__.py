from plugins import moderation
from plugins import tournaments
from plugins import messages
from plugins import workshop
from plugins import anagram
from plugins.battling import battleHandler

# This is where you pick what the name of the command actually is, then map it to a function.
# Every command needs a function to work, with the parameters (bot, cmd, room, msg, user)
# in that order.
PluginCommands = {
    'moderate'      : moderation.moderate,
    'banuser'       : moderation.banthing,
    'banphrase'     : moderation.banthing,
    'unbanuser'     : moderation.unbanthing,
    'unbanphrase'   : moderation.unbanthing,
    'oldgentour'    : tournaments.oldgentour,
    'showranking'   : tournaments.getranking,
    'tell'          : messages.tell,
    'read'          : messages.read,
    'untell'        : messages.untell,
    'workshop'      : workshop.handler,
    'ws'            : workshop.handler,
    'anagram'       : anagram.start,
    'a'             : anagram.answer,
    'storeteam'     : battleHandler.acceptTeam
}