Plugins
=======

Plugins include anything that isn't a regular feature such as battles, tournaments, and chat games.
They are structured as standalone programs created by the main chat application, and should to some degree controll
the behavior of the main application in such a way that it does not interfere with other features curently running.

Chat games
----------

Chat games like hangman are supported by one game at a time. No two games can be started at once, both for safety but also to restrict memory usage. Any additional chat games also have to adhere to this rule, but can, if such features are added, run simultaneously to other functions like tournament play.

Tournaments
-----------

Tournaments in any of the supported formats will be joined if the following conditions are met:
- The tournament start after the bot enter the room.
- The tournament format is among the supported formats (see below).
- The option to join tournamets is enabled.

Currently only Challenge Cup 1v1 is supported.