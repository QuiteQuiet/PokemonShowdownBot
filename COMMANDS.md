Commands
========

Every command is prefaced with ~, to separate it from regular chat. If the broadcast setting is
higher than your current auth level, you will get a message prompting you to re-enter the command through PM.

Standard commands
-----------------

- `commands` : Gives a link to this page.
- `source` : Prints a link to this github repository.
- `pick a, b, c, d...` : Randomly selects one of the entered options.

- `[tier]poke` : Randomly selects one Pokémon from the viable tier list from [tier]. Supported tiers are Uber, OU, UU, RU, NU, PU, and LC.
- `[tier]team` : Randomly generate a team that is usable in [tier]. Same restrictions as [tier]poke apply.
- `team [tier]` : Select a random sample team in [tier], with the same restrictions as the above two.
- `pokemon` : Entering any existing pokemon (for example ~kyogre) gives a link to their respective Smogon analysis page.
- `tier` : Similar to the above, entering any official Smogon tier (such as ~ou) brings up a link to the Smogon hub for that tier.

- `~vr [tier]`, `~speedtiers [tier]`, `~np [tier]`, `~sample [tier]`, `~roles [tier]` :
- The above five commands bring up their respective forum resource that was requested (if one exists). Supported tiers are Uber, OU, UU, RU, NU, PU, and LC.

- `tell [user], [message]` : This will save [message], and when [user] join any room the bot is in, they will get a PM notifying them they have a message waiting. Messages are not saved on a restart, and you can only have one message to each user waiting at any time.
- `read [number]` : Returns [number] messages that you have waiting. If you have no messages it returns nothing, and if [number] is larger than your waiting messages, all of them are returned.
- `removetell [user]` : Remove your waiting message to [user], if one exists.

Chat Games
----------
These commands are only allowed after relevant part enbling them through the allowgames command, and then it's only enabled for a single room. Only one of these can be played per room, so to play something else the first game has to end.

#### Anagram ####
- `anagram new` : Generates a new anagram from a Pokémon or a move.
- `anagram hint` : Display the hint for the current anagram
- `anagram end` : Forcefully ends the current game, revealing the solution
- Doing `~anagram` without any parameter prints out the current anagram if one exists.
- `a` : Guess the solution. Everything after a is treated as the guess.

#### Trivia ####
Trivia is played in a 30 second guessing period and a 5 second wait between every question. Answers are only accepted during the answering period
and not before or after. Games can be stopped at any point during either period.
- `trivia start` : Begin a selfrepeating trivia session that will continue until cancelled.
- `trivia end/stop` : Stop the ongoing trivia session.
- `ta` : Guess on the current question. This doesn't give a reply until after the time runs out.

#### Workshops ####
Although not a chatgame, the workshop command use the same container as they do and as such cannot be used if a game is in progress. Similarly, no chat games can be started during a workshop. Do note that the config option about chat games does not apply to workshops.
- `workshop new [name]` : Starts a new workshop session with [name] as the host. If [name] is blank, the person doing the command is set as host.
- `workshop add [anything]` : Adds [anything] to the current workshop team. There's no checking if [anything] exists, so that's up to the host. (Requires Host or @)
- `workshop remove [anything]` : Removes [anything] if its in the team. Otherwise the same conditions as add.
- `workshop team` : Displays the current workshop team. (Requires Host or @)
- `workshop clear` : Deletes the workshop team. (Requires Host or @)
- `workshop end` : Ends the workshop session, deleting the team as well. (Requires Host or @)
- `ws` is an alias for `workshop`, for lazy people.

Extended commands
-----------------

These commands are based on some form of moderating purpose,
and as such require global or roomauth of some degree.

- `broadcast` : Show the current required rank to broadcast command returns.
- `setbroadcast` : Set the level required to broadcast. This is a global setting and not tied to single rooms.
- `allowgames` True/False : Enable or disable the chatgames in the current room.
- `[un]banuser [user]` : Room[un]bans [user] from any room the bot moderate.
- `[un]banphrase [phrase]` : [un]Bans [phrase] in every room the bot moderate.

None of the above commands save the current settings, and will be cleared on a restart. To save settings, use `savedetails`, which save everything currently in details (including games and battles for now).

#### Tournament Whitelisting ####
Users can be added to a room specific whitelist that allows them to start tours in that specific room, as long as the bot has the rank required to start tournaments itself.
- `tourwl [name]` : Add [name] to the whitelist for this room, as long as they're not on the list already.
- `untourwl [name]` : Remove [name] from the whitelist for this room.
- `tour [message]` : Pipes everything in [message] and outputs `/tour [message]`. (`/tour` syntax required for anything to work)

#### Event Scheduling ####
The chatbot can be scheduled to run a specific set of commands at some point in the future, once or on an user-defined interval. This can be configured on a per-room basis by Room Owners for an unlimited (not really, but within reason it practically is) set of scheduled jobs.

- `initevents`: Has to be done prior to scheduling any form of job execution. It sets up some important context that is needed for any job that will run.
- `addevent [time]|[periodicity]|[job]`: Adds a new event that will have its first execution at [time], and will then repeat once every [periodicity] days. It currently only allows you to specify periodicity by days. [time] can only be specified in the exact format: `YYYY/MM/DD HH:MM` with a 24 hour clock and GMT+0 as timezone. At [time] it will execute all instruction in [job]. This can either be a simple command such as `/rank chaos` or a more complex set of instructions. [jobs] can also be set of instruction in a paste from an url that the `PasteImporter` supports (hastebin.com/raw/, pastebin.com/raw/, or gist.githubusercontent.com/). It will read and interpret each line as its own command in this case.

#### Leaderboards ####
Each room is recording the result of all tours that happen; how many participants, who won, how many games each person has played. This is all collected to an all-time leaderboard that can be displayed, or for a specific user.

- `leaderboard [room], [format], [user]`: Display the [room] leaderboard for [format], or the stats for the single [user] in [format]. [room] and [user] are optional, and if ommited will use the current room and no user.

#### Official Tournaments  ####
Each room can specify a set of formats that will be considered 'official' formats of that room. All tournaments started of that format will be recorded to a separate leaderboard that will be displayed after each tour has finished. This leaderboard can be reset at any point. This will have no impact on the all-time leaderboard, they will coexist independently of each other.

- `addofficial [format]`: Mark [format] as an official format for the room.
- `officialleaderboard`: Same parameters as `leaderboard`.
- `resetofficials`: Clear all data for official tournaments.
- `excludetour`: Exclude a tour that would otherwise have been official from counting towards the official leaderboard.