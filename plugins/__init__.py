from plugins import moderation
from plugins import tournaments
from plugins import messages
from plugins import workshop
from plugins import anagram

PluginCommands = [
    moderation.commands,
    tournaments.commands,
    messages.commands,
    workshop.commands,
    anagram.commands
]