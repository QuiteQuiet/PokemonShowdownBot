Commands
========

Every command is prefaced with ~, to separate it from regular chat. If the broadcast setting is
higher than your current auth level, you will get a message prompting you to re-enter the command through PM.

Standard commands
-----------------

- pick a,b,c,d... : Randomly selects one of the entered options.
- [tier]poke : Randomly selects one Pokémon from the viable tier list from [tier]. Supported tiers are Uber, OU, UU, RU, NU, PU, and LC.
- [tier]team : Randomly generate a team that is usable in [tier]. Same restrictions as [tier]poke apply.
- [pokemon] : Entering any existing pokemon (for example ~kyogre) gives a link to their respective Smogon analysis page.
- commands : Gives a link to this page.
- hangman new, [room], [phrase] : Use hangman new, [room], [phrase] to create a hangman game in [room], with the solution being [phrase]. Forcefully end an ongoing hangman game with hangman end.
- hg : Only usable with the above command, hg [letter/phrase] is used to play games of hangman and accepts either a single letter or phrases as guesses.

Extended commands
-----------------

These commands are based on some form of moderating purpose,
and as such require global or roomauth of some degree.

- broadcast : Show the current required rank to broadcast command returns.
- setbroadcast : Set the level required to broadcast. This is a global setting and not tied to single rooms.
- allowgames [room], True/False : Enable or disable the chatgames in [room]
- whitelist : Print the current whitelist that gains extended permissions above their current auth rank (currently unsupported)
