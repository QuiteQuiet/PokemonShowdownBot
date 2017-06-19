[![Build Status](https://travis-ci.org/QuiteQuiet/PokemonShowdownBot.svg?branch=master)](https://travis-ci.org/QuiteQuiet/PokemonShowdownBot)

Pokemon Showdown Bot made in Python 3.4

Detailed information can be found in the respective files.

Structure
---------

The Showdown bot is built from three components:

- app.py which contains PSBot(), the central network, and is where most of the connections to other pieces of the app is created.
- The class PSBot is extended from the base class PokemonShowdownBot found in robot.py, and contain almost all basic functions that are required for the bot to function. Most of the more general functions like join, leave and say are defined here.
- The third file this rely on is room.py, as every room joined creats a new room object that store important information for the bot, such as userlists and allowed uses.

Setting up
----------
#### Python version:
- Python 3.4.2 (Supposedly works with 2.7 versions of the libraries too, but cannot confirm)

#### Guide:
1. Clone the git repo to your desired location
2. Use `pip install requirements.txt` to get relevant modules for the project
3. Follow the instructions in `details-example.py` to configure it
4. Run using `python app.py` (or `python3 app.py` if you have both versions installed)

License
-------

This is distributed under the terms of the [MIT License][1].

  [1]: https://github.com/QuiteQuiet/PokemonShowdownBot/blob/master/LICENCE

Credits
-------

Owner

- Quite Quiet
