Commands
========

Every command is prefaced with ~, to separate it from regular chat. If the broadcast setting is
higher than your current auth level, you will get a message prompting you to re-enter the command through PM.

Standard commands
-----------------

- commands : Gives a link to this page.
- source : Prints a link to this github repository.
- pick a,b,c,d... : Randomly selects one of the entered options.

- [tier]poke : Randomly selects one Pokémon from the viable tier list from [tier]. Supported tiers are Uber, OU, UU, RU, NU, PU, and LC. 
- [tier]team : Randomly generate a team that is usable in [tier]. Same restrictions as [tier]poke apply.
- [pokemon] : Entering any existing pokemon (for example ~kyogre) gives a link to their respective Smogon analysis page.
- [tier] : Similar to the above, entering any official Smogon tier (such as ~ou) brings up a link to the Smogon hub for that tier.

- ~viability [tier], ~speedtiers [tier], ~np [tier], ~sample [tier] :
- The above four commands bring up their respective forums resource that was requested (if one exists). Supported tiers are Uber, OU, UU, RU, NU, PU, and LC.

Chat Games
----------
These commands are only allowed after relevant part enbling them through the allowgames command, and then it's only enabled for a single room. Only one of these can be played at any point, which is shared across all rooms it's currently in.

Hangman
- hangman new, [room], [phrase] : Use hangman new, [room], [phrase] to create a hangman game in [room], with the solution being [phrase]. Forcefully end an ongoing hangman game with hangman end.
- hg : Only usable with the above command, hg [letter/phrase] is used to play games of hangman and accepts either a single letter or phrases as guesses.

Anagram
- anagram new : Generates a new anagram from a Pokémon or a move.
- anagram hint : Display the hint for the current anagram
- anagram end : Forcefully ends the current game, revealing the solution
- a : Guess the solution. Everything after a is treated as the guess.

Extended commands
-----------------

These commands are based on some form of moderating purpose,
and as such require global or roomauth of some degree.

- broadcast : Show the current required rank to broadcast command returns.
- setbroadcast : Set the level required to broadcast. This is a global setting and not tied to single rooms.
- allowgames [room], True/False : Enable or disable the chatgames in [room]
- whitelist : Print the current whitelist that allow regular users the ability to broadcast commands.
- whitelistadd [user]: Add a user to the whitelist.
- removewl [user]: Remove a user from the whitelist.
