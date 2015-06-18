Moves = {
    "absorb": {
        "accuracy": 100,
        "basePower": 20,
        "category": "Special",
        "pp": 25,
        "priority": 0,
        "flags": {"protect", "mirror", "heal"},
        "drain": [1, 2],
        "secondary": False,
        "target": "normal",
        "type": "Grass"
    },
    "acid": {
        "accuracy": 100,
        "basePower": 40,
        "category": "Special",
        "pp": 30,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": {
            "chance": 10,
            "boosts": {
                "spd": -1
            }
        },
        "target": "allAdjacentFoes",
        "type": "Poison"
    },
    "acidarmor": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 20,
        "priority": 0,
        "flags": {"snatch"},
        "boosts": {
            "def": 2
        },
        "secondary": False,
        "target": "self",
        "type": "Poison"
    },
    "acidspray": {
        "accuracy": 100,
        "basePower": 40,
        "category": "Special",
        "pp": 20,
        "priority": 0,
        "flags": {"bullet", "protect", "mirror"},
        "secondary": {
            "chance": 100,
            "boosts": {
                "spd": -2
            }
        },
        "target": "normal",
        "type": "Poison"
    },
    "acrobatics": {
        "accuracy": 100,
        "basePower": 55,
        "category": "Physical",
        "pp": 15,
        "priority": 0,
        "flags": {"contact", "protect", "mirror", "distance"},
        "secondary": False,
        "target": "any",
        "type": "Flying"
    },
    "acupressure": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 30,
        "priority": 0,
        "flags": {},
        "secondary": False,
        "target": "adjacentAllyOrSelf",
        "type": "Normal"
    },
    "aerialace": {
        "accuracy": True,
        "basePower": 60,
        "category": "Physical",
        "pp": 20,
        "priority": 0,
        "flags": {"contact", "protect", "mirror", "distance"},
        "secondary": False,
        "target": "any",
        "type": "Flying"
    },
    "aeroblast": {
        "accuracy": 95,
        "basePower": 100,
        "category": "Special",
        "pp": 5,
        "priority": 0,
        "flags": {"protect", "mirror", "distance"},
        "critRatio": 2,
        "secondary": False,
        "target": "any",
        "type": "Flying"
    },
    "afteryou": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 15,
        "priority": 0,
        "flags": {"authentic"},
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "agility": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 30,
        "priority": 0,
        "flags": {"snatch"},
        "boosts": {
            "spe": 2
        },
        "secondary": False,
        "target": "self",
        "type": "Psychic"
    },
    "aircutter": {
        "accuracy": 95,
        "basePower": 60,
        "category": "Special",
        "pp": 25,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "critRatio": 2,
        "secondary": False,
        "target": "allAdjacentFoes",
        "type": "Flying"
    },
    "airslash": {
        "accuracy": 95,
        "basePower": 75,
        "category": "Special",
        "pp": 15,
        "priority": 0,
        "flags": {"protect", "mirror", "distance"},
        "secondary": {
            "chance": 30,
            "volatileStatus": 'flinch'
        },
        "target": "any",
        "type": "Flying"
    },
    "allyswitch": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 15,
        "priority": 1,
        "flags": {},
        "secondary": False,
        "target": "self",
        "type": "Psychic"
    },
    "amnesia": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 20,
        "priority": 0,
        "flags": {"snatch"},
        "boosts": {
            "spd": 2
        },
        "secondary": False,
        "target": "self",
        "type": "Psychic"
    },
    "ancientpower": {
        "accuracy": 100,
        "basePower": 60,
        "category": "Special",
        "pp": 5,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": {
            "chance": 10,
            "self": {
                "boosts": {
                    "atk": 1,
                    "def": 1,
                    "spa": 1,
                    "spd": 1,
                    "spe": 1
                }
            }
        },
        "target": "normal",
        "type": "Rock"
    },
    "aquajet": {
        "accuracy": 100,
        "basePower": 40,
        "category": "Physical",
        "pp": 20,
        "priority": 1,
        "flags": {"contact", "protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Water"
    },
    "aquaring": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 20,
        "priority": 0,
        "flags": {"snatch"},
        "volatileStatus": 'aquaring',
        "secondary": False,
        "target": "self",
        "type": "Water"
    },
    "aquatail": {
        "accuracy": 90,
        "basePower": 90,
        "category": "Physical",
        "pp": 10,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Water"
    },
    "armthrust": {
        "accuracy": 100,
        "basePower": 15,
        "category": "Physical",
        "pp": 20,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "multihit": [2, 5],
        "secondary": False,
        "target": "normal",
        "type": "Fighting"
    },
    "aromatherapy": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 5,
        "priority": 0,
        "flags": {"snatch", "distance"},
        "secondary": False,
        "target": "allyTeam",
        "type": "Grass"
    },
    "aromaticmist": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 20,
        "priority": 0,
        "flags": {"authentic"},
        "boosts": {
            "spd": 1
        },
        "secondary": False,
        "target": "adjacentAlly",
        "type": "Fairy"
    },
    "assist": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 20,
        "priority": 0,
        "flags": {},
        "secondary": False,
        "target": "self",
        "type": "Normal"
    },
    "assurance": {
        "accuracy": 100,
        "basePower": 60,
        "category": "Physical",
        "pp": 10,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Dark"
    },
    "astonish": {
        "accuracy": 100,
        "basePower": 30,
        "category": "Physical",
        "pp": 15,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "secondary": {
            "chance": 30,
            "volatileStatus": 'flinch'
        },
        "target": "normal",
        "type": "Ghost"
    },
    "attackorder": {
        "accuracy": 100,
        "basePower": 90,
        "category": "Physical",
        "pp": 15,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "critRatio": 2,
        "secondary": False,
        "target": "normal",
        "type": "Bug"
    },
    "attract": {
        "accuracy": 100,
        "basePower": 0,
        "category": "Status",
        "pp": 15,
        "priority": 0,
        "flags": {"protect", "reflectable", "mirror", "authentic"},
        "volatileStatus": 'attract',
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "aurasphere": {
        "accuracy": True,
        "basePower": 80,
        "category": "Special",
        "pp": 20,
        "priority": 0,
        "flags": {"bullet", "protect", "pulse", "mirror", "distance"},
        "secondary": False,
        "target": "any",
        "type": "Fighting"
    },
    "aurorabeam": {
        "accuracy": 100,
        "basePower": 65,
        "category": "Special",
        "pp": 20,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": {
            "chance": 10,
            "boosts": {
                "atk": -1
            }
        },
        "target": "normal",
        "type": "Ice"
    },
    "autotomize": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 15,
        "priority": 0,
        "flags": {"snatch"},
        "boosts": {
            "spe": 2
        },
        "volatileStatus": 'autotomize',
        "secondary": False,
        "target": "self",
        "type": "Steel"
    },
    "avalanche": {
        "accuracy": 100,
        "basePower": 60,
        "category": "Physical",
        "pp": 10,
        "priority": -4,
        "flags": {"contact", "protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Ice"
    },
    "babydolleyes": {
        "accuracy": 100,
        "basePower": 0,
        "category": "Status",
        "pp": 30,
        "priority": 1,
        "flags": {"protect", "reflectable", "mirror"},
        "boosts": {
            "atk": -1
        },
        "secondary": False,
        "target": "normal",
        "type": "Fairy"
    },
    "barrage": {
        "accuracy": 85,
        "basePower": 15,
        "category": "Physical",
        "pp": 20,
        "priority": 0,
        "flags": {"bullet", "protect", "mirror"},
        "multihit": [2, 5],
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "barrier": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 20,
        "priority": 0,
        "flags": {"snatch"},
        "boosts": {
            "def": 2
        },
        "secondary": False,
        "target": "self",
        "type": "Psychic"
    },
    "batonpass": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 40,
        "priority": 0,
        "flags": {},
        "selfSwitch": 'copyvolatile',
        "secondary": False,
        "target": "self",
        "type": "Normal"
    },
    "beatup": {
        "accuracy": 100,
        "basePower": 0,
        "category": "Physical",
        "pp": 10,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "multihit": 6,
        "secondary": False,
        "target": "normal",
        "type": "Dark"
    },
    "belch": {
        "accuracy": 90,
        "basePower": 120,
        "category": "Special",
        "pp": 10,
        "priority": 0,
        "flags": {"protect"},
        "secondary": False,
        "target": "normal",
        "type": "Poison"
    },
    "bellydrum": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 10,
        "priority": 0,
        "flags": {"snatch"},
        "secondary": False,
        "target": "self",
        "type": "Normal"
    },
    "bestow": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 15,
        "priority": 0,
        "flags": {"mirror", "authentic"},
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "bide": {
        "accuracy": True,
        "basePower": 0,
        "category": "Physical",
        "pp": 10,
        "priority": 1,
        "flags": {"contact", "protect"},
        "volatileStatus": 'bide',
        "ignoreImmunity": True,
        "secondary": False,
        "target": "self",
        "type": "Normal"
    },
    "bind": {
        "accuracy": 85,
        "basePower": 15,
        "category": "Physical",
        "pp": 20,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "volatileStatus": 'partiallytrapped',
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "bite": {
        "accuracy": 100,
        "basePower": 60,
        "category": "Physical",
        "pp": 25,
        "priority": 0,
        "flags": {"bite", "contact", "protect", "mirror"},
        "secondary": {
            "chance": 30,
            "volatileStatus": 'flinch'
        },
        "target": "normal",
        "type": "Dark"
    },
    "blastburn": {
        "accuracy": 90,
        "basePower": 150,
        "category": "Special",
        "pp": 5,
        "priority": 0,
        "flags": {"recharge", "protect", "mirror"},
        "self": {
            "volatileStatus": 'mustrecharge'
        },
        "secondary": False,
        "target": "normal",
        "type": "Fire"
    },
    "blazekick": {
        "accuracy": 90,
        "basePower": 85,
        "category": "Physical",
        "pp": 10,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "critRatio": 2,
        "secondary": {
            "chance": 10,
            "status": 'brn'
        },
        "target": "normal",
        "type": "Fire"
    },
    "blizzard": {
        "accuracy": 70,
        "basePower": 110,
        "category": "Special",
        "pp": 5,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": {
            "chance": 10,
            "status": 'frz'
        },
        "target": "allAdjacentFoes",
        "type": "Ice"
    },
    "block": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 5,
        "priority": 0,
        "flags": {"reflectable", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "blueflare": {
        "accuracy": 85,
        "basePower": 130,
        "category": "Special",
        "pp": 5,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": {
            "chance": 20,
            "status": 'brn'
        },
        "target": "normal",
        "type": "Fire"
    },
    "bodyslam": {
        "accuracy": 100,
        "basePower": 85,
        "category": "Physical",
        "pp": 15,
        "priority": 0,
        "flags": {"contact", "protect", "mirror", "nonsky"},
        "secondary": {
            "chance": 30,
            "status": 'par'
        },
        "target": "normal",
        "type": "Normal"
    },
    "boltstrike": {
        "accuracy": 85,
        "basePower": 130,
        "category": "Physical",
        "pp": 5,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "secondary": {
            "chance": 20,
            "status": 'par'
        },
        "target": "normal",
        "type": "Electric"
    },
    "boneclub": {
        "accuracy": 85,
        "basePower": 65,
        "category": "Physical",
        "pp": 20,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": {
            "chance": 10,
            "volatileStatus": 'flinch'
        },
        "target": "normal",
        "type": "Ground"
    },
    "bonerush": {
        "accuracy": 90,
        "basePower": 25,
        "category": "Physical",
        "pp": 10,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "multihit": [2, 5],
        "secondary": False,
        "target": "normal",
        "type": "Ground"
    },
    "bonemerang": {
        "accuracy": 90,
        "basePower": 50,
        "category": "Physical",
        "pp": 10,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "multihit": 2,
        "secondary": False,
        "target": "normal",
        "type": "Ground"
    },
    "boomburst": {
        "accuracy": 100,
        "basePower": 140,
        "category": "Special",
        "pp": 10,
        "priority": 0,
        "flags": {"protect", "mirror", "sound", "authentic"},
        "secondary": False,
        "target": "allAdjacent",
        "type": "Normal"
    },
    "bounce": {
        "accuracy": 85,
        "basePower": 85,
        "category": "Physical",
        "pp": 5,
        "priority": 0,
        "flags": {"contact", "charge", "protect", "mirror", "gravity", "distance"},
        "secondary": {
            "chance": 30,
            "status": 'par'
        },
        "target": "any",
        "type": "Flying"
    },
    "bravebird": {
        "accuracy": 100,
        "basePower": 120,
        "category": "Physical",
        "pp": 15,
        "priority": 0,
        "flags": {"contact", "protect", "mirror", "distance"},
        "recoil": [33, 100],
        "secondary": False,
        "target": "any",
        "type": "Flying"
    },
    "brickbreak": {
        "accuracy": 100,
        "basePower": 75,
        "category": "Physical",
        "pp": 15,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Fighting"
    },
    "brine": {
        "accuracy": 100,
        "basePower": 65,
        "category": "Special",
        "pp": 10,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Water"
    },
    "bubble": {
        "accuracy": 100,
        "basePower": 40,
        "category": "Special",
        "pp": 30,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": {
            "chance": 10,
            "boosts": {
                "spe": -1
            }
        },
        "target": "allAdjacentFoes",
        "type": "Water"
    },
    "bubblebeam": {
        "accuracy": 100,
        "basePower": 65,
        "category": "Special",
        "pp": 20,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": {
            "chance": 10,
            "boosts": {
                "spe": -1
            }
        },
        "target": "normal",
        "type": "Water"
    },
    "bugbite": {
        "accuracy": 100,
        "basePower": 60,
        "category": "Physical",
        "pp": 20,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Bug"
    },
    "bugbuzz": {
        "accuracy": 100,
        "basePower": 90,
        "category": "Special",
        "pp": 10,
        "priority": 0,
        "flags": {"protect", "mirror", "sound", "authentic"},
        "secondary": {
            "chance": 10,
            "boosts": {
                "spd": -1
            }
        },
        "target": "normal",
        "type": "Bug"
    },
    "bulkup": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 20,
        "priority": 0,
        "flags": {"snatch"},
        "boosts": {
            "atk": 1,
            "def": 1
        },
        "secondary": False,
        "target": "self",
        "type": "Fighting"
    },
    "bulldoze": {
        "accuracy": 100,
        "basePower": 60,
        "category": "Physical",
        "pp": 20,
        "priority": 0,
        "flags": {"protect", "mirror", "nonsky"},
        "secondary": {
            "chance": 100,
            "boosts": {
                "spe": -1
            }
        },
        "target": "allAdjacent",
        "type": "Ground"
    },
    "bulletpunch": {
        "accuracy": 100,
        "basePower": 40,
        "category": "Physical",
        "pp": 30,
        "priority": 1,
        "flags": {"contact", "protect", "mirror", "punch"},
        "secondary": False,
        "target": "normal",
        "type": "Steel"
    },
    "bulletseed": {
        "accuracy": 100,
        "basePower": 25,
        "category": "Physical",
        "pp": 30,
        "priority": 0,
        "flags": {"bullet", "protect", "mirror"},
        "multihit": [2, 5],
        "secondary": False,
        "target": "normal",
        "type": "Grass"
    },
    "calmmind": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 20,
        "priority": 0,
        "flags": {"snatch"},
        "boosts": {
            "spa": 1,
            "spd": 1
        },
        "secondary": False,
        "target": "self",
        "type": "Psychic"
    },
    "camouflage": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 20,
        "priority": 0,
        "flags": {"snatch"},
        "secondary": False,
        "target": "self",
        "type": "Normal"
    },
    "captivate": {
        "accuracy": 100,
        "basePower": 0,
        "category": "Status",
        "pp": 20,
        "priority": 0,
        "flags": {"protect", "reflectable", "mirror"},
        "boosts": {
            "spa": -2
        },
        "secondary": False,
        "target": "allAdjacentFoes",
        "type": "Normal"
    },
    "celebrate": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 40,
        "priority": 0,
        "flags": {},
        "secondary": False,
        "target": "self",
        "type": "Normal"
    },
    "charge": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 20,
        "priority": 0,
        "flags": {"snatch"},
        "volatileStatus": 'charge',
        "boosts": {
            "spd": 1
        },
        "secondary": False,
        "target": "self",
        "type": "Electric"
    },
    "chargebeam": {
        "accuracy": 90,
        "basePower": 50,
        "category": "Special",
        "pp": 10,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": {
            "chance": 70,
            "self": {
                "boosts": {
                    "spa": 1
                }
            }
        },
        "target": "normal",
        "type": "Electric"
    },
    "charm": {
        "accuracy": 100,
        "basePower": 0,
        "category": "Status",
        "pp": 20,
        "priority": 0,
        "flags": {"protect", "reflectable", "mirror"},
        "boosts": {
            "atk": -2
        },
        "secondary": False,
        "target": "normal",
        "type": "Fairy"
    },
    "chatter": {
        "accuracy": 100,
        "basePower": 65,
        "category": "Special",
        "pp": 20,
        "priority": 0,
        "flags": {"protect", "mirror", "sound", "distance", "authentic"},
        "secondary": {
            "chance": 100,
            "volatileStatus": 'confusion'
        },
        "target": "any",
        "type": "Flying"
    },
    "chipaway": {
        "accuracy": 100,
        "basePower": 70,
        "category": "Physical",
        "pp": 20,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "ignoreDefensive": True,
        "ignoreEvasion": True,
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "circlethrow": {
        "accuracy": 90,
        "basePower": 60,
        "category": "Physical",
        "pp": 10,
        "priority": -6,
        "flags": {"contact", "protect", "mirror"},
        "forceSwitch": True,
        "target": "normal",
        "type": "Fighting"
    },
    "clamp": {
        "accuracy": 85,
        "basePower": 35,
        "category": "Physical",
        "pp": 15,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "volatileStatus": 'partiallytrapped',
        "secondary": False,
        "target": "normal",
        "type": "Water"
    },
    "clearsmog": {
        "accuracy": True,
        "basePower": 50,
        "category": "Special",
        "pp": 15,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Poison"
    },
    "closecombat": {
        "accuracy": 100,
        "basePower": 120,
        "category": "Physical",
        "pp": 5,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "self": {
            "boosts": {
                "def": -1,
                "spd": -1
            }
        },
        "secondary": False,
        "target": "normal",
        "type": "Fighting"
    },
    "coil": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 20,
        "priority": 0,
        "flags": {"snatch"},
        "boosts": {
            "atk": 1,
            "def": 1,
            "accuracy": 1
        },
        "secondary": False,
        "target": "self",
        "type": "Poison"
    },
    "cometpunch": {
        "accuracy": 85,
        "basePower": 18,
        "category": "Physical",
        "pp": 15,
        "priority": 0,
        "flags": {"contact", "protect", "mirror", "punch"},
        "multihit": [2, 5],
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "confide": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 20,
        "priority": 0,
        "flags": {"reflectable", "mirror", "sound", "authentic"},
        "boosts": {
            "spa": -1
        },
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "confuseray": {
        "accuracy": 100,
        "basePower": 0,
        "category": "Status",
        "pp": 10,
        "priority": 0,
        "flags": {"protect", "reflectable", "mirror"},
        "volatileStatus": 'confusion',
        "secondary": False,
        "target": "normal",
        "type": "Ghost"
    },
    "confusion": {
        "accuracy": 100,
        "basePower": 50,
        "category": "Special",
        "pp": 25,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": {
            "chance": 10,
            "volatileStatus": 'confusion'
        },
        "target": "normal",
        "type": "Psychic"
    },
    "constrict": {
        "accuracy": 100,
        "basePower": 10,
        "category": "Physical",
        "pp": 35,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "secondary": {
            "chance": 10,
            "boosts": {
                "spe": -1
            }
        },
        "target": "normal",
        "type": "Normal"
    },
    "conversion": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 30,
        "priority": 0,
        "flags": {"snatch"},
        "secondary": False,
        "target": "self",
        "type": "Normal"
    },
    "conversion2": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 30,
        "priority": 0,
        "flags": {"authentic"},
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "copycat": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 20,
        "priority": 0,
        "flags": {},
        "secondary": False,
        "target": "self",
        "type": "Normal"
    },
    "cosmicpower": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 20,
        "priority": 0,
        "flags": {"snatch"},
        "boosts": {
            "def": 1,
            "spd": 1
        },
        "secondary": False,
        "target": "self",
        "type": "Psychic"
    },
    "cottonguard": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 10,
        "priority": 0,
        "flags": {"snatch"},
        "boosts": {
            "def": 3
        },
        "secondary": False,
        "target": "self",
        "type": "Grass"
    },
    "cottonspore": {
        "accuracy": 100,
        "basePower": 0,
        "category": "Status",
        "pp": 40,
        "priority": 0,
        "flags": {"powder", "protect", "reflectable", "mirror"},
        "boosts": {
            "spe": -2
        },
        "secondary": False,
        "target": "allAdjacentFoes",
        "type": "Grass"
    },
    "counter": {
        "accuracy": 100,
        "basePower": 0,
        "category": "Physical",
        "pp": 20,
        "priority": -5,
        "flags": {"contact", "protect"},

        "secondary": False,
        "target": "scripted",
        "type": "Fighting"
    },
    "covet": {
        "accuracy": 100,
        "basePower": 60,
        "category": "Physical",
        "pp": 25,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "crabhammer": {
        "accuracy": 90,
        "basePower": 100,
        "category": "Physical",
        "pp": 10,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "critRatio": 2,
        "secondary": False,
        "target": "normal",
        "type": "Water"
    },
    "craftyshield": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 10,
        "priority": 3,
        "flags": {},
        "sidecondition": 'craftyshield',
        "secondary": False,
        "target": "allySide",
        "type": "Fairy"
    },
    "crosschop": {
        "accuracy": 80,
        "basePower": 100,
        "category": "Physical",
        "pp": 5,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "critRatio": 2,
        "secondary": False,
        "target": "normal",
        "type": "Fighting"
    },
    "crosspoison": {
        "accuracy": 100,
        "basePower": 70,
        "category": "Physical",
        "pp": 20,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "secondary": {
            "chance": 10,
            "status": 'psn'
        },
        "critRatio": 2,
        "secondary": {
            "chance": 10,
            "status": 'psn'
        },
        "target": "normal",
        "type": "Poison"
    },
    "crunch": {
        "accuracy": 100,
        "basePower": 80,
        "category": "Physical",
        "pp": 15,
        "priority": 0,
        "flags": {"bite", "contact", "protect", "mirror"},
        "secondary": {
            "chance": 20,
            "boosts": {
                "def": -1
            }
        },
        "target": "normal",
        "type": "Dark"
    },
    "crushclaw": {
        "accuracy": 95,
        "basePower": 75,
        "category": "Physical",
        "pp": 10,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "secondary": {
            "chance": 50,
            "boosts": {
                "def": -1
            }
        },
        "target": "normal",
        "type": "Normal"
    },
    "crushgrip": {
        "accuracy": 100,
        "basePower": 0,
        "category": "Physical",
        "pp": 5,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "curse": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 10,
        "priority": 0,
        "flags": {"authentic"},
        "volatileStatus": 'curse',
        "secondary": False,
        "target": "normal",
        "nonGhosttarget": "self",
        "type": "Ghost"
    },
    "cut": {
        "accuracy": 95,
        "basePower": 50,
        "category": "Physical",
        "pp": 30,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "darkpulse": {
        "accuracy": 100,
        "basePower": 80,
        "category": "Special",
        "pp": 15,
        "priority": 0,
        "flags": {"protect", "pulse", "mirror", "distance"},
        "secondary": {
            "chance": 20,
            "volatileStatus": 'flinch'
        },
        "target": "any",
        "type": "Dark"
    },
    "darkvoid": {
        "accuracy": 80,
        "basePower": 0,
        "category": "Status",
        "pp": 10,
        "priority": 0,
        "flags": {"protect", "reflectable", "mirror"},
        "status": 'slp',
        "secondary": False,
        "target": "allAdjacentFoes",
        "type": "Dark"
    },
    "dazzlinggleam": {
        "accuracy": 100,
        "basePower": 80,
        "category": "Special",
        "pp": 10,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": False,
        "target": "allAdjacentFoes",
        "type": "Fairy"
    },
    "defendorder": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 10,
        "priority": 0,
        "flags": {"snatch"},
        "boosts": {
            "def": 1,
            "spd": 1
        },
        "secondary": False,
        "target": "self",
        "type": "Bug"
    },
    "defensecurl": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 40,
        "priority": 0,
        "flags": {"snatch"},
        "boosts": {
            "def": 1
        },
        "volatileStatus": 'DefenseCurl',
        "secondary": False,
        "target": "self",
        "type": "Normal"
    },
    "defog": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 15,
        "priority": 0,
        "flags": {"protect", "reflectable", "mirror", "authentic"},
        "secondary": False,
        "target": "normal",
        "type": "Flying"
    },
    "destinybond": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 5,
        "priority": 0,
        "flags": {"authentic"},
        "volatileStatus": 'destinybond',
        "secondary": False,
        "target": "self",
        "type": "Ghost"
    },
    "detect": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 5,
        "priority": 4,
        "flags": {},
        "stallingMove": True,
        "volatileStatus": 'protect',
        "secondary": False,
        "target": "self",
        "type": "Fighting"
    },
    "diamondstorm": {
        "accuracy": 95,
        "basePower": 100,
        "category": "Physical",
        "pp": 5,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": {
            "chance": 50,
            "self": {
                "boosts": {
                    "def": 1
                }
            }
        },
        "target": "allAdjacentFoes",
        "type": "Rock"
    },
    "dig": {
        "accuracy": 100,
        "basePower": 80,
        "category": "Physical",
        "pp": 10,
        "priority": 0,
        "flags": {"contact", "charge", "protect", "mirror", "nonsky"},
        "secondary": False,
        "target": "normal",
        "type": "Ground"
    },
    "disable": {
        "accuracy": 100,
        "basePower": 0,
        "category": "Status",
        "pp": 20,
        "priority": 0,
        "flags": {"protect", "reflectable", "mirror", "authentic"},
        "volatileStatus": 'disable',
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "disarmingvoice": {
        "accuracy": True,
        "basePower": 40,
        "category": "Special",
        "pp": 15,
        "priority": 0,
        "flags": {"protect", "mirror", "sound", "authentic"},
        "secondary": False,
        "target": "allAdjacentFoes",
        "type": "Fairy"
    },
    "discharge": {
        "accuracy": 100,
        "basePower": 80,
        "category": "Special",
        "pp": 15,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": {
            "chance": 30,
            "status": 'par'
        },
        "target": "allAdjacent",
        "type": "Electric"
    },
    "dive": {
        "accuracy": 100,
        "basePower": 80,
        "category": "Physical",
        "pp": 10,
        "priority": 0,
        "flags": {"contact", "charge", "protect", "mirror", "nonsky"},
        "secondary": False,
        "target": "normal",
        "type": "Water"
    },
    "dizzypunch": {
        "accuracy": 100,
        "basePower": 70,
        "category": "Physical",
        "pp": 10,
        "priority": 0,
        "flags": {"contact", "protect", "mirror", "punch"},
        "secondary": {
            "chance": 20,
            "volatileStatus": 'confusion'
        },
        "target": "normal",
        "type": "Normal"
    },
    "doomdesire": {
        "accuracy": 100,
        "basePower": 140,
        "category": "Special",
        "pp": 5,
        "priority": 0,
        "flags": {},
        "isFutureMove": True,
        "secondary": False,
        "target": "normal",
        "type": "Steel"
    },
    "doubleedge": {
        "accuracy": 100,
        "basePower": 120,
        "category": "Physical",
        "pp": 15,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "recoil": [33, 100],
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "doublehit": {
        "accuracy": 90,
        "basePower": 35,
        "category": "Physical",
        "pp": 10,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "multihit": 2,
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "doublekick": {
        "accuracy": 100,
        "basePower": 30,
        "category": "Physical",
        "pp": 30,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "multihit": 2,
        "secondary": False,
        "target": "normal",
        "type": "Fighting"
    },
    "doubleslap": {
        "accuracy": 85,
        "basePower": 15,
        "category": "Physical",
        "pp": 10,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "multihit": [2, 5],
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "doubleteam": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 15,
        "priority": 0,
        "flags": {"snatch"},
        "boosts": {
            "evasion": 1
        },
        "secondary": False,
        "target": "self",
        "type": "Normal"
    },
    "dracometeor": {
        "accuracy": 90,
        "basePower": 130,
        "category": "Special",
        "pp": 5,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "self": {
            "boosts": {
                "spa": -2
            }
        },
        "secondary": False,
        "target": "normal",
        "type": "Dragon"
    },
    "dragonascent": {
        "accuracy": 100,
        "basePower": 120,
        "category": "Physical",
        "pp": 5,
        "priority": 0,
        "flags": {"contact", "protect", "mirror", "distance"},
        "self": {
            "boosts": {
                "def": -1,
                "spd": -1
            }
        },
        "secondary": False,
        "target": "any",
        "type": "Flying"
    },
    "dragonbreath": {
        "accuracy": 100,
        "basePower": 60,
        "category": "Special",
        "pp": 20,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": {
            "chance": 30,
            "status": 'par'
        },
        "target": "normal",
        "type": "Dragon"
    },
    "dragonclaw": {
        "accuracy": 100,
        "basePower": 80,
        "category": "Physical",
        "pp": 15,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Dragon"
    },
    "dragondance": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 20,
        "priority": 0,
        "flags": {"snatch"},
        "boosts": {
            "atk": 1,
            "spe": 1
        },
        "secondary": False,
        "target": "self",
        "type": "Dragon"
    },
    "dragonpulse": {
        "accuracy": 100,
        "basePower": 85,
        "category": "Special",
        "pp": 10,
        "priority": 0,
        "flags": {"protect", "pulse", "mirror", "distance"},
        "secondary": False,
        "target": "any",
        "type": "Dragon"
    },
    "dragonrage": {
        "accuracy": 100,
        "basePower": 0,
        "damage": 40,
        "category": "Special",
        "pp": 10,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Dragon"
    },
    "dragonrush": {
        "accuracy": 75,
        "basePower": 100,
        "category": "Physical",
        "pp": 10,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "secondary": {
            "chance": 20,
            "volatileStatus": 'flinch'
        },
        "target": "normal",
        "type": "Dragon"
    },
    "dragontail": {
        "accuracy": 90,
        "basePower": 60,
        "category": "Physical",
        "pp": 10,
        "priority": -6,
        "flags": {"contact", "protect", "mirror"},
        "forceSwitch": True,
        "secondary": False,
        "target": "normal",
        "type": "Dragon"
    },
    "drainingkiss": {
        "accuracy": 100,
        "basePower": 50,
        "category": "Special",
        "pp": 10,
        "priority": 0,
        "flags": {"contact", "protect", "mirror", "heal"},
        "drain": [3, 4],
        "secondary": False,
        "target": "normal",
        "type": "Fairy"
    },
    "drainpunch": {
        "accuracy": 100,
        "basePower": 75,
        "category": "Physical",
        "pp": 10,
        "priority": 0,
        "flags": {"contact", "protect", "mirror", "punch", "heal"},
        "drain": [1, 2],
        "secondary": False,
        "target": "normal",
        "type": "Fighting"
    },
    "dreameater": {
        "accuracy": 100,
        "basePower": 100,
        "category": "Special",
        "pp": 15,
        "priority": 0,
        "flags": {"protect", "mirror", "heal"},
        "drain": [1, 2],
        "secondary": False,
        "target": "normal",
        "type": "Psychic"
    },
    "drillpeck": {
        "accuracy": 100,
        "basePower": 80,
        "category": "Physical",
        "pp": 20,
        "priority": 0,
        "flags": {"contact", "protect", "mirror", "distance"},
        "secondary": False,
        "target": "any",
        "type": "Flying"
    },
    "drillrun": {
        "accuracy": 95,
        "basePower": 80,
        "category": "Physical",
        "pp": 10,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "critRatio": 2,
        "secondary": False,
        "target": "normal",
        "type": "Ground"
    },
    "dualchop": {
        "accuracy": 90,
        "basePower": 40,
        "category": "Physical",
        "pp": 15,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "multihit": 2,
        "secondary": False,
        "target": "normal",
        "type": "Dragon"
    },
    "dynamicpunch": {
        "accuracy": 50,
        "basePower": 100,
        "category": "Physical",
        "pp": 5,
        "priority": 0,
        "flags": {"contact", "protect", "mirror", "punch"},
        "secondary": {
            "chance": 100,
            "volatileStatus": 'confusion'
        },
        "target": "normal",
        "type": "Fighting"
    },
    "earthpower": {
        "accuracy": 100,
        "basePower": 90,
        "category": "Special",
        "pp": 10,
        "priority": 0,
        "flags": {"protect", "mirror", "nonsky"},
        "secondary": {
            "chance": 10,
            "boosts": {
                "spd": -1
            }
        },
        "target": "normal",
        "type": "Ground"
    },
    "earthquake": {
        "accuracy": 100,
        "basePower": 100,
        "category": "Physical",
        "pp": 10,
        "priority": 0,
        "flags": {"protect", "mirror", "nonsky"},
        "secondary": False,
        "target": "allAdjacent",
        "type": "Ground"
    },
    "echoedvoice": {
        "accuracy": 100,
        "basePower": 40,
        "category": "Special",
        "pp": 15,
        "priority": 0,
        "flags": {"protect", "mirror", "sound", "authentic"},
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "eerieimpulse": {
        "accuracy": 100,
        "basePower": 0,
        "category": "Status",
        "pp": 15,
        "priority": 0,
        "flags": {"protect", "reflectable", "mirror"},
        "boosts": {
            "spa": -2
        },
        "secondary": False,
        "target": "normal",
        "type": "Electric"
    },
    "eggbomb": {
        "accuracy": 75,
        "basePower": 100,
        "category": "Physical",
        "pp": 10,
        "priority": 0,
        "flags": {"bullet", "protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "electricterrain": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 10,
        "priority": 0,
        "flags": {"nonsky"},
        "terrain": 'electricterrain',
        "secondary": False,
        "target": "all",
        "type": "Electric"
    },
    "electrify": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 20,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "volatileStatus": 'electrify',
        "secondary": False,
        "target": "normal",
        "type": "Electric"
    },
    "electroball": {
        "accuracy": 100,
        "basePower": 0,
        "category": "Special",
        "pp": 10,
        "priority": 0,
        "flags": {"bullet", "protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Electric"
    },
    "electroweb": {
        "accuracy": 95,
        "basePower": 55,
        "category": "Special",
        "pp": 15,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": {
            "chance": 100,
            "boosts": {
                "spe": -1
            }
        },
        "target": "allAdjacentFoes",
        "type": "Electric"
    },
    "embargo": {
        "accuracy": 100,
        "basePower": 0,
        "category": "Status",
        "pp": 15,
        "priority": 0,
        "flags": {"protect", "reflectable", "mirror"},
        "volatileStatus": 'embargo',
        "secondary": False,
        "target": "normal",
        "type": "Dark"
    },
    "ember": {
        "accuracy": 100,
        "basePower": 40,
        "category": "Special",
        "pp": 25,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": {
            "chance": 10,
            "status": 'brn'
        },
        "target": "normal",
        "type": "Fire"
    },
    "encore": {
        "accuracy": 100,
        "basePower": 0,
        "category": "Status",
        "pp": 5,
        "priority": 0,
        "flags": {"protect", "reflectable", "mirror", "authentic"},
        "volatileStatus": 'encore',
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "endeavor": {
        "accuracy": 100,
        "basePower": 0,
        "category": "Physical",
        "pp": 5,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "endure": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 10,
        "priority": 4,
        "flags": {},
        "stallingMove": True,
        "volatileStatus": 'endure',
        "secondary": False,
        "target": "self",
        "type": "Normal"
    },
    "energyball": {
        "accuracy": 100,
        "basePower": 90,
        "category": "Special",
        "pp": 10,
        "priority": 0,
        "flags": {"bullet", "protect", "mirror"},
        "secondary": {
            "chance": 10,
            "boosts": {
                "spd": -1
            }
        },
        "target": "normal",
        "type": "Grass"
    },
    "entrainment": {
        "accuracy": 100,
        "basePower": 0,
        "category": "Status",
        "pp": 15,
        "priority": 0,
        "flags": {"protect", "reflectable", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "eruption": {
        "accuracy": 100,
        "basePower": 150,
        "category": "Special",
        "pp": 5,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": False,
        "target": "allAdjacentFoes",
        "type": "Fire"
    },
    "explosion": {
        "accuracy": 100,
        "basePower": 250,
        "category": "Physical",
        "pp": 5,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "selfdestruct": True,
        "secondary": False,
        "target": "allAdjacent",
        "type": "Normal"
    },
    "extrasensory": {
        "accuracy": 100,
        "basePower": 80,
        "category": "Special",
        "pp": 20,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": {
            "chance": 10,
            "volatileStatus": 'flinch'
        },
        "target": "normal",
        "type": "Psychic"
    },
    "extremespeed": {
        "accuracy": 100,
        "basePower": 80,
        "category": "Physical",
        "pp": 5,
        "priority": 2,
        "flags": {"contact", "protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "facade": {
        "accuracy": 100,
        "basePower": 70,
        "category": "Physical",
        "pp": 20,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "feintattack": {
        "accuracy": True,
        "basePower": 60,
        "category": "Physical",
        "pp": 20,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Dark"
    },
    "fairylock": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 10,
        "priority": 0,
        "flags": {"mirror", "authentic"},
        "pseudoWeather": 'fairylock',
        "secondary": False,
        "target": "all",
        "type": "Fairy"
    },
    "fairywind": {
        "accuracy": 100,
        "basePower": 40,
        "category": "Special",
        "pp": 30,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Fairy"
    },
    "fakeout": {
        "accuracy": 100,
        "basePower": 40,
        "category": "Physical",
        "pp": 10,
        "priority": 3,
        "flags": {"contact", "protect", "mirror"},
        "secondary": {
            "chance": 100,
            "volatileStatus": 'flinch'
        },
        "target": "normal",
        "type": "Normal"
    },
    "faketears": {
        "accuracy": 100,
        "basePower": 0,
        "category": "Status",
        "pp": 20,
        "priority": 0,
        "flags": {"protect", "reflectable", "mirror"},
        "boosts": {
            "spd": -2
        },
        "secondary": False,
        "target": "normal",
        "type": "Dark"
    },
    "falseswipe": {
        "accuracy": 100,
        "basePower": 40,
        "category": "Physical",
        "pp": 40,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "noFaint": True,
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "featherdance": {
        "accuracy": 100,
        "basePower": 0,
        "category": "Status",
        "pp": 15,
        "priority": 0,
        "flags": {"protect", "reflectable", "mirror"},
        "boosts": {
            "atk": -2
        },
        "secondary": False,
        "target": "normal",
        "type": "Flying"
    },
    "feint": {
        "accuracy": 100,
        "basePower": 30,
        "category": "Physical",
        "pp": 10,
        "priority": 2,
        "flags": {"mirror"},
        "breaksProtect": True,
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "fellstinger": {
        "accuracy": 100,
        "basePower": 30,
        "category": "Physical",
        "pp": 25,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Bug"
    },
    "fierydance": {
        "accuracy": 100,
        "basePower": 80,
        "category": "Special",
        "pp": 10,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": {
            "chance": 50,
            "self": {
                "boosts": {
                    "spa": 1
                }
            }
        },
        "target": "normal",
        "type": "Fire"
    },
    "finalgambit": {
        "accuracy": 100,
        "basePower": 0,
        "category": "Special",
        "pp": 5,
        "priority": 0,
        "flags": {"protect"},
        "selfdestruct": True,
        "secondary": False,
        "target": "normal",
        "type": "Fighting"
    },
    "fireblast": {
        "accuracy": 85,
        "basePower": 110,
        "category": "Special",
        "pp": 5,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": {
            "chance": 10,
            "status": 'brn'
        },
        "target": "normal",
        "type": "Fire"
    },
    "firefang": {
        "accuracy": 95,
        "basePower": 65,
        "category": "Physical",
        "pp": 15,
        "priority": 0,
        "flags": {"bite", "contact", "protect", "mirror"},
        "secondary": [
            {
                "chance": 10,
                "status": 'brn'
            }, {
                "chance": 10,
                "volatileStatus": 'flinch'
            }
        ],
        "target": "normal",
        "type": "Fire"
    },
    "firepledge": {
        "accuracy": 100,
        "basePower": 80,
        "category": "Special",
        "pp": 10,
        "priority": 0,
        "flags": {"protect", "mirror", "nonsky"},
        "secondary": False,
        "target": "normal",
        "type": "Fire"
    },
    "firepunch": {
        "accuracy": 100,
        "basePower": 75,
        "category": "Physical",
        "pp": 15,
        "priority": 0,
        "flags": {"contact", "protect", "mirror", "punch"},
        "secondary": {
            "chance": 10,
            "status": 'brn'
        },
        "target": "normal",
        "type": "Fire"
    },
    "firespin": {
        "accuracy": 85,
        "basePower": 35,
        "category": "Special",
        "pp": 15,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "volatileStatus": 'partiallytrapped',
        "secondary": False,
        "target": "normal",
        "type": "Fire"
    },
    "fissure": {
        "accuracy": 30,
        "basePower": 0,
        "category": "Physical",
        "pp": 5,
        "priority": 0,
        "flags": {"protect", "mirror", "nonsky"},
        "ohko": True,
        "secondary": False,
        "target": "normal",
        "type": "Ground"
    },
    "flail": {
        "accuracy": 100,
        "basePower": 0,
        "category": "Physical",
        "pp": 15,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "flameburst": {
        "accuracy": 100,
        "basePower": 70,
        "category": "Special",
        "pp": 15,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Fire"
    },
    "flamecharge": {
        "accuracy": 100,
        "basePower": 50,
        "category": "Physical",
        "pp": 20,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "secondary": {
            "chance": 100,
            "self": {
                "boosts": {
                    "spe": 1
                }
            }
        },
        "target": "normal",
        "type": "Fire"
    },
    "flamewheel": {
        "accuracy": 100,
        "basePower": 60,
        "category": "Physical",
        "pp": 25,
        "priority": 0,
        "flags": {"contact", "protect", "mirror", "defrost"},
        "secondary": {
            "chance": 10,
            "status": 'brn'
        },
        "target": "normal",
        "type": "Fire"
    },
    "flamethrower": {
        "accuracy": 100,
        "basePower": 90,
        "category": "Special",
        "pp": 15,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": {
            "chance": 10,
            "status": 'brn'
        },
        "target": "normal",
        "type": "Fire"
    },
    "flareblitz": {
        "accuracy": 100,
        "basePower": 120,
        "category": "Physical",
        "pp": 15,
        "priority": 0,
        "flags": {"contact", "protect", "mirror", "defrost"},
        "recoil": [33, 100],
        "secondary": {
            "chance": 10,
            "status": 'brn'
        },
        "target": "normal",
        "type": "Fire"
    },
    "flash": {
        "accuracy": 100,
        "basePower": 0,
        "category": "Status",
        "pp": 20,
        "priority": 0,
        "flags": {"protect", "reflectable", "mirror"},
        "boosts": {
            "accuracy": -1
        },
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "flashcannon": {
        "accuracy": 100,
        "basePower": 80,
        "category": "Special",
        "pp": 10,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": {
            "chance": 10,
            "boosts": {
                "spd": -1
            }
        },
        "target": "normal",
        "type": "Steel"
    },
    "flatter": {
        "accuracy": 100,
        "basePower": 0,
        "category": "Status",
        "pp": 15,
        "priority": 0,
        "flags": {"protect", "reflectable", "mirror"},
        "volatileStatus": 'confusion',
        "boosts": {
            "spa": 1
        },
        "secondary": False,
        "target": "normal",
        "type": "Dark"
    },
    "fling": {
        "accuracy": 100,
        "basePower": 0,
        "category": "Physical",
        "pp": 10,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Dark"
    },
    "flowershield": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 10,
        "priority": 0,
        "flags": {"distance"},
        "secondary": False,
        "target": "all",
        "type": "Fairy"
    },
    "fly": {
        "accuracy": 95,
        "basePower": 90,
        "category": "Physical",
        "pp": 15,
        "priority": 0,
        "flags": {"contact", "charge", "protect", "mirror", "gravity", "distance"},
        "secondary": False,
        "target": "any",
        "type": "Flying"
    },
    "flyingpress": {
        "accuracy": 95,
        "basePower": 80,
        "category": "Physical",
        "pp": 10,
        "flags": {"contact", "protect", "mirror", "gravity", "distance", "nonsky"},
        "priority": 0,
        "secondary": False,
        "target": "any",
        "type": "Fighting"
    },
    "focusblast": {
        "accuracy": 70,
        "basePower": 120,
        "category": "Special",
        "pp": 5,
        "priority": 0,
        "flags": {"bullet", "protect", "mirror"},
        "secondary": {
            "chance": 10,
            "boosts": {
                "spd": -1
            }
        },
        "target": "normal",
        "type": "Fighting"
    },
    "focusenergy": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 30,
        "priority": 0,
        "flags": {"snatch"},
        "volatileStatus": 'focusenergy',
        "secondary": False,
        "target": "self",
        "type": "Normal"
    },
    "focuspunch": {
        "accuracy": 100,
        "basePower": 150,
        "category": "Physical",
        "pp": 20,
        "priority": -3,
        "flags": {"contact", "protect", "punch"},
        "secondary": False,
        "target": "normal",
        "type": "Fighting"
    },
    "followme": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 20,
        "priority": 2,
        "flags": {},
        "volatileStatus": 'followme',
        "secondary": False,
        "target": "self",
        "type": "Normal"
    },
    "forcepalm": {
        "accuracy": 100,
        "basePower": 60,
        "category": "Physical",
        "pp": 10,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "secondary": {
            "chance": 30,
            "status": 'par'
        },
        "target": "normal",
        "type": "Fighting"
    },
    "foresight": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 40,
        "priority": 0,
        "flags": {"protect", "reflectable", "mirror", "authentic"},
        "volatileStatus": 'foresight',
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "forestscurse": {
        "accuracy": 100,
        "basePower": 0,
        "category": "Status",
        "pp": 20,
        "priority": 0,
        "flags": {"protect", "reflectable", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Grass"
    },
    "foulplay": {
        "accuracy": 100,
        "basePower": 95,
        "category": "Physical",
        "pp": 15,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "useTargetOffensive": True,
        "secondary": False,
        "target": "normal",
        "type": "Dark"
    },
    "freezedry": {
        "accuracy": 100,
        "basePower": 70,
        "category": "Special",
        "pp": 20,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": {
            "chance": 10,
            "status": 'frz'
        },
        "target": "normal",
        "type": "Ice"
    },
    "freezeshock": {
        "accuracy": 90,
        "basePower": 140,
        "category": "Physical",
        "pp": 5,
        "priority": 0,
        "flags": {"charge", "protect", "mirror"},
        "secondary": {
            "chance": 30,
            "status": 'par'
        },
        "target": "normal",
        "type": "Ice"
    },
    "frenzyplant": {
        "accuracy": 90,
        "basePower": 150,
        "category": "Special",
        "pp": 5,
        "priority": 0,
        "flags": {"recharge", "protect", "mirror", "nonsky"},
        "self": {
            "volatileStatus": 'mustrecharge'
        },
        "secondary": False,
        "target": "normal",
        "type": "Grass"
    },
    "frostbreath": {
        "accuracy": 90,
        "basePower": 60,
        "category": "Special",
        "pp": 10,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "willCrit": True,
        "secondary": False,
        "target": "normal",
        "type": "Ice"
    },
    "frustration": {
        "accuracy": 100,
        "basePower": 0,
        "category": "Physical",
        "pp": 20,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "furyattack": {
        "accuracy": 85,
        "basePower": 15,
        "category": "Physical",
        "pp": 20,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "multihit": [2, 5],
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "furycutter": {
        "accuracy": 95,
        "basePower": 40,
        "category": "Physical",
        "pp": 20,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Bug"
    },
    "furyswipes": {
        "accuracy": 80,
        "basePower": 18,
        "category": "Physical",
        "pp": 15,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "multihit": [2, 5],
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "fusionbolt": {
        "accuracy": 100,
        "basePower": 100,
        "category": "Physical",
        "pp": 5,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Electric"
    },
    "fusionflare": {
        "accuracy": 100,
        "basePower": 100,
        "category": "Special",
        "pp": 5,
        "priority": 0,
        "flags": {"protect", "mirror", "defrost"},
        "secondary": False,
        "target": "normal",
        "type": "Fire"
    },
    "futuresight": {
        "accuracy": 100,
        "basePower": 120,
        "category": "Special",
        "pp": 10,
        "priority": 0,
        "flags": {},
        "ignoreImmunity": True,
        "isFutureMove": True,
        "secondary": False,
        "target": "normal",
        "type": "Psychic"
    },
    "gastroacid": {
        "accuracy": 100,
        "basePower": 0,
        "category": "Status",
        "pp": 10,
        "priority": 0,
        "flags": {"protect", "reflectable", "mirror"},
        "volatileStatus": 'gastroacid',
        "secondary": False,
        "target": "normal",
        "type": "Poison"
    },
    "geargrind": {
        "accuracy": 85,
        "basePower": 50,
        "category": "Physical",
        "pp": 15,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "multihit": 2,
        "secondary": False,
        "target": "normal",
        "type": "Steel"
    },
    "geomancy": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 10,
        "priority": 0,
        "flags": {"charge", "nonsky"},
        "boosts": {
            "spa": 2,
            "spd": 2,
            "spe": 2
        },
        "secondary": False,
        "target": "self",
        "type": "Fairy"
    },
    "gigadrain": {
        "accuracy": 100,
        "basePower": 75,
        "category": "Special",
        "pp": 10,
        "priority": 0,
        "flags": {"protect", "mirror", "heal"},
        "drain": [1, 2],
        "secondary": False,
        "target": "normal",
        "type": "Grass"
    },
    "gigaimpact": {
        "accuracy": 90,
        "basePower": 150,
        "category": "Physical",
        "pp": 5,
        "priority": 0,
        "flags": {"contact", "recharge", "protect", "mirror"},
        "self": {
            "volatileStatus": 'mustrecharge'
        },
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "glaciate": {
        "accuracy": 95,
        "basePower": 65,
        "category": "Special",
        "pp": 10,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": {
            "chance": 100,
            "boosts": {
                "spe": -1
            }
        },
        "target": "allAdjacentFoes",
        "type": "Ice"
    },
    "glare": {
        "accuracy": 100,
        "basePower": 0,
        "category": "Status",
        "pp": 30,
        "priority": 0,
        "flags": {"protect", "reflectable", "mirror"},
        "status": 'par',
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "grassknot": {
        "accuracy": 100,
        "basePower": 0,
        "category": "Special",
        "pp": 20,
        "priority": 0,
        "flags": {"contact", "protect", "mirror", "nonsky"},
        "secondary": False,
        "target": "normal",
        "type": "Grass"
    },
    "grasspledge": {
        "accuracy": 100,
        "basePower": 80,
        "category": "Special",
        "pp": 10,
        "priority": 0,
        "flags": {"protect", "mirror", "nonsky"},
        "secondary": False,
        "target": "normal",
        "type": "Grass"
    },
    "grasswhistle": {
        "accuracy": 55,
        "basePower": 0,
        "category": "Status",
        "pp": 15,
        "priority": 0,
        "flags": {"protect", "reflectable", "mirror", "sound", "authentic"},
        "status": 'slp',
        "secondary": False,
        "target": "normal",
        "type": "Grass"
    },
    "grassyterrain": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 10,
        "priority": 0,
        "flags": {"nonsky"},
        "terrain": 'grassyterrain',
        "secondary": False,
        "target": "all",
        "type": "Grass"
    },
    "gravity": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 5,
        "priority": 0,
        "flags": {"nonsky"},
        "pseudoWeather": 'gravity',
        "secondary": False,
        "target": "all",
        "type": "Psychic"
    },
    "growl": {
        "accuracy": 100,
        "basePower": 0,
        "category": "Status",
        "pp": 40,
        "priority": 0,
        "flags": {"protect", "reflectable", "mirror", "sound", "authentic"},
        "boosts": {
            "atk": -1
        },
        "secondary": False,
        "target": "allAdjacentFoes",
        "type": "Normal"
    },
    "growth": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 20,
        "priority": 0,
        "flags": {"snatch"},
        "boosts": {
            "atk": 1,
            "spa": 1
        },
        "secondary": False,
        "target": "self",
        "type": "Normal"
    },
    "grudge": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 5,
        "priority": 0,
        "flags": {"authentic"},
        "volatileStatus": 'grudge',
        "secondary": False,
        "target": "self",
        "type": "Ghost"
    },
    "guardsplit": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 10,
        "priority": 0,
        "flags": {"protect"},
        "secondary": False,
        "target": "normal",
        "type": "Psychic"
    },
    "guardswap": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 10,
        "priority": 0,
        "flags": {"protect", "mirror", "authentic"},
        "secondary": False,
        "target": "normal",
        "type": "Psychic"
    },
    "guillotine": {
        "accuracy": 30,
        "basePower": 0,
        "category": "Physical",
        "pp": 5,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "ohko": True,
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "gunkshot": {
        "accuracy": 80,
        "basePower": 120,
        "category": "Physical",
        "pp": 5,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": {
            "chance": 30,
            "status": 'psn'
        },
        "target": "normal",
        "type": "Poison"
    },
    "gust": {
        "accuracy": 100,
        "basePower": 40,
        "category": "Special",
        "pp": 35,
        "priority": 0,
        "flags": {"protect", "mirror", "distance"},
        "secondary": False,
        "target": "any",
        "type": "Flying"
    },
    "gyroball": {
        "accuracy": 100,
        "basePower": 0,
        "category": "Physical",
        "pp": 5,
        "priority": 0,
        "flags": {"bullet", "contact", "protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Steel"
    },
    "hail": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 10,
        "priority": 0,
        "flags": {},
        "weather": 'hail',
        "secondary": False,
        "target": "all",
        "type": "Ice"
    },
    "hammerarm": {
        "accuracy": 90,
        "basePower": 100,
        "category": "Physical",
        "pp": 10,
        "priority": 0,
        "flags": {"contact", "protect", "mirror", "punch"},
        "self": {
            "boosts": {
                "spe": -1
            }
        },
        "secondary": False,
        "target": "normal",
        "type": "Fighting"
    },
    "happyhour": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 30,
        "priority": 0,
        "flags": {},
        "secondary": False,
        "target": "allySide",
        "type": "Normal"
    },
    "harden": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 30,
        "priority": 0,
        "flags": {"snatch"},
        "boosts": {
            "def": 1
        },
        "secondary": False,
        "target": "self",
        "type": "Normal"
    },
    "haze": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 30,
        "priority": 0,
        "flags": {"authentic"},
        "secondary": False,
        "target": "all",
        "type": "Ice"
    },
    "headcharge": {
        "accuracy": 100,
        "basePower": 120,
        "category": "Physical",
        "pp": 15,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "recoil": [1, 4],
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "headsmash": {
        "accuracy": 80,
        "basePower": 150,
        "category": "Physical",
        "pp": 5,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "recoil": [1, 2],
        "secondary": False,
        "target": "normal",
        "type": "Rock"
    },
    "headbutt": {
        "accuracy": 100,
        "basePower": 70,
        "category": "Physical",
        "pp": 15,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "secondary": {
            "chance": 30,
            "volatileStatus": 'flinch'
        },
        "target": "normal",
        "type": "Normal"
    },
    "healbell": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 5,
        "priority": 0,
        "flags": {"snatch", "sound", "distance", "authentic"},
        "secondary": False,
        "target": "allyTeam",
        "type": "Normal"
    },
    "healblock": {
        "accuracy": 100,
        "basePower": 0,
        "category": "Status",
        "pp": 15,
        "priority": 0,
        "flags": {"protect", "reflectable", "mirror"},
        "volatileStatus": 'healblock',
        "secondary": False,
        "target": "allAdjacentFoes",
        "type": "Psychic"
    },
    "healorder": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 10,
        "priority": 0,
        "flags": {"snatch", "heal"},
        "heal": [1, 2],
        "secondary": False,
        "target": "self",
        "type": "Bug"
    },
    "healpulse": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 10,
        "priority": 0,
        "flags": {"protect", "pulse", "reflectable", "distance", "heal"},
        "secondary": False,
        "target": "any",
        "type": "Psychic"
    },
    "healingwish": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 10,
        "priority": 0,
        "flags": {"snatch", "heal"},
        "selfdestruct": True,
        "sidecondition": 'healingwish',
        "secondary": False,
        "target": "self",
        "type": "Psychic"
    },
    "heartstamp": {
        "accuracy": 100,
        "basePower": 60,
        "category": "Physical",
        "pp": 25,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "secondary": {
            "chance": 30,
            "volatileStatus": 'flinch'
        },
        "target": "normal",
        "type": "Psychic"
    },
    "heartswap": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 10,
        "priority": 0,
        "flags": {"protect", "mirror", "authentic"},
        "secondary": False,
        "target": "normal",
        "type": "Psychic"
    },
    "heatcrash": {
        "accuracy": 100,
        "basePower": 0,
        "category": "Physical",
        "pp": 10,
        "priority": 0,
        "flags": {"contact", "protect", "mirror", "nonsky"},
        "secondary": False,
        "target": "normal",
        "type": "Fire"
    },
    "heatwave": {
        "accuracy": 90,
        "basePower": 95,
        "category": "Special",
        "pp": 10,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": {
            "chance": 10,
            "status": 'brn'
        },
        "target": "allAdjacentFoes",
        "type": "Fire"
    },
    "heavyslam": {
        "accuracy": 100,
        "basePower": 0,
        "category": "Physical",
        "pp": 10,
        "priority": 0,
        "flags": {"contact", "protect", "mirror", "nonsky"},
        "secondary": False,
        "target": "normal",
        "type": "Steel"
    },
    "helpinghand": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 20,
        "priority": 5,
        "flags": {"authentic"},
        "volatileStatus": 'helpinghand',
        "secondary": False,
        "target": "adjacentAlly",
        "type": "Normal"
    },
    "hex": {
        "accuracy": 100,
        "basePower": 65,
        "category": "Special",
        "pp": 10,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Ghost"
    },
    "hiddenpower": {
        "accuracy": 100,
        "basePower": 60,
        "category": "Special",
        "pp": 15,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "hiddenpowerbug": {
        "accuracy": 100,
        "basePower": 60,
        "category": "Special",
        "pp": 15,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Bug"
    },
    "hiddenpowerdark": {
        "accuracy": 100,
        "basePower": 60,
        "category": "Special",
        "pp": 15,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Dark"
    },
    "hiddenpowerdragon": {
        "accuracy": 100,
        "basePower": 60,
        "category": "Special",
        "pp": 15,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Dragon"
    },
    "hiddenpowerelectric": {
        "accuracy": 100,
        "basePower": 60,
        "category": "Special",
        "pp": 15,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Electric"
    },
    "hiddenpowerfighting": {
        "accuracy": 100,
        "basePower": 60,
        "category": "Special",
        "pp": 15,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Fighting"
    },
    "hiddenpowerfire": {
        "accuracy": 100,
        "basePower": 60,
        "category": "Special",
        "pp": 15,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Fire"
    },
    "hiddenpowerflying": {
        "accuracy": 100,
        "basePower": 60,
        "category": "Special",
        "pp": 15,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Flying"
    },
    "hiddenpowerghost": {
        "accuracy": 100,
        "basePower": 60,
        "category": "Special",
        "pp": 15,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Ghost"
    },
    "hiddenpowergrass": {
        "accuracy": 100,
        "basePower": 60,
        "category": "Special",
        "pp": 15,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Grass"
    },
    "hiddenpowerground": {
        "accuracy": 100,
        "basePower": 60,
        "category": "Special",
        "pp": 15,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Ground"
    },
    "hiddenpowerice": {
        "accuracy": 100,
        "basePower": 60,
        "category": "Special",
        "pp": 15,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Ice"
    },
    "hiddenpowerpoison": {
        "accuracy": 100,
        "basePower": 60,
        "category": "Special",
        "pp": 15,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Poison"
    },
    "hiddenpowerpsychic": {
        "accuracy": 100,
        "basePower": 60,
        "category": "Special",
        "pp": 15,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Psychic"
    },
    "hiddenpowerrock": {
        "accuracy": 100,
        "basePower": 60,
        "category": "Special",
        "pp": 15,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Rock"
    },
    "hiddenpowersteel": {
        "accuracy": 100,
        "basePower": 60,
        "category": "Special",
        "pp": 15,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Steel"
    },
    "hiddenpowerwater": {
        "accuracy": 100,
        "basePower": 60,
        "category": "Special",
        "pp": 15,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Water"
    },
    "highjumpkick": {
        "accuracy": 90,
        "basePower": 130,
        "category": "Physical",
        "pp": 10,
        "priority": 0,
        "flags": {"contact", "protect", "mirror", "gravity"},
        "hasCustomRecoil": True,
        "secondary": False,
        "target": "normal",
        "type": "Fighting"
    },
    "holdback": {
        "accuracy": 100,
        "basePower": 40,
        "category": "Physical",
        "pp": 40,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "noFaint": True,
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "holdhands": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 40,
        "priority": 0,
        "flags": {"authentic"},
        "secondary": False,
        "target": "adjacentAlly",
        "type": "Normal"
    },
    "honeclaws": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 15,
        "priority": 0,
        "flags": {"snatch"},
        "boosts": {
            "atk": 1,
            "accuracy": 1
        },
        "secondary": False,
        "target": "self",
        "type": "Dark"
    },
    "hornattack": {
        "accuracy": 100,
        "basePower": 65,
        "category": "Physical",
        "pp": 25,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "horndrill": {
        "accuracy": 30,
        "basePower": 0,
        "category": "Physical",
        "pp": 5,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "ohko": True,
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "hornleech": {
        "accuracy": 100,
        "basePower": 75,
        "category": "Physical",
        "pp": 10,
        "priority": 0,
        "flags": {"contact", "protect", "mirror", "heal"},
        "drain": [1, 2],
        "secondary": False,
        "target": "normal",
        "type": "Grass"
    },
    "howl": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 40,
        "priority": 0,
        "flags": {"snatch"},
        "boosts": {
            "atk": 1
        },
        "secondary": False,
        "target": "self",
        "type": "Normal"
    },
    "hurricane": {
        "accuracy": 70,
        "basePower": 110,
        "category": "Special",
        "pp": 10,
        "priority": 0,
        "flags": {"protect", "mirror", "distance"},
        "secondary": {
            "chance": 30,
            "volatileStatus": 'confusion'
        },
        "target": "any",
        "type": "Flying"
    },
    "hydrocannon": {
        "accuracy": 90,
        "basePower": 150,
        "category": "Special",
        "pp": 5,
        "priority": 0,
        "flags": {"recharge", "protect", "mirror"},
        "self": {
            "volatileStatus": 'mustrecharge'
        },
        "secondary": False,
        "target": "normal",
        "type": "Water"
    },
    "hydropump": {
        "accuracy": 80,
        "basePower": 110,
        "category": "Special",
        "pp": 5,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Water"
    },
    "hyperbeam": {
        "accuracy": 90,
        "basePower": 150,
        "category": "Special",
        "pp": 5,
        "priority": 0,
        "flags": {"recharge", "protect", "mirror"},
        "self": {
            "volatileStatus": 'mustrecharge'
        },
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "hyperfang": {
        "accuracy": 90,
        "basePower": 80,
        "category": "Physical",
        "pp": 15,
        "priority": 0,
        "flags": {"bite", "contact", "protect", "mirror"},
        "secondary": {
            "chance": 10,
            "volatileStatus": 'flinch'
        },
        "target": "normal",
        "type": "Normal"
    },
    "hyperspacefury": {
        "accuracy": True,
        "basePower": 100,
        "category": "Physical",
        "pp": 5,
        "priority": 0,
        "flags": {"mirror", "authentic"},
        "isUnreleased": True,
        "breaksProtect": True,
        "self": {
            "boosts": {
                "def": -1
            }
        },
        "secondary": False,
        "target": "normal",
        "type": "Dark"
    },
    "hyperspacehole": {
        "accuracy": True,
        "basePower": 80,
        "category": "Special",
        "pp": 5,
        "priority": 0,
        "flags": {"mirror", "authentic"},
        "isUnreleased": True,
        "breaksProtect": True,
        "secondary": False,
        "target": "normal",
        "type": "Psychic"
    },
    "hypervoice": {
        "accuracy": 100,
        "basePower": 90,
        "category": "Special",
        "pp": 10,
        "priority": 0,
        "flags": {"protect", "mirror", "sound", "authentic"},
        "secondary": False,
        "target": "allAdjacentFoes",
        "type": "Normal"
    },
    "hypnosis": {
        "accuracy": 60,
        "basePower": 0,
        "category": "Status",
        "pp": 20,
        "priority": 0,
        "flags": {"protect", "reflectable", "mirror"},
        "status": 'slp',
        "secondary": False,
        "target": "normal",
        "type": "Psychic"
    },
    "iceball": {
        "accuracy": 90,
        "basePower": 30,
        "category": "Physical",
        "pp": 20,
        "priority": 0,
        "flags": {"bullet", "contact", "protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Ice"
    },
    "icebeam": {
        "accuracy": 100,
        "basePower": 90,
        "category": "Special",
        "pp": 10,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": {
            "chance": 10,
            "status": 'frz'
        },
        "target": "normal",
        "type": "Ice"
    },
    "iceburn": {
        "accuracy": 90,
        "basePower": 140,
        "category": "Special",
        "pp": 5,
        "priority": 0,
        "flags": {"charge", "protect", "mirror"},
        "secondary": {
            "chance": 30,
            "status": 'brn'
        },
        "target": "normal",
        "type": "Ice"
    },
    "icefang": {
        "accuracy": 95,
        "basePower": 65,
        "category": "Physical",
        "pp": 15,
        "priority": 0,
        "flags": {"bite", "contact", "protect", "mirror"},
        "secondary": [
            {
                "chance": 10,
                "status": 'frz'
            }, {
                "chance": 10,
                "volatileStatus": 'flinch'
            }
        ],
        "target": "normal",
        "type": "Ice"
    },
    "icepunch": {
        "accuracy": 100,
        "basePower": 75,
        "category": "Physical",
        "pp": 15,
        "priority": 0,
        "flags": {"contact", "protect", "mirror", "punch"},
        "secondary": {
            "chance": 10,
            "status": 'frz'
        },
        "target": "normal",
        "type": "Ice"
    },
    "iceshard": {
        "accuracy": 100,
        "basePower": 40,
        "category": "Physical",
        "pp": 30,
        "priority": 1,
        "flags": {"protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Ice"
    },
    "iciclecrash": {
        "accuracy": 90,
        "basePower": 85,
        "category": "Physical",
        "pp": 10,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": {
            "chance": 30,
            "volatileStatus": 'flinch'
        },
        "target": "normal",
        "type": "Ice"
    },
    "iciclespear": {
        "accuracy": 100,
        "basePower": 25,
        "category": "Physical",
        "pp": 30,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "multihit": [2, 5],
        "secondary": False,
        "target": "normal",
        "type": "Ice"
    },
    "icywind": {
        "accuracy": 95,
        "basePower": 55,
        "category": "Special",
        "pp": 15,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": {
            "chance": 100,
            "boosts": {
                "spe": -1
            }
        },
        "target": "allAdjacentFoes",
        "type": "Ice"
    },
    "imprison": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 10,
        "priority": 0,
        "flags": {"snatch", "authentic"},
        "volatileStatus": 'imprison',
        "secondary": False,
        "target": "self",
        "type": "Psychic"
    },
    "incinerate": {
        "accuracy": 100,
        "basePower": 60,
        "category": "Special",
        "pp": 15,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": False,
        "target": "allAdjacentFoes",
        "type": "Fire"
    },
    "inferno": {
        "accuracy": 50,
        "basePower": 100,
        "category": "Special",
        "pp": 5,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": {
            "chance": 100,
            "status": 'brn'
        },
        "target": "normal",
        "type": "Fire"
    },
    "infestation": {
        "accuracy": 100,
        "basePower": 20,
        "category": "Special",
        "pp": 20,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "volatileStatus": 'partiallytrapped',
        "secondary": False,
        "target": "normal",
        "type": "Bug"
    },
    "ingrain": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 20,
        "priority": 0,
        "flags": {"snatch", "nonsky"},
        "volatileStatus": 'ingrain',
        "secondary": False,
        "target": "self",
        "type": "Grass"
    },
    "iondeluge": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 25,
        "priority": 1,
        "flags": {},
        "pseudoWeather": 'iondeluge',
        "secondary": False,
        "target": "all",
        "type": "Electric"
    },
    "irondefense": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 15,
        "priority": 0,
        "flags": {"snatch"},
        "boosts": {
            "def": 2
        },
        "secondary": False,
        "target": "self",
        "type": "Steel"
    },
    "ironhead": {
        "accuracy": 100,
        "basePower": 80,
        "category": "Physical",
        "pp": 15,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "secondary": {
            "chance": 30,
            "volatileStatus": 'flinch'
        },
        "target": "normal",
        "type": "Steel"
    },
    "irontail": {
        "accuracy": 75,
        "basePower": 100,
        "category": "Physical",
        "pp": 15,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "secondary": {
            "chance": 30,
            "boosts": {
                "def": -1
            }
        },
        "target": "normal",
        "type": "Steel"
    },
    "judgment": {
        "accuracy": 100,
        "basePower": 100,
        "category": "Special",
        "pp": 10,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "jumpkick": {
        "accuracy": 95,
        "basePower": 100,
        "category": "Physical",
        "pp": 10,
        "priority": 0,
        "flags": {"contact", "protect", "mirror", "gravity"},
        "hasCustomRecoil": True,
        "secondary": False,
        "target": "normal",
        "type": "Fighting"
    },
    "karatechop": {
        "accuracy": 100,
        "basePower": 50,
        "category": "Physical",
        "pp": 25,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "critRatio": 2,
        "secondary": False,
        "target": "normal",
        "type": "Fighting"
    },
    "kinesis": {
        "accuracy": 80,
        "basePower": 0,
        "category": "Status",
        "pp": 15,
        "priority": 0,
        "flags": {"protect", "reflectable", "mirror"},
        "boosts": {
            "accuracy": -1
        },
        "secondary": False,
        "target": "normal",
        "type": "Psychic"
    },
    "kingsshield": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 10,
        "priority": 4,
        "flags": {},
        "stallingMove": True,
        "volatileStatus": 'kingsshield',
        "secondary": False,
        "target": "self",
        "type": "Steel"
    },
    "knockoff": {
        "accuracy": 100,
        "basePower": 65,
        "category": "Physical",
        "pp": 20,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Dark"
    },
    "landswrath": {
        "accuracy": 100,
        "basePower": 90,
        "category": "Physical",
        "pp": 10,
        "priority": 0,
        "flags": {"protect", "mirror", "nonsky"},
        "secondary": False,
        "target": "allAdjacentFoes",
        "type": "Ground"
    },
    "lastresort": {
        "accuracy": 100,
        "basePower": 140,
        "category": "Physical",
        "pp": 5,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "lavaplume": {
        "accuracy": 100,
        "basePower": 80,
        "category": "Special",
        "pp": 15,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": {
            "chance": 30,
            "status": 'brn'
        },
        "target": "allAdjacent",
        "type": "Fire"
    },
    "leafblade": {
        "accuracy": 100,
        "basePower": 90,
        "category": "Physical",
        "pp": 15,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "critRatio": 2,
        "secondary": False,
        "target": "normal",
        "type": "Grass"
    },
    "leafstorm": {
        "accuracy": 90,
        "basePower": 130,
        "category": "Special",
        "pp": 5,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "self": {
            "boosts": {
                "spa": -2
            }
        },
        "secondary": False,
        "target": "normal",
        "type": "Grass"
    },
    "leaftornado": {
        "accuracy": 90,
        "basePower": 65,
        "category": "Special",
        "pp": 10,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": {
            "chance": 50,
            "boosts": {
                "accuracy": -1
            }
        },
        "target": "normal",
        "type": "Grass"
    },
    "leechlife": {
        "accuracy": 100,
        "basePower": 20,
        "category": "Physical",
        "pp": 15,
        "priority": 0,
        "flags": {"contact", "protect", "mirror", "heal"},
        "drain": [1, 2],
        "secondary": False,
        "target": "normal",
        "type": "Bug"
    },
    "leechseed": {
        "accuracy": 90,
        "basePower": 0,
        "category": "Status",
        "pp": 10,
        "priority": 0,
        "flags": {"protect", "reflectable", "mirror"},
        "volatileStatus": 'leechseed',
        "secondary": False,
        "target": "normal",
        "type": "Grass"
    },
    "leer": {
        "accuracy": 100,
        "basePower": 0,
        "category": "Status",
        "pp": 30,
        "priority": 0,
        "flags": {"protect", "reflectable", "mirror"},
        "boosts": {
            "def": -1
        },
        "secondary": False,
        "target": "allAdjacentFoes",
        "type": "Normal"
    },
    "lick": {
        "accuracy": 100,
        "basePower": 30,
        "category": "Physical",
        "pp": 30,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "secondary": {
            "chance": 30,
            "status": 'par'
        },
        "target": "normal",
        "type": "Ghost"
    },
    "lightofruin": {
        "accuracy": 90,
        "basePower": 140,
        "category": "Special",
        "pp": 5,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "isUnreleased": True,
        "recoil": [1, 2],
        "secondary": False,
        "target": "normal",
        "type": "Fairy"
    },
    "lightscreen": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 30,
        "priority": 0,
        "flags": {"snatch"},
        "sidecondition": 'lightscreen',
        "secondary": False,
        "target": "allySide",
        "type": "Psychic"
    },
    "lockon": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 5,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "lovelykiss": {
        "accuracy": 75,
        "basePower": 0,
        "category": "Status",
        "pp": 10,
        "priority": 0,
        "flags": {"protect", "reflectable", "mirror"},
        "status": 'slp',
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "lowkick": {
        "accuracy": 100,
        "basePower": 0,
        "category": "Physical",
        "pp": 20,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Fighting"
    },
    "lowsweep": {
        "accuracy": 100,
        "basePower": 65,
        "category": "Physical",
        "pp": 20,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "secondary": {
            "chance": 100,
            "boosts": {
                "spe": -1
            }
        },
        "target": "normal",
        "type": "Fighting"
    },
    "luckychant": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 30,
        "priority": 0,
        "flags": {"snatch"},
        "sidecondition": 'luckychant',
        "secondary": False,
        "target": "allySide",
        "type": "Normal"
    },
    "lunardance": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 10,
        "priority": 0,
        "flags": {"snatch", "heal"},
        "selfdestruct": True,
        "sidecondition": 'lunardance',
        "secondary": False,
        "target": "self",
        "type": "Psychic"
    },
    "lusterpurge": {
        "accuracy": 100,
        "basePower": 70,
        "category": "Special",
        "pp": 5,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": {
            "chance": 50,
            "boosts": {
                "spd": -1
            }
        },
        "target": "normal",
        "type": "Psychic"
    },
    "machpunch": {
        "accuracy": 100,
        "basePower": 40,
        "category": "Physical",
        "pp": 30,
        "priority": 1,
        "flags": {"contact", "protect", "mirror", "punch"},
        "secondary": False,
        "target": "normal",
        "type": "Fighting"
    },
    "magiccoat": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 15,
        "priority": 4,
        "flags": {},
        "volatileStatus": 'magiccoat',
        "secondary": False,
        "target": "self",
        "type": "Psychic"
    },
    "magicroom": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 10,
        "priority": 0,
        "flags": {"mirror"},
        "secondary": False,
        "target": "all",
        "type": "Psychic"
    },
    "magicalleaf": {
        "accuracy": True,
        "basePower": 60,
        "category": "Special",
        "pp": 20,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Grass"
    },
    "magmastorm": {
        "accuracy": 75,
        "basePower": 100,
        "category": "Special",
        "pp": 5,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "volatileStatus": 'partiallytrapped',
        "secondary": False,
        "target": "normal",
        "type": "Fire"
    },
    "magnetbomb": {
        "accuracy": True,
        "basePower": 60,
        "category": "Physical",
        "pp": 20,
        "priority": 0,
        "flags": {"bullet", "protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Steel"
    },
    "magneticflux": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 20,
        "priority": 0,
        "flags": {"snatch", "distance", "authentic"},
        "secondary": False,
        "target": "allySide",
        "type": "Electric"
    },
    "magnetrise": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 10,
        "priority": 0,
        "flags": {"snatch", "gravity"},
        "volatileStatus": 'magnetrise',
        "secondary": False,
        "target": "self",
        "type": "Electric"
    },
    "magnitude": {
        "accuracy": 100,
        "basePower": 0,
        "category": "Physical",
        "pp": 30,
        "priority": 0,
        "flags": {"protect", "mirror", "nonsky"},
        "secondary": False,
        "target": "allAdjacent",
        "type": "Ground"
    },
    "matblock": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 10,
        "priority": 0,
        "flags": {"snatch", "nonsky"},
        "stallingMove": True,
        "volatileStatus": 'matblock',
        "secondary": False,
        "target": "allySide",
        "type": "Fighting"
    },
    "mefirst": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 20,
        "priority": 0,
        "flags": {"protect", "authentic"},
        "secondary": False,
        "target": "adjacentFoe",
        "type": "Normal"
    },
    "meanlook": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 5,
        "priority": 0,
        "flags": {"reflectable", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "meditate": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 40,
        "priority": 0,
        "flags": {"snatch"},
        "boosts": {
            "atk": 1
        },
        "secondary": False,
        "target": "self",
        "type": "Psychic"
    },
    "megadrain": {
        "accuracy": 100,
        "basePower": 40,
        "category": "Special",
        "pp": 15,
        "priority": 0,
        "flags": {"protect", "mirror", "heal"},
        "drain": [1, 2],
        "secondary": False,
        "target": "normal",
        "type": "Grass"
    },
    "megakick": {
        "accuracy": 75,
        "basePower": 120,
        "category": "Physical",
        "pp": 5,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "megapunch": {
        "accuracy": 85,
        "basePower": 80,
        "category": "Physical",
        "pp": 20,
        "priority": 0,
        "flags": {"contact", "protect", "mirror", "punch"},
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "megahorn": {
        "accuracy": 85,
        "basePower": 120,
        "category": "Physical",
        "pp": 10,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Bug"
    },
    "memento": {
        "accuracy": 100,
        "basePower": 0,
        "category": "Status",
        "pp": 10,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "boosts": {
            "atk": -2,
            "spa": -2
        },
        "selfdestruct": True,
        "secondary": False,
        "target": "normal",
        "type": "Dark"
    },
    "metalburst": {
        "accuracy": 100,
        "basePower": 0,
        "category": "Physical",
        "pp": 10,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": False,
        "target": "scripted",
        "type": "Steel"
    },
    "metalclaw": {
        "accuracy": 95,
        "basePower": 50,
        "category": "Physical",
        "pp": 35,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "secondary": {
            "chance": 10,
            "self": {
                "boosts": {
                    "atk": 1
                }
            }
        },
        "target": "normal",
        "type": "Steel"
    },
    "metalsound": {
        "accuracy": 85,
        "basePower": 0,
        "category": "Status",
        "pp": 40,
        "priority": 0,
        "flags": {"protect", "reflectable", "mirror", "sound", "authentic"},
        "boosts": {
            "spd": -2
        },
        "secondary": False,
        "target": "normal",
        "type": "Steel"
    },
    "meteormash": {
        "accuracy": 90,
        "basePower": 90,
        "category": "Physical",
        "pp": 10,
        "priority": 0,
        "flags": {"contact", "protect", "mirror", "punch"},
        "secondary": {
            "chance": 20,
            "self": {
                "boosts": {
                    "atk": 1
                }
            }
        },
        "target": "normal",
        "type": "Steel"
    },
    "metronome": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 10,
        "priority": 0,
        "flags": {},
        "secondary": False,
        "target": "self",
        "type": "Normal"
    },
    "milkdrink": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 10,
        "priority": 0,
        "flags": {"snatch", "heal"},
        "heal": [1, 2],
        "secondary": False,
        "target": "self",
        "type": "Normal"
    },
    "mimic": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 10,
        "priority": 0,
        "flags": {"protect", "authentic"},
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "mindreader": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 5,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "minimize": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 10,
        "priority": 0,
        "flags": {"snatch"},
        "volatileStatus": 'minimize',
        "boosts": {
            "evasion": 2
        },
        "secondary": False,
        "target": "self",
        "type": "Normal"
    },
    "miracleeye": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 40,
        "priority": 0,
        "flags": {"protect", "reflectable", "mirror", "authentic"},
        "volatileStatus": 'miracleeye',
        "secondary": False,
        "target": "normal",
        "type": "Psychic"
    },
    "mirrorcoat": {
        "accuracy": 100,
        "basePower": 0,
        "category": "Special",
        "pp": 20,
        "priority": -5,
        "flags": {"protect"},
        "secondary": False,
        "target": "scripted",
        "type": "Psychic"
    },
    "mirrormove": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 20,
        "priority": 0,
        "flags": {},
        "secondary": False,
        "target": "normal",
        "type": "Flying"
    },
    "mirrorshot": {
        "accuracy": 85,
        "basePower": 65,
        "category": "Special",
        "pp": 10,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": {
            "chance": 30,
            "boosts": {
                "accuracy": -1
            }
        },
        "target": "normal",
        "type": "Steel"
    },
    "mist": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 30,
        "priority": 0,
        "flags": {"snatch"},
        "sidecondition": 'mist',
        "secondary": False,
        "target": "allySide",
        "type": "Ice"
    },
    "mistball": {
        "accuracy": 100,
        "basePower": 70,
        "category": "Special",
        "pp": 5,
        "priority": 0,
        "flags": {"bullet", "protect", "mirror"},
        "secondary": {
            "chance": 50,
            "boosts": {
                "spa": -1
            }
        },
        "target": "normal",
        "type": "Psychic"
    },
    "mistyterrain": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 10,
        "priority": 0,
        "flags": {"nonsky"},
        "terrain": 'mistyterrain',
        "secondary": False,
        "target": "all",
        "type": "Fairy"
    },
    "moonblast": {
        "accuracy": 100,
        "basePower": 95,
        "category": "Special",
        "pp": 15,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": {
            "chance": 30,
            "boosts": {
                "spa": -1
            }
        },
        "target": "normal",
        "type": "Fairy"
    },
    "moonlight": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 5,
        "priority": 0,
        "flags": {"snatch", "heal"},
        "secondary": False,
        "target": "self",
        "type": "Fairy"
    },
    "morningsun": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 5,
        "priority": 0,
        "flags": {"snatch", "heal"},
        "secondary": False,
        "target": "self",
        "type": "Normal"
    },
    "mudslap": {
        "accuracy": 100,
        "basePower": 20,
        "category": "Special",
        "pp": 10,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": {
            "chance": 100,
            "boosts": {
                "accuracy": -1
            }
        },
        "target": "normal",
        "type": "Ground"
    },
    "mudbomb": {
        "accuracy": 85,
        "basePower": 65,
        "category": "Special",
        "pp": 10,
        "priority": 0,
        "flags": {"bullet", "protect", "mirror"},
        "secondary": {
            "chance": 30,
            "boosts": {
                "accuracy": -1
            }
        },
        "target": "normal",
        "type": "Ground"
    },
    "mudshot": {
        "accuracy": 95,
        "basePower": 55,
        "category": "Special",
        "pp": 15,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": {
            "chance": 100,
            "boosts": {
                "spe": -1
            }
        },
        "target": "normal",
        "type": "Ground"
    },
    "mudsport": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 15,
        "priority": 0,
        "flags": {"nonsky"},
        "secondary": False,
        "target": "all",
        "type": "Ground"
    },
    "muddywater": {
        "accuracy": 85,
        "basePower": 90,
        "category": "Special",
        "pp": 10,
        "priority": 0,
        "flags": {"protect", "mirror", "nonsky"},
        "secondary": {
            "chance": 30,
            "boosts": {
                "accuracy": -1
            }
        },
        "target": "allAdjacentFoes",
        "type": "Water"
    },
    "mysticalfire": {
        "accuracy": 100,
        "basePower": 65,
        "category": "Special",
        "pp": 10,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": {
            "chance": 100,
            "boosts": {
                "spa": -1
            }
        },
        "target": "normal",
        "type": "Fire"
    },
    "nastyplot": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 20,
        "priority": 0,
        "flags": {"snatch"},
        "boosts": {
            "spa": 2
        },
        "secondary": False,
        "target": "self",
        "type": "Dark"
    },
    "naturalgift": {
        "accuracy": 100,
        "basePower": 0,
        "category": "Physical",
        "pp": 15,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "naturepower": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 20,
        "priority": 0,
        "flags": {},
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "needlearm": {
        "accuracy": 100,
        "basePower": 60,
        "category": "Physical",
        "pp": 15,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "secondary": {
            "chance": 30,
            "volatileStatus": 'flinch'
        },
        "target": "normal",
        "type": "Grass"
    },
    "nightdaze": {
        "accuracy": 95,
        "basePower": 85,
        "category": "Special",
        "pp": 10,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": {
            "chance": 40,
            "boosts": {
                "accuracy": -1
            }
        },
        "target": "normal",
        "type": "Dark"
    },
    "nightshade": {
        "accuracy": 100,
        "basePower": 0,
        "damage": 'level',
        "category": "Special",
        "pp": 15,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Ghost"
    },
    "nightslash": {
        "accuracy": 100,
        "basePower": 70,
        "category": "Physical",
        "pp": 15,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "critRatio": 2,
        "secondary": False,
        "target": "normal",
        "type": "Dark"
    },
    "nightmare": {
        "accuracy": 100,
        "basePower": 0,
        "category": "Status",
        "pp": 15,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "volatileStatus": 'nightmare',
        "secondary": False,
        "target": "normal",
        "type": "Ghost"
    },
    "nobleroar": {
        "accuracy": 100,
        "basePower": 0,
        "category": "Status",
        "pp": 30,
        "priority": 0,
        "flags": {"protect", "reflectable", "mirror", "sound", "authentic"},
        "boosts": {
            "atk": -1,
            "spa": -1
        },
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "nuzzle": {
        "accuracy": 100,
        "basePower": 20,
        "category": "Physical",
        "pp": 20,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "secondary": {
            "chance": 100,
            "status": 'par'
        },
        "target": "normal",
        "type": "Electric"
    },
    "oblivionwing": {
        "accuracy": 100,
        "basePower": 80,
        "category": "Special",
        "pp": 10,
        "priority": 0,
        "flags": {"protect", "mirror", "distance", "heal"},
        "drain": [3, 4],
        "secondary": False,
        "target": "any",
        "type": "Flying"
    },
    "octazooka": {
        "accuracy": 85,
        "basePower": 65,
        "category": "Special",
        "pp": 10,
        "priority": 0,
        "flags": {"bullet", "protect", "mirror"},
        "secondary": {
            "chance": 50,
            "boosts": {
                "accuracy": -1
            }
        },
        "target": "normal",
        "type": "Water"
    },
    "odorsleuth": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 40,
        "priority": 0,
        "flags": {"protect", "reflectable", "mirror", "authentic"},
        "volatileStatus": 'foresight',
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "ominouswind": {
        "accuracy": 100,
        "basePower": 60,
        "category": "Special",
        "pp": 5,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": {
            "chance": 10,
            "self": {
                "boosts": {
                    "atk": 1,
                    "def": 1,
                    "spa": 1,
                    "spd": 1,
                    "spe": 1
                }
            }
        },
        "target": "normal",
        "type": "Ghost"
    },
    "originpulse": {
        "accuracy": 85,
        "basePower": 110,
        "category": "Special",
        "pp": 10,
        "priority": 0,
        "flags": {"protect", "pulse", "mirror"},
        "secondary": False,
        "target": "allAdjacentFoes",
        "type": "Water"
    },
    "outrage": {
        "accuracy": 100,
        "basePower": 120,
        "category": "Physical",
        "pp": 10,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "self": {
            "volatileStatus": 'lockedmove'
        },
        "secondary": False,
        "target": "randomNormal",
        "type": "Dragon"
    },
    "overheat": {
        "accuracy": 90,
        "basePower": 130,
        "category": "Special",
        "pp": 5,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "self": {
            "boosts": {
                "spa": -2
            }
        },
        "secondary": False,
        "target": "normal",
        "type": "Fire"
    },
    "painsplit": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 20,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "paraboliccharge": {
        "accuracy": 100,
        "basePower": 50,
        "category": "Special",
        "pp": 20,
        "priority": 0,
        "flags": {"protect", "mirror", "heal"},
        "drain": [1, 2],
        "secondary": False,
        "target": "allAdjacent",
        "type": "Electric"
    },
    "partingshot": {
        "accuracy": 100,
        "basePower": 0,
        "category": "Status",
        "pp": 20,
        "priority": 0,
        "flags": {"protect", "reflectable", "mirror", "sound", "authentic"},
        "selfSwitch": True,
        "boosts": {
            "atk": -1,
            "spa": -1
        },
        "secondary": False,
        "target": "normal",
        "type": "Dark"
    },
    "payday": {
        "accuracy": 100,
        "basePower": 40,
        "category": "Physical",
        "pp": 20,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "payback": {
        "accuracy": 100,
        "basePower": 50,
        "category": "Physical",
        "pp": 10,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Dark"
    },
    "peck": {
        "accuracy": 100,
        "basePower": 35,
        "category": "Physical",
        "pp": 35,
        "priority": 0,
        "flags": {"contact", "protect", "mirror", "distance"},
        "secondary": False,
        "target": "any",
        "type": "Flying"
    },
    "perishsong": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 5,
        "priority": 0,
        "flags": {"sound", "distance", "authentic"},        "secondary": False,
        "target": "all",
        "type": "Normal"
    },
    "petalblizzard": {
        "accuracy": 100,
        "basePower": 90,
        "category": "Physical",
        "pp": 15,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": False,
        "target": "allAdjacent",
        "type": "Grass"
    },
    "petaldance": {
        "accuracy": 100,
        "basePower": 120,
        "category": "Special",
        "pp": 10,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "self": {
            "volatileStatus": 'lockedmove'
        },
        "secondary": False,
        "target": "randomNormal",
        "type": "Grass"
    },
    "phantomforce": {
        "accuracy": 100,
        "basePower": 90,
        "category": "Physical",
        "pp": 10,
        "priority": 0,
        "flags": {"contact", "charge", "mirror"},
        "breaksProtect": True,        "secondary": False,
        "target": "normal",
        "type": "Ghost"
    },
    "pinmissile": {
        "accuracy": 95,
        "basePower": 25,
        "category": "Physical",
        "pp": 20,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "multihit": [2, 5],
        "secondary": False,
        "target": "normal",
        "type": "Bug"
    },
    "playnice": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 20,
        "priority": 0,
        "flags": {"reflectable", "mirror", "authentic"},
        "boosts": {
            "atk": -1
        },
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "playrough": {
        "accuracy": 90,
        "basePower": 90,
        "category": "Physical",
        "pp": 10,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "secondary": {
            "chance": 10,
            "boosts": {
                "atk": -1
            }
        },
        "target": "normal",
        "type": "Fairy"
    },
    "pluck": {
        "accuracy": 100,
        "basePower": 60,
        "category": "Physical",
        "pp": 20,
        "priority": 0,
        "flags": {"contact", "protect", "mirror", "distance"},
        "secondary": False,
        "target": "any",
        "type": "Flying"
    },
    "poisonfang": {
        "accuracy": 100,
        "basePower": 50,
        "category": "Physical",
        "pp": 15,
        "priority": 0,
        "flags": {"bite", "contact", "protect", "mirror"},
        "secondary": {
            "chance": 50,
            "status": 'tox'
        },
        "target": "normal",
        "type": "Poison"
    },
    "poisongas": {
        "accuracy": 90,
        "basePower": 0,
        "category": "Status",
        "pp": 40,
        "priority": 0,
        "flags": {"protect", "reflectable", "mirror"},
        "status": 'psn',
        "secondary": False,
        "target": "allAdjacentFoes",
        "type": "Poison"
    },
    "poisonjab": {
        "accuracy": 100,
        "basePower": 80,
        "category": "Physical",
        "pp": 20,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "secondary": {
            "chance": 30,
            "status": 'psn'
        },
        "target": "normal",
        "type": "Poison"
    },
    "poisonpowder": {
        "accuracy": 75,
        "basePower": 0,
        "category": "Status",
        "pp": 35,
        "priority": 0,
        "flags": {"powder", "protect", "reflectable", "mirror"},
        "status": 'psn',
        "secondary": False,
        "target": "normal",
        "type": "Poison"
    },
    "poisonsting": {
        "accuracy": 100,
        "basePower": 15,
        "category": "Physical",
        "pp": 35,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": {
            "chance": 30,
            "status": 'psn'
        },
        "target": "normal",
        "type": "Poison"
    },
    "poisontail": {
        "accuracy": 100,
        "basePower": 50,
        "category": "Physical",
        "pp": 25,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "critRatio": 2,
        "secondary": {
            "chance": 10,
            "status": 'psn'
        },
        "target": "normal",
        "type": "Poison"
    },
    "pound": {
        "accuracy": 100,
        "basePower": 40,
        "category": "Physical",
        "pp": 35,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "powder": {
        "accuracy": 100,
        "basePower": 0,
        "category": "Status",
        "pp": 20,
        "priority": 1,
        "flags": {"powder", "protect", "reflectable", "mirror", "authentic"},
        "volatileStatus": 'powder',
        "secondary": False,
        "target": "normal",
        "type": "Bug"
    },
    "powdersnow": {
        "accuracy": 100,
        "basePower": 40,
        "category": "Special",
        "pp": 25,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": {
            "chance": 10,
            "status": 'frz'
        },
        "target": "allAdjacentFoes",
        "type": "Ice"
    },
    "powergem": {
        "accuracy": 100,
        "basePower": 80,
        "category": "Special",
        "pp": 20,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Rock"
    },
    "powersplit": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 10,
        "priority": 0,
        "flags": {"protect"},
        "secondary": False,
        "target": "normal",
        "type": "Psychic"
    },
    "powerswap": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 10,
        "priority": 0,
        "flags": {"protect", "mirror", "authentic"},
        "secondary": False,
        "target": "normal",
        "type": "Psychic"
    },
    "powertrick": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 10,
        "priority": 0,
        "flags": {"snatch"},
        "volatileStatus": 'powertrick',
        "secondary": False,
        "target": "self",
        "type": "Psychic"
    },
    "poweruppunch": {
        "accuracy": 100,
        "basePower": 40,
        "category": "Physical",
        "pp": 20,
        "priority": 0,
        "flags": {"contact", "protect", "mirror", "punch"},
        "secondary": {
            "chance": 100,
            "self": {
                "boosts": {
                    "atk": 1
                }
            }
        },
        "target": "normal",
        "type": "Fighting"
    },
    "powerwhip": {
        "accuracy": 85,
        "basePower": 120,
        "category": "Physical",
        "pp": 10,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Grass"
    },
    "precipiceblades": {
        "accuracy": 85,
        "basePower": 120,
        "category": "Physical",
        "pp": 10,
        "priority": 0,
        "flags": {"protect", "mirror", "nonsky"},
        "target": "allAdjacentFoes",
        "type": "Ground"
    },
    "present": {
        "accuracy": 90,
        "basePower": 0,
        "category": "Physical",
        "pp": 15,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "protect": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 10,
        "priority": 4,
        "flags": {},
        "stallingMove": True,
        "volatileStatus": 'protect',
        "secondary": False,
        "target": "self",
        "type": "Normal"
    },
    "psybeam": {
        "accuracy": 100,
        "basePower": 65,
        "category": "Special",
        "pp": 20,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": {
            "chance": 10,
            "volatileStatus": 'confusion'
        },
        "target": "normal",
        "type": "Psychic"
    },
    "psychup": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 10,
        "priority": 0,
        "flags": {"authentic"},
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "psychic": {
        "accuracy": 100,
        "basePower": 90,
        "category": "Special",
        "pp": 10,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": {
            "chance": 10,
            "boosts": {
                "spd": -1
            }
        },
        "target": "normal",
        "type": "Psychic"
    },
    "psychoboost": {
        "accuracy": 90,
        "basePower": 140,
        "category": "Special",
        "pp": 5,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "self": {
            "boosts": {
                "spa": -2
            }
        },
        "secondary": False,
        "target": "normal",
        "type": "Psychic"
    },
    "psychocut": {
        "accuracy": 100,
        "basePower": 70,
        "category": "Physical",
        "pp": 20,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "critRatio": 2,
        "secondary": False,
        "target": "normal",
        "type": "Psychic"
    },
    "psychoshift": {
        "accuracy": 100,
        "basePower": 0,
        "category": "Status",
        "pp": 10,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Psychic"
    },
    "psyshock": {
        "accuracy": 100,
        "basePower": 80,
        "category": "Special",
        "defensivecategory": "Physical",
        "pp": 10,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Psychic"
    },
    "psystrike": {
        "accuracy": 100,
        "basePower": 100,
        "category": "Special",
        "defensivecategory": "Physical",
        "pp": 10,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Psychic"
    },
    "psywave": {
        "accuracy": 100,
        "basePower": 0,
        "category": "Special",
        "pp": 15,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Psychic"
    },
    "punishment": {
        "accuracy": 100,
        "basePower": 0,
        "category": "Physical",
        "pp": 5,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Dark"
    },
    "pursuit": {
        "accuracy": 100,
        "basePower": 40,
        "category": "Physical",
        "pp": 20,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Dark"
    },
    "quash": {
        "accuracy": 100,
        "basePower": 0,
        "category": "Status",
        "pp": 15,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Dark"
    },
    "quickattack": {
        "accuracy": 100,
        "basePower": 40,
        "category": "Physical",
        "pp": 30,
        "priority": 1,
        "flags": {"contact", "protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "quickguard": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 15,
        "priority": 3,
        "flags": {"snatch"},
        "sidecondition": 'quickguard',
        "secondary": False,
        "target": "allySide",
        "type": "Fighting"
    },
    "quiverdance": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 20,
        "priority": 0,
        "flags": {"snatch"},
        "boosts": {
            "spa": 1,
            "spd": 1,
            "spe": 1
        },
        "secondary": False,
        "target": "self",
        "type": "Bug"
    },
    "rage": {
        "accuracy": 100,
        "basePower": 20,
        "category": "Physical",
        "pp": 20,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "self": {
            "volatileStatus": 'rage'
        },
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "ragepowder": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 20,
        "priority": 2,
        "flags": {"powder"},
        "volatileStatus": 'ragepowder',
        "secondary": False,
        "target": "self",
        "type": "Bug"
    },
    "raindance": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 5,
        "priority": 0,
        "flags": {},
        "weather": 'RainDance',
        "secondary": False,
        "target": "all",
        "type": "Water"
    },
    "rapidspin": {
        "accuracy": 100,
        "basePower": 20,
        "category": "Physical",
        "pp": 40,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "clearHazards": True,
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "razorleaf": {
        "accuracy": 95,
        "basePower": 55,
        "category": "Physical",
        "pp": 25,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "critRatio": 2,
        "secondary": False,
        "target": "allAdjacentFoes",
        "type": "Grass"
    },
    "razorshell": {
        "accuracy": 95,
        "basePower": 75,
        "category": "Physical",
        "pp": 10,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "secondary": {
            "chance": 50,
            "boosts": {
                "def": -1
            }
        },
        "target": "normal",
        "type": "Water"
    },
    "razorwind": {
        "accuracy": 100,
        "basePower": 80,
        "category": "Special",
        "pp": 10,
        "priority": 0,
        "flags": {"charge", "protect", "mirror"},
        "critRatio": 2,
        "secondary": False,
        "target": "allAdjacentFoes",
        "type": "Normal"
    },
    "recover": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 10,
        "priority": 0,
        "flags": {"snatch", "heal"},
        "heal": [1, 2],
        "secondary": False,
        "target": "self",
        "type": "Normal"
    },
    "recycle": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 10,
        "priority": 0,
        "flags": {"snatch"},
        "secondary": False,
        "target": "self",
        "type": "Normal"
    },
    "reflect": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 20,
        "priority": 0,
        "flags": {"snatch"},
        "sidecondition": 'reflect',
        "secondary": False,
        "target": "allySide",
        "type": "Psychic"
    },
    "reflecttype": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 15,
        "priority": 0,
        "flags": {"protect", "authentic"},
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "refresh": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 20,
        "priority": 0,
        "flags": {"snatch"},
        "secondary": False,
        "target": "self",
        "type": "Normal"
    },
    "relicsong": {
        "accuracy": 100,
        "basePower": 75,
        "category": "Special",
        "pp": 10,
        "priority": 0,
        "flags": {"protect", "mirror", "sound", "authentic"},
        "secondary": {
            "chance": 10,
            "status": 'slp'
        },      "target": "allAdjacentFoes",
        "type": "Normal"
    },
    "rest": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 10,
        "priority": 0,
        "flags": {"snatch", "heal"},
        "secondary": False,
        "target": "self",
        "type": "Psychic"
    },
    "retaliate": {
        "accuracy": 100,
        "basePower": 70,
        "category": "Physical",
        "pp": 5,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "return": {
        "accuracy": 100,
        "basePower": 0,
        "category": "Physical",
        "pp": 20,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "revenge": {
        "accuracy": 100,
        "basePower": 60,
        "category": "Physical",
        "pp": 10,
        "priority": -4,
        "flags": {"contact", "protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Fighting"
    },
    "reversal": {
        "accuracy": 100,
        "basePower": 0,
        "category": "Physical",
        "pp": 15,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Fighting"
    },
    "roar": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 20,
        "priority": -6,
        "flags": {"reflectable", "mirror", "sound", "authentic"},
        "forceSwitch": True,
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "roaroftime": {
        "accuracy": 90,
        "basePower": 150,
        "category": "Special",
        "pp": 5,
        "priority": 0,
        "flags": {"recharge", "protect", "mirror"},
        "self": {
            "volatileStatus": 'mustrecharge'
        },
        "secondary": False,
        "target": "normal",
        "type": "Dragon"
    },
    "rockblast": {
        "accuracy": 90,
        "basePower": 25,
        "category": "Physical",
        "pp": 10,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "multihit": [2, 5],
        "secondary": False,
        "target": "normal",
        "type": "Rock"
    },
    "rockclimb": {
        "accuracy": 85,
        "basePower": 90,
        "category": "Physical",
        "pp": 20,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "secondary": {
            "chance": 20,
            "volatileStatus": 'confusion'
        },
        "target": "normal",
        "type": "Normal"
    },
    "rockpolish": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 20,
        "priority": 0,
        "flags": {"snatch"},
        "boosts": {
            "spe": 2
        },
        "secondary": False,
        "target": "self",
        "type": "Rock"
    },
    "rockslide": {
        "accuracy": 90,
        "basePower": 75,
        "category": "Physical",
        "pp": 10,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": {
            "chance": 30,
            "volatileStatus": 'flinch'
        },
        "target": "allAdjacentFoes",
        "type": "Rock"
    },
    "rocksmash": {
        "accuracy": 100,
        "basePower": 40,
        "category": "Physical",
        "pp": 15,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "secondary": {
            "chance": 50,
            "boosts": {
                "def": -1
            }
        },
        "target": "normal",
        "type": "Fighting"
    },
    "rockthrow": {
        "accuracy": 90,
        "basePower": 50,
        "category": "Physical",
        "pp": 15,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Rock"
    },
    "rocktomb": {
        "accuracy": 95,
        "basePower": 60,
        "category": "Physical",
        "pp": 15,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": {
            "chance": 100,
            "boosts": {
                "spe": -1
            }
        },
        "target": "normal",
        "type": "Rock"
    },
    "rockwrecker": {
        "accuracy": 90,
        "basePower": 150,
        "category": "Physical",
        "pp": 5,
        "priority": 0,
        "flags": {"bullet", "recharge", "protect", "mirror"},
        "self": {
            "volatileStatus": 'mustrecharge'
        },
        "secondary": False,
        "target": "normal",
        "type": "Rock"
    },
    "roleplay": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 10,
        "priority": 0,
        "flags": {"authentic"},     "secondary": False,
        "target": "normal",
        "type": "Psychic"
    },
    "rollingkick": {
        "accuracy": 85,
        "basePower": 60,
        "category": "Physical",
        "pp": 15,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "secondary": {
            "chance": 30,
            "volatileStatus": 'flinch'
        },
        "target": "normal",
        "type": "Fighting"
    },
    "rollout": {
        "accuracy": 90,
        "basePower": 30,
        "category": "Physical",
        "pp": 20,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Rock"
    },
    "roost": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 10,
        "priority": 0,
        "flags": {"snatch", "heal"},
        "heal": [1, 2],
        "self": {
            "volatileStatus": 'roost'
        },
        "secondary": False,
        "target": "self",
        "type": "Flying"
    },
    "rototiller": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 10,
        "priority": 0,
        "flags": {"distance", "nonsky"},
        "secondary": False,
        "target": "all",
        "type": "Ground"
    },
    "round": {
        "accuracy": 100,
        "basePower": 60,
        "category": "Special",
        "pp": 15,
        "priority": 0,
        "flags": {"protect", "mirror", "sound", "authentic"},
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "sacredfire": {
        "accuracy": 95,
        "basePower": 100,
        "category": "Physical",
        "pp": 5,
        "priority": 0,
        "flags": {"protect", "mirror", "defrost"},
        "secondary": {
            "chance": 50,
            "status": 'brn'
        },
        "target": "normal",
        "type": "Fire"
    },
    "sacredsword": {
        "accuracy": 100,
        "basePower": 90,
        "category": "Physical",
        "pp": 15,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "ignoreEvasion": True,
        "ignoreDefensive": True,
        "secondary": False,
        "target": "normal",
        "type": "Fighting"
    },
    "safeguard": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 25,
        "priority": 0,
        "flags": {"snatch"},
        "sidecondition": 'safeguard',
        "secondary": False,
        "target": "allySide",
        "type": "Normal"
    },
    "sandattack": {
        "accuracy": 100,
        "basePower": 0,
        "category": "Status",
        "pp": 15,
        "priority": 0,
        "flags": {"protect", "reflectable", "mirror"},
        "boosts": {
            "accuracy": -1
        },
        "secondary": False,
        "target": "normal",
        "type": "Ground"
    },
    "sandtomb": {
        "accuracy": 85,
        "basePower": 35,
        "category": "Physical",
        "pp": 15,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "volatileStatus": 'partiallytrapped',
        "secondary": False,
        "target": "normal",
        "type": "Ground"
    },
    "sandstorm": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 10,
        "priority": 0,
        "flags": {},
        "weather": 'Sandstorm',
        "secondary": False,
        "target": "all",
        "type": "Rock"
    },
    "scald": {
        "accuracy": 100,
        "basePower": 80,
        "category": "Special",
        "pp": 15,
        "priority": 0,
        "flags": {"protect", "mirror", "defrost"},
        "thawstarget": True,
        "secondary": {
            "chance": 30,
            "status": 'brn'
        },
        "target": "normal",
        "type": "Water"
    },
    "scaryface": {
        "accuracy": 100,
        "basePower": 0,
        "category": "Status",
        "pp": 10,
        "priority": 0,
        "flags": {"protect", "reflectable", "mirror"},
        "boosts": {
            "spe": -2
        },
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "scratch": {
        "accuracy": 100,
        "basePower": 40,
        "category": "Physical",
        "pp": 35,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "screech": {
        "accuracy": 85,
        "basePower": 0,
        "category": "Status",
        "pp": 40,
        "priority": 0,
        "flags": {"protect", "reflectable", "mirror", "sound", "authentic"},
        "boosts": {
            "def": -2
        },
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "searingshot": {
        "accuracy": 100,
        "basePower": 100,
        "category": "Special",
        "pp": 5,
        "priority": 0,
        "flags": {"bullet", "protect", "mirror"},
        "secondary": {
            "chance": 30,
            "status": 'brn'
        },
        "target": "allAdjacent",
        "type": "Fire"
    },
    "secretpower": {
        "accuracy": 100,
        "basePower": 70,
        "category": "Physical",
        "pp": 20,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": {
            "chance": 30,
            "status": 'par'
        },
        "target": "normal",
        "type": "Normal"
    },
    "secretsword": {
        "accuracy": 100,
        "basePower": 85,
        "category": "Special",
        "defensivecategory": "Physical",
        "pp": 10,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Fighting"
    },
    "seedbomb": {
        "accuracy": 100,
        "basePower": 80,
        "category": "Physical",
        "pp": 15,
        "priority": 0,
        "flags": {"bullet", "protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Grass"
    },
    "seedflare": {
        "accuracy": 85,
        "basePower": 120,
        "category": "Special",
        "pp": 5,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": {
            "chance": 40,
            "boosts": {
                "spd": -2
            }
        },
        "target": "normal",
        "type": "Grass"
    },
    "seismictoss": {
        "accuracy": 100,
        "basePower": 0,
        "damage": 'level',
        "category": "Physical",
        "pp": 20,
        "priority": 0,
        "flags": {"contact", "protect", "mirror", "nonsky"},
        "secondary": False,
        "target": "normal",
        "type": "Fighting"
    },
    "selfdestruct": {
        "accuracy": 100,
        "basePower": 200,
        "category": "Physical",
        "pp": 5,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "selfdestruct": True,
        "secondary": False,
        "target": "allAdjacent",
        "type": "Normal"
    },
    "shadowball": {
        "accuracy": 100,
        "basePower": 80,
        "category": "Special",
        "pp": 15,
        "priority": 0,
        "flags": {"bullet", "protect", "mirror"},
        "secondary": {
            "chance": 20,
            "boosts": {
                "spd": -1
            }
        },
        "target": "normal",
        "type": "Ghost"
    },
    "shadowclaw": {
        "accuracy": 100,
        "basePower": 70,
        "category": "Physical",
        "pp": 15,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "critRatio": 2,
        "secondary": False,
        "target": "normal",
        "type": "Ghost"
    },
    "shadowforce": {
        "accuracy": 100,
        "basePower": 120,
        "category": "Physical",
        "pp": 5,
        "priority": 0,
        "flags": {"contact", "charge", "mirror"},
        "breaksProtect": True,        "secondary": False,
        "target": "normal",
        "type": "Ghost"
    },
    "shadowpunch": {
        "accuracy": True,
        "basePower": 60,
        "category": "Physical",
        "pp": 20,
        "priority": 0,
        "flags": {"contact", "protect", "mirror", "punch"},
        "secondary": False,
        "target": "normal",
        "type": "Ghost"
    },
    "shadowsneak": {
        "accuracy": 100,
        "basePower": 40,
        "category": "Physical",
        "pp": 30,
        "priority": 1,
        "flags": {"contact", "protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Ghost"
    },
    "sharpen": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 30,
        "priority": 0,
        "flags": {"snatch"},
        "boosts": {
            "atk": 1
        },
        "secondary": False,
        "target": "self",
        "type": "Normal"
    },
    "sheercold": {
        "accuracy": 30,
        "basePower": 0,
        "category": "Special",
        "pp": 5,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": False,
        "ohko": True,
        "target": "normal",
        "type": "Ice"
    },
    "shellsmash": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 15,
        "priority": 0,
        "flags": {"snatch"},
        "boosts": {
            "atk": 2,
            "spa": 2,
            "spe": 2,
            "def": -1,
            "spd": -1
        },
        "secondary": False,
        "target": "self",
        "type": "Normal"
    },
    "shiftgear": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 10,
        "priority": 0,
        "flags": {"snatch"},
        "boosts": {
            "atk": 1,
            "spe": 2
        },
        "secondary": False,
        "target": "self",
        "type": "Steel"
    },
    "shockwave": {
        "accuracy": True,
        "basePower": 60,
        "category": "Special",
        "pp": 20,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Electric"
    },
    "signalbeam": {
        "accuracy": 100,
        "basePower": 75,
        "category": "Special",
        "pp": 15,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": {
            "chance": 10,
            "volatileStatus": 'confusion'
        },
        "target": "normal",
        "type": "Bug"
    },
    "silverwind": {
        "accuracy": 100,
        "basePower": 60,
        "category": "Special",
        "pp": 5,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": {
            "chance": 10,
            "self": {
                "boosts": {
                    "atk": 1,
                    "def": 1,
                    "spa": 1,
                    "spd": 1,
                    "spe": 1
                }
            }
        },
        "target": "normal",
        "type": "Bug"
    },
    "simplebeam": {
        "accuracy": 100,
        "basePower": 0,
        "category": "Status",
        "pp": 15,
        "priority": 0,
        "flags": {"protect", "reflectable", "mirror"},      "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "sing": {
        "accuracy": 55,
        "basePower": 0,
        "category": "Status",
        "pp": 15,
        "priority": 0,
        "flags": {"protect", "reflectable", "mirror", "sound", "authentic"},
        "status": 'slp',
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "sketch": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 1,
        "priority": 0,
        "flags": {"authentic"},
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "skillswap": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 10,
        "priority": 0,
        "flags": {"protect", "mirror", "authentic"},        "secondary": False,
        "target": "normal",
        "type": "Psychic"
    },
    "skullbash": {
        "accuracy": 100,
        "basePower": 130,
        "category": "Physical",
        "pp": 10,
        "priority": 0,
        "flags": {"contact", "charge", "protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "skyattack": {
        "accuracy": 90,
        "basePower": 140,
        "category": "Physical",
        "pp": 5,
        "priority": 0,
        "flags": {"charge", "protect", "mirror", "distance"},
        "critRatio": 2,
        "secondary": {
            "chance": 30,
            "volatileStatus": 'flinch'
        },
        "target": "any",
        "type": "Flying"
    },
    "skydrop": {
        "accuracy": 100,
        "basePower": 60,
        "category": "Physical",
        "pp": 10,
        "priority": 0,
        "flags": {"contact", "charge", "protect", "mirror", "gravity", "distance"},
        "secondary": False,
        "target": "any",
        "type": "Flying"
    },
    "skyuppercut": {
        "accuracy": 90,
        "basePower": 85,
        "category": "Physical",
        "pp": 15,
        "priority": 0,
        "flags": {"contact", "protect", "mirror", "punch"},
        "secondary": False,
        "target": "normal",
        "type": "Fighting"
    },
    "slackoff": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 10,
        "priority": 0,
        "flags": {"snatch", "heal"},
        "heal": [1, 2],
        "secondary": False,
        "target": "self",
        "type": "Normal"
    },
    "slam": {
        "accuracy": 75,
        "basePower": 80,
        "category": "Physical",
        "pp": 20,
        "priority": 0,
        "flags": {"contact", "protect", "mirror", "nonsky"},
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "slash": {
        "accuracy": 100,
        "basePower": 70,
        "category": "Physical",
        "pp": 20,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "critRatio": 2,
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "sleeppowder": {
        "accuracy": 75,
        "basePower": 0,
        "category": "Status",
        "pp": 15,
        "priority": 0,
        "flags": {"powder", "protect", "reflectable", "mirror"},
        "status": 'slp',
        "secondary": False,
        "target": "normal",
        "type": "Grass"
    },
    "sleeptalk": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 10,
        "priority": 0,
        "flags": {},
        "sleepUsable": True,
        "secondary": False,
        "target": "self",
        "type": "Normal"
    },
    "sludge": {
        "accuracy": 100,
        "basePower": 65,
        "category": "Special",
        "pp": 20,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": {
            "chance": 30,
            "status": 'psn'
        },
        "target": "normal",
        "type": "Poison"
    },
    "sludgebomb": {
        "accuracy": 100,
        "basePower": 90,
        "category": "Special",
        "pp": 10,
        "priority": 0,
        "flags": {"bullet", "protect", "mirror"},
        "secondary": {
            "chance": 30,
            "status": 'psn'
        },
        "target": "normal",
        "type": "Poison"
    },
    "sludgewave": {
        "accuracy": 100,
        "basePower": 95,
        "category": "Special",
        "pp": 10,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": {
            "chance": 10,
            "status": 'psn'
        },
        "target": "allAdjacent",
        "type": "Poison"
    },
    "smackdown": {
        "accuracy": 100,
        "basePower": 50,
        "category": "Physical",
        "pp": 15,
        "priority": 0,
        "flags": {"protect", "mirror", "nonsky"},
        "volatileStatus": 'smackdown',
        "secondary": False,
        "target": "normal",
        "type": "Rock"
    },
    "smellingsalts": {
        "accuracy": 100,
        "basePower": 70,
        "category": "Physical",
        "pp": 10,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "smog": {
        "accuracy": 70,
        "basePower": 30,
        "category": "Special",
        "pp": 20,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": {
            "chance": 40,
            "status": 'psn'
        },
        "target": "normal",
        "type": "Poison"
    },
    "smokescreen": {
        "accuracy": 100,
        "basePower": 0,
        "category": "Status",
        "pp": 20,
        "priority": 0,
        "flags": {"protect", "reflectable", "mirror"},
        "boosts": {
            "accuracy": -1
        },
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "snarl": {
        "accuracy": 95,
        "basePower": 55,
        "category": "Special",
        "pp": 15,
        "priority": 0,
        "flags": {"protect", "mirror", "sound", "authentic"},
        "secondary": {
            "chance": 100,
            "boosts": {
                "spa": -1
            }
        },
        "target": "allAdjacentFoes",
        "type": "Dark"
    },
    "snatch": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 10,
        "priority": 4,
        "flags": {"authentic"},
        "volatileStatus": 'snatch',
        "secondary": False,
        "target": "self",
        "type": "Dark"
    },
    "snore": {
        "accuracy": 100,
        "basePower": 50,
        "category": "Special",
        "pp": 15,
        "priority": 0,
        "flags": {"protect", "mirror", "sound", "authentic"},
        "sleepUsable": True,
        "secondary": {
            "chance": 30,
            "volatileStatus": 'flinch'
        },
        "target": "normal",
        "type": "Normal"
    },
    "spikyshield": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 10,
        "priority": 4,
        "flags": {},
        "stallingMove": True,
        "volatileStatus": 'spikyshield',
        "secondary": False,
        "target": "self",
        "type": "Grass"
    },
    "soak": {
        "accuracy": 100,
        "basePower": 0,
        "category": "Status",
        "pp": 20,
        "priority": 0,
        "flags": {"protect", "reflectable", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Water"
    },
    "softboiled": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 10,
        "priority": 0,
        "flags": {"snatch", "heal"},
        "heal": [1, 2],
        "secondary": False,
        "target": "self",
        "type": "Normal"
    },
    "solarbeam": {
        "accuracy": 100,
        "basePower": 120,
        "category": "Special",
        "pp": 10,
        "priority": 0,
        "flags": {"charge", "protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Grass"
    },
    "sonicboom": {
        "accuracy": 90,
        "basePower": 0,
        "damage": 20,
        "category": "Special",
        "pp": 20,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "spacialrend": {
        "accuracy": 95,
        "basePower": 100,
        "category": "Special",
        "pp": 5,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "critRatio": 2,
        "secondary": False,
        "target": "normal",
        "type": "Dragon"
    },
    "spark": {
        "accuracy": 100,
        "basePower": 65,
        "category": "Physical",
        "pp": 20,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "secondary": {
            "chance": 30,
            "status": 'par'
        },
        "target": "normal",
        "type": "Electric"
    },
    "spiderweb": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 10,
        "priority": 0,
        "flags": {"protect", "reflectable", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Bug"
    },
    "spikecannon": {
        "accuracy": 100,
        "basePower": 20,
        "category": "Physical",
        "pp": 15,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "multihit": [2, 5],
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "spikes": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 20,
        "priority": 0,
        "flags": {"reflectable", "nonsky"},
        "sidecondition": 'spikes',
        "secondary": False,
        "target": "foeSide",
        "type": "Ground"
    },
    "spitup": {
        "accuracy": 100,
        "basePower": 0,
        "category": "Special",
        "pp": 10,
        "priority": 0,
        "flags": {"protect"},       "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "spite": {
        "accuracy": 100,
        "basePower": 0,
        "category": "Status",
        "pp": 10,
        "priority": 0,
        "flags": {"protect", "reflectable", "mirror", "authentic"},
        "secondary": False,
        "target": "normal",
        "type": "Ghost"
    },
    "splash": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 40,
        "priority": 0,
        "flags": {"gravity"},
        "secondary": False,
        "target": "self",
        "type": "Normal"
    },
    "spore": {
        "accuracy": 100,
        "basePower": 0,
        "category": "Status",
        "pp": 15,
        "priority": 0,
        "flags": {"powder", "protect", "reflectable", "mirror"},
        "status": 'slp',
        "secondary": False,
        "target": "normal",
        "type": "Grass"
    },
    "stealthrock": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 20,
        "priority": 0,
        "flags": {"reflectable"},
        "sidecondition": 'stealthrock',
        "secondary": False,
        "target": "foeSide",
        "type": "Rock"
    },
    "steameruption": {
        "accuracy": 95,
        "basePower": 110,
        "category": "Special",
        "pp": 5,
        "priority": 0,
        "flags": {"protect", "mirror", "defrost"},
        "thawstarget": True,
        "isUnreleased": True,
        "secondary": {
            "chance": 30,
            "status": 'brn'
        },
        "target": "normal",
        "type": "Water"
    },
    "steelwing": {
        "accuracy": 90,
        "basePower": 70,
        "category": "Physical",
        "pp": 25,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "secondary": {
            "chance": 10,
            "self": {
                "boosts": {
                    "def": 1
                }
            }
        },
        "target": "normal",
        "type": "Steel"
    },
    "stickyweb": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 20,
        "priority": 0,
        "flags": {"reflectable"},
        "sidecondition": 'stickyweb',
        "secondary": False,
        "target": "foeSide",
        "type": "Bug"
    },
    "stockpile": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 20,
        "priority": 0,
        "flags": {"snatch"},
        "volatileStatus": 'stockpile',
        "secondary": False,
        "target": "self",
        "type": "Normal"
    },
    "stomp": {
        "accuracy": 100,
        "basePower": 65,
        "category": "Physical",
        "pp": 20,
        "priority": 0,
        "flags": {"contact", "protect", "mirror", "nonsky"},
        "secondary": {
            "chance": 30,
            "volatileStatus": 'flinch'
        },
        "target": "normal",
        "type": "Normal"
    },
    "stoneedge": {
        "accuracy": 80,
        "basePower": 100,
        "category": "Physical",
        "pp": 5,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "critRatio": 2,
        "secondary": False,
        "target": "normal",
        "type": "Rock"
    },
    "storedpower": {
        "accuracy": 100,
        "basePower": 20,
        "category": "Special",
        "pp": 10,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Psychic"
    },
    "stormthrow": {
        "accuracy": 100,
        "basePower": 60,
        "category": "Physical",
        "pp": 10,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "willCrit": True,
        "secondary": False,
        "target": "normal",
        "type": "Fighting"
    },
    "steamroller": {
        "accuracy": 100,
        "basePower": 65,
        "category": "Physical",
        "pp": 20,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "secondary": {
            "chance": 30,
            "volatileStatus": 'flinch'
        },
        "target": "normal",
        "type": "Bug"
    },
    "strength": {
        "accuracy": 100,
        "basePower": 80,
        "category": "Physical",
        "pp": 15,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "stringshot": {
        "accuracy": 95,
        "basePower": 0,
        "category": "Status",
        "pp": 40,
        "priority": 0,
        "flags": {"protect", "reflectable", "mirror"},
        "boosts": {
            "spe": -2
        },
        "secondary": False,
        "target": "allAdjacentFoes",
        "type": "Bug"
    },
    "struggle": {
        "accuracy": True,
        "basePower": 50,
        "category": "Physical",
        "pp": 1,
        "priority": 0,
        "flags": {"contact", "protect"},
	"hasCustomRecoil": True,
        "secondary": False,
        "target": "randomNormal",
        "type": "Normal"
    },
    "strugglebug": {
        "accuracy": 100,
        "basePower": 50,
        "category": "Special",
        "pp": 20,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": {
            "chance": 100,
            "boosts": {
                "spa": -1
            }
        },
        "target": "allAdjacentFoes",
        "type": "Bug"
    },
    "stunspore": {
        "accuracy": 75,
        "basePower": 0,
        "category": "Status",
        "pp": 30,
        "priority": 0,
        "flags": {"powder", "protect", "reflectable", "mirror"},
        "status": 'par',
        "secondary": False,
        "target": "normal",
        "type": "Grass"
    },
    "submission": {
        "accuracy": 80,
        "basePower": 80,
        "category": "Physical",
        "pp": 20,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "recoil": [1, 4],
        "secondary": False,
        "target": "normal",
        "type": "Fighting"
    },
    "substitute": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 10,
        "priority": 0,
        "flags": {"snatch", "nonsky"},
        "volatileStatus": 'Substitute',
        "secondary": False,
        "target": "self",
        "type": "Normal"
    },
    "suckerpunch": {
        "accuracy": 100,
        "basePower": 80,
        "category": "Physical",
        "pp": 5,
        "priority": 1,
        "flags": {"contact", "protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Dark"
    },
    "sunnyday": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 5,
        "priority": 0,
        "flags": {},
        "weather": 'sunnyday',
        "secondary": False,
        "target": "all",
        "type": "Fire"
    },
    "superfang": {
        "accuracy": 90,
        "basePower": 0,
        "category": "Physical",
        "pp": 10,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "superpower": {
        "accuracy": 100,
        "basePower": 120,
        "category": "Physical",
        "pp": 5,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "self": {
            "boosts": {
                "atk": -1,
                "def": -1
            }
        },
        "secondary": False,
        "target": "normal",
        "type": "Fighting"
    },
    "supersonic": {
        "accuracy": 55,
        "basePower": 0,
        "category": "Status",
        "pp": 20,
        "priority": 0,
        "flags": {"protect", "reflectable", "mirror", "sound", "authentic"},
        "volatileStatus": 'confusion',
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "surf": {
        "accuracy": 100,
        "basePower": 90,
        "category": "Special",
        "pp": 15,
        "priority": 0,
        "flags": {"protect", "mirror", "nonsky"},
        "secondary": False,
        "target": "allAdjacent",
        "type": "Water"
    },
    "swagger": {
        "accuracy": 90,
        "basePower": 0,
        "category": "Status",
        "pp": 15,
        "priority": 0,
        "flags": {"protect", "reflectable", "mirror"},
        "volatileStatus": 'confusion',
        "boosts": {
            "atk": 2
        },
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "swallow": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 10,
        "priority": 0,
        "flags": {"snatch", "heal"},        "secondary": False,
        "target": "self",
        "type": "Normal"
    },
    "sweetkiss": {
        "accuracy": 75,
        "basePower": 0,
        "category": "Status",
        "pp": 10,
        "priority": 0,
        "flags": {"protect", "reflectable", "mirror"},
        "volatileStatus": 'confusion',
        "secondary": False,
        "target": "normal",
        "type": "Fairy"
    },
    "sweetscent": {
        "accuracy": 100,
        "basePower": 0,
        "category": "Status",
        "pp": 20,
        "priority": 0,
        "flags": {"protect", "reflectable", "mirror"},
        "boosts": {
            "evasion": -2
        },
        "secondary": False,
        "target": "allAdjacentFoes",
        "type": "Normal"
    },
    "swift": {
        "accuracy": True,
        "basePower": 60,
        "category": "Special",
        "pp": 20,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": False,
        "target": "allAdjacentFoes",
        "type": "Normal"
    },
    "switcheroo": {
        "accuracy": 100,
        "basePower": 0,
        "category": "Status",
        "pp": 10,
        "priority": 0,
        "flags": {"protect", "mirror"},     "secondary": False,
        "target": "normal",
        "type": "Dark"
    },
    "swordsdance": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 20,
        "priority": 0,
        "flags": {"snatch"},
        "boosts": {
            "atk": 2
        },
        "secondary": False,
        "target": "self",
        "type": "Normal"
    },
    "synchronoise": {
        "accuracy": 100,
        "basePower": 120,
        "category": "Special",
        "pp": 10,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": False,
        "target": "allAdjacent",
        "type": "Psychic"
    },
    "synthesis": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 5,
        "priority": 0,
        "flags": {"snatch", "heal"},
        "secondary": False,
        "target": "self",
        "type": "Grass"
    },
    "tackle": {
        "accuracy": 100,
        "basePower": 50,
        "category": "Physical",
        "pp": 35,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "tailglow": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 20,
        "priority": 0,
        "flags": {"snatch"},
        "boosts": {
            "spa": 3
        },
        "secondary": False,
        "target": "self",
        "type": "Bug"
    },
    "tailslap": {
        "accuracy": 85,
        "basePower": 25,
        "category": "Physical",
        "pp": 10,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "multihit": [2, 5],
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "tailwhip": {
        "accuracy": 100,
        "basePower": 0,
        "category": "Status",
        "pp": 30,
        "priority": 0,
        "flags": {"protect", "reflectable", "mirror"},
        "boosts": {
            "def": -1
        },
        "secondary": False,
        "target": "allAdjacentFoes",
        "type": "Normal"
    },
    "tailwind": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 15,
        "priority": 0,
        "flags": {"snatch"},
        "sidecondition": 'tailwind',
        "secondary": False,
        "target": "allySide",
        "type": "Flying"
    },
    "takedown": {
        "accuracy": 85,
        "basePower": 90,
        "category": "Physical",
        "pp": 20,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "recoil": [1, 4],
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "taunt": {
        "accuracy": 100,
        "basePower": 0,
        "category": "Status",
        "pp": 20,
        "priority": 0,
        "flags": {"protect", "reflectable", "mirror", "authentic"},
        "volatileStatus": 'taunt',
        "secondary": False,
        "target": "normal",
        "type": "Dark"
    },
    "technoblast": {
        "accuracy": 100,
        "basePower": 120,
        "category": "Special",
        "pp": 5,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "teeterdance": {
        "accuracy": 100,
        "basePower": 0,
        "category": "Status",
        "pp": 20,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "volatileStatus": 'confusion',
        "secondary": False,
        "target": "allAdjacent",
        "type": "Normal"
    },
    "telekinesis": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 15,
        "priority": 0,
        "flags": {"protect", "reflectable", "mirror", "gravity"},
        "volatileStatus": 'telekinesis',
        "secondary": False,
        "target": "normal",
        "type": "Psychic"
    },
    "teleport": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 20,
        "priority": 0,
        "flags": {},
        "secondary": False,
        "target": "self",
        "type": "Psychic"
    },
    "thief": {
        "accuracy": 100,
        "basePower" : 60,
        "category": "Physical",
        "pp": 25,
        "priority": 0,
        "secondary": False,
        "target": "normal",
        "type": "Dark"
    },
    "thousandarrows": {
        "accuracy": 100,
        "basePower": 90,
        "category": "Physical",
        "pp": 10,
        "priority": 0,
        "volatileStatus": 'smackdown',
        "ignoreImmunity": {"Ground"},
        "secondary": False,
        "target": "allAdjacentFoes",
        "type": "Ground"
    },
    "thousandwaves": {
        "accuracy": 100,
        "basePower": 90,
        "category": "Physical",
        "pp": 10,
        "priority": 0,
        "flags": {"protect", "mirror", "nonsky"},
        "isUnreleased": True,
        "secondary": False,
        "target": "allAdjacentFoes",
        "type": "Ground"
    },
    "thrash": {
        "accuracy": 100,
        "basePower": 120,
        "category": "Physical",
        "pp": 10,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "self": {
            "volatileStatus": 'lockedmove'
        },
        "secondary": False,
        "target": "randomNormal",
        "type": "Normal"
    },
    "thunder": {
        "accuracy": 70,
        "basePower": 110,
        "category": "Special",
        "pp": 10,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": {
            "chance": 30,
            "status": 'par'
        },
        "target": "normal",
        "type": "Electric"
    },
    "thunderfang": {
        "accuracy": 95,
        "basePower": 65,
        "category": "Physical",
        "pp": 15,
        "priority": 0,
        "flags": {"bite", "contact", "protect", "mirror"},
        "secondary": [
            {
                "chance": 10,
                "status": 'par'
            }, {
                "chance": 10,
                "volatileStatus": 'flinch'
            }
        ],
        "target": "normal",
        "type": "Electric"
    },
    "thunderpunch": {
        "accuracy": 100,
        "basePower": 75,
        "category": "Physical",
        "pp": 15,
        "priority": 0,
        "flags": {"contact", "protect", "mirror", "punch"},
        "secondary": {
            "chance": 10,
            "status": 'par'
        },
        "target": "normal",
        "type": "Electric"
    },
    "thundershock": {
        "accuracy": 100,
        "basePower": 40,
        "category": "Special",
        "pp": 30,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": {
            "chance": 10,
            "status": 'par'
        },
        "target": "normal",
        "type": "Electric"
    },
    "thunderwave": {
        "accuracy": 100,
        "basePower": 0,
        "category": "Status",
        "pp": 20,
        "priority": 0,
        "flags": {"protect", "reflectable", "mirror"},
        "status": 'par',
        "ignoreImmunity": False,
        "secondary": False,
        "target": "normal",
        "type": "Electric"
    },
    "thunderbolt": {
        "accuracy": 100,
        "basePower": 90,
        "category": "Special",
        "pp": 15,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": {
            "chance": 10,
            "status": 'par'
        },
        "target": "normal",
        "type": "Electric"
    },
    "tickle": {
        "accuracy": 100,
        "basePower": 0,
        "category": "Status",
        "pp": 20,
        "priority": 0,
        "flags": {"protect", "reflectable", "mirror"},
        "boosts": {
            "atk": -1,
            "def": -1
        },
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "topsyturvy": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 20,
        "priority": 0,
        "flags": {"protect", "reflectable", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Dark"
    },
    "torment": {
        "accuracy": 100,
        "basePower": 0,
        "category": "Status",
        "pp": 15,
        "priority": 0,
        "flags": {"protect", "reflectable", "mirror", "authentic"},
        "volatileStatus": 'torment',
        "secondary": False,
        "target": "normal",
        "type": "Dark"
    },
    "toxic": {
        "accuracy": 90,
        "basePower": 0,
        "category": "Status",
        "pp": 10,
        "priority": 0,
        "flags": {"protect", "reflectable", "mirror"},
        "status": 'tox',
        "secondary": False,
        "target": "normal",
        "type": "Poison"
    },
    "toxicspikes": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 20,
        "priority": 0,
        "flags": {"reflectable", "nonsky"},
        "sidecondition": 'toxicspikes',
        "secondary": False,
        "target": "foeSide",
        "type": "Poison"
    },
    "transform": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 10,
        "priority": 0,
        "flags": {},
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "triattack": {
        "accuracy": 100,
        "basePower": 80,
        "category": "Special",
        "pp": 10,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": {
            "chance": 20,
            "status": ['brn', 'frz', 'par'],
        },
        "target": "normal",
        "type": "Normal"
    },
    "trick": {
        "accuracy": 100,
        "basePower": 0,
        "category": "Status",
        "pp": 10,
        "priority": 0,
        "flags": {"protect", "mirror"},     "secondary": False,
        "target": "normal",
        "type": "Psychic"
    },
    "trickortreat": {
        "accuracy": 100,
        "basePower": 0,
        "category": "Status",
        "pp": 20,
        "priority": 0,
        "flags": {"protect", "reflectable", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Ghost"
    },
    "trickroom": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 5,
        "priority": -7,
        "flags": {"mirror"},        "secondary": False,
        "target": "all",
        "type": "Psychic"
    },
    "triplekick": {
        "accuracy": 90,
        "basePower": 10,
        "category": "Physical",
        "pp": 10,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "multihit": [3, 3],
        "secondary": False,
        "target": "normal",
        "type": "Fighting"
    },
    "trumpcard": {
        "accuracy": True,
        "basePower": 0,
        "category": "Special",
        "pp": 5,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "twineedle": {
        "accuracy": 100,
        "basePower": 25,
        "category": "Physical",
        "pp": 20,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "multihit": [2, 2],
        "secondary": {
            "chance": 20,
            "status": 'psn'
        },
        "target": "normal",
        "type": "Bug"
    },
    "twister": {
        "accuracy": 100,
        "basePower": 40,
        "category": "Special",
        "pp": 20,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": {
            "chance": 20,
            "volatileStatus": 'flinch'
        },
        "target": "allAdjacentFoes",
        "type": "Dragon"
    },
    "uturn": {
        "accuracy": 100,
        "basePower": 70,
        "category": "Physical",
        "pp": 20,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "selfSwitch": True,
        "secondary": False,
        "target": "normal",
        "type": "Bug"
    },
    "uproar": {
        "accuracy": 100,
        "basePower": 90,
        "category": "Special",
        "pp": 10,
        "priority": 0,
        "flags": {"protect", "mirror", "sound", "authentic"},
        "self": {
            "volatileStatus": 'uproar'
        },
        "secondary": False,
        "target": "randomNormal",
        "type": "Normal"
    },
    "vcreate": {
        "accuracy": 95,
        "basePower": 180,
        "category": "Physical",
        "pp": 5,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "self": {
            "boosts": {
                "def": -1,
                "spd": -1,
                "spe": -1
            }
        },
        "secondary": False,
        "target": "normal",
        "type": "Fire"
    },
    "vacuumwave": {
        "accuracy": 100,
        "basePower": 40,
        "category": "Special",
        "pp": 30,
        "priority": 1,
        "flags": {"protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Fighting"
    },
    "venomdrench": {
        "accuracy": 100,
        "basePower": 0,
        "category": "Status",
        "pp": 20,
        "priority": 0,
        "flags": {"protect", "reflectable", "mirror"},
        "secondary": False,
        "target": "allAdjacentFoes",
        "type": "Poison"
    },
    "venoshock": {
        "accuracy": 100,
        "basePower": 65,
        "category": "Special",
        "pp": 10,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Poison"
    },
    "vicegrip": {
        "accuracy": 100,
        "basePower": 55,
        "category": "Physical",
        "pp": 30,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "vinewhip": {
        "accuracy": 100,
        "basePower": 45,
        "category": "Physical",
        "pp": 25,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Grass"
    },
    "vitalthrow": {
        "accuracy": True,
        "basePower": 70,
        "category": "Physical",
        "pp": 10,
        "priority": -1,
        "flags": {"contact", "protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Fighting"
    },
    "voltswitch": {
        "accuracy": 100,
        "basePower": 70,
        "category": "Special",
        "pp": 20,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "selfSwitch": True,
        "secondary": False,
        "target": "normal",
        "type": "Electric"
    },
    "volttackle": {
        "accuracy": 100,
        "basePower": 120,
        "category": "Physical",
        "pp": 15,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "recoil": [33, 100],
        "secondary": {
            "chance": 10,
            "status": 'par'
        },
        "target": "normal",
        "type": "Electric"
    },
    "wakeupslap": {
        "accuracy": 100,
        "basePower": 70,
        "category": "Physical",
        "pp": 10,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Fighting"
    },
    "watergun": {
        "accuracy": 100,
        "basePower": 40,
        "category": "Special",
        "pp": 25,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Water"
    },
    "waterpledge": {
        "accuracy": 100,
        "basePower": 80,
        "category": "Special",
        "pp": 10,
        "priority": 0,
        "flags": {"protect", "mirror", "nonsky"},
        "secondary": False,
        "target": "normal",
        "type": "Water"
    },
    "waterpulse": {
        "accuracy": 100,
        "basePower": 60,
        "category": "Special",
        "pp": 20,
        "priority": 0,
        "flags": {"protect", "pulse", "mirror", "distance"},
        "secondary": {
            "chance": 20,
            "volatileStatus": 'confusion'
        },
        "target": "any",
        "type": "Water"
    },
    "watersport": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 15,
        "priority": 0,
        "flags": {"nonsky"},
        "secondary": False,
        "target": "all",
        "type": "Water"
    },
    "waterspout": {
        "accuracy": 100,
        "basePower": 150,
        "category": "Special",
        "pp": 5,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": False,
        "target": "allAdjacentFoes",
        "type": "Water"
    },
    "waterfall": {
        "accuracy": 100,
        "basePower": 80,
        "category": "Physical",
        "pp": 15,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "secondary": {
            "chance": 20,
            "volatileStatus": 'flinch'
        },
        "target": "normal",
        "type": "Water"
    },
    "watershuriken": {
        "accuracy": 100,
        "basePower": 15,
        "category": "Physical",
        "pp": 20,
        "priority": 1,
        "flags": {"protect", "mirror"},
        "multihit": [2, 5],
        "secondary": False,
        "target": "normal",
        "type": "Water"
    },
    "weatherball": {
        "accuracy": 100,
        "basePower": 50,
        "category": "Special",
        "pp": 10,
        "priority": 0,
        "flags": {"bullet", "protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "whirlpool": {
        "accuracy": 85,
        "basePower": 35,
        "category": "Special",
        "pp": 15,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "volatileStatus": 'partiallytrapped',
        "secondary": False,
        "target": "normal",
        "type": "Water"
    },
    "whirlwind": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 20,
        "priority": -6,
        "flags": {"reflectable", "mirror", "authentic"},
        "forceSwitch": True,
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "wideguard": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 10,
        "priority": 3,
        "flags": {"snatch"},
        "sidecondition": 'wideguard',
        "secondary": False,
        "target": "allySide",
        "type": "Rock"
    },
    "wildcharge": {
        "accuracy": 100,
        "basePower": 90,
        "category": "Physical",
        "pp": 15,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "recoil": [1, 4],
        "secondary": False,
        "target": "normal",
        "type": "Electric"
    },
    "willowisp": {
        "accuracy": 85,
        "basePower": 0,
        "category": "Status",
        "pp": 15,
        "priority": 0,
        "flags": {"protect", "reflectable", "mirror"},
        "status": 'brn',
        "secondary": False,
        "target": "normal",
        "type": "Fire"
    },
    "wingattack": {
        "accuracy": 100,
        "basePower": 60,
        "category": "Physical",
        "pp": 35,
        "priority": 0,
        "flags": {"contact", "protect", "mirror", "distance"},
        "secondary": False,
        "target": "any",
        "type": "Flying"
    },
    "wish": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 10,
        "priority": 0,
        "flags": {"snatch", "heal"},
        "sidecondition": 'Wish',
        "secondary": False,
        "target": "self",
        "type": "Normal"
    },
    "withdraw": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 40,
        "priority": 0,
        "flags": {"snatch"},
        "boosts": {
            "def": 1
        },
        "secondary": False,
        "target": "self",
        "type": "Water"
    },
    "wonderroom": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 10,
        "priority": 0,
        "flags": {"mirror"},
        "secondary": False,
        "target": "all",
        "type": "Psychic"
    },
    "woodhammer": {
        "accuracy": 100,
        "basePower": 120,
        "category": "Physical",
        "pp": 15,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "recoil": [33, 100],
        "secondary": False,
        "target": "normal",
        "type": "Grass"
    },
    "workup": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 30,
        "priority": 0,
        "flags": {"snatch"},
        "boosts": {
            "atk": 1,
            "spa": 1
        },
        "secondary": False,
        "target": "self",
        "type": "Normal"
    },
    "worryseed": {
        "accuracy": 100,
        "basePower": 0,
        "category": "Status",
        "pp": 10,
        "priority": 0,
        "flags": {"protect", "reflectable", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Grass"
    },
    "wrap": {
        "accuracy": 90,
        "basePower": 15,
        "category": "Physical",
        "pp": 20,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "volatileStatus": 'partiallytrapped',
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "wringout": {
        "accuracy": 100,
        "basePower": 0,
        "category": "Special",
        "pp": 5,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "xscissor": {
        "accuracy": 100,
        "basePower": 80,
        "category": "Physical",
        "pp": 15,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "secondary": False,
        "target": "normal",
        "type": "Bug"
    },
    "yawn": {
        "accuracy": True,
        "basePower": 0,
        "category": "Status",
        "pp": 10,
        "priority": 0,
        "flags": {"protect", "reflectable", "mirror"},
        "volatileStatus": 'yawn',
        "secondary": False,
        "target": "normal",
        "type": "Normal"
    },
    "zapcannon": {
        "accuracy": 50,
        "basePower": 120,
        "category": "Special",
        "pp": 5,
        "priority": 0,
        "flags": {"bullet", "protect", "mirror"},
        "secondary": {
            "chance": 100,
            "status": 'par'
        },
        "target": "normal",
        "type": "Electric"
    },
    "zenheadbutt": {
        "accuracy": 90,
        "basePower": 80,
        "category": "Physical",
        "pp": 15,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "secondary": {
            "chance": 20,
            "volatileStatus": 'flinch'
        },
        "target": "normal",
        "type": "Psychic"
    },
    "paleowave": {
        "accuracy": 100,
        "basePower": 85,
        "category": "Special",
        "isNonstandard": True,
        "pp": 15,
        "priority": 0,
        "flags": {"protect", "mirror"},
        "secondary": {
            "chance": 20,
            "boosts": {
                "atk": -1
            }
        },
        "target": "normal",
        "type": "Rock"
    },
    "shadowstrike": {
        "accuracy": 95,
        "basePower": 80,
        "category": "Physical",
        "isNonstandard": True,
        "pp": 10,
        "priority": 0,
        "flags": {"contact", "protect", "mirror"},
        "secondary": {
            "chance": 50,
            "boosts": {
                "def": -1
            }
        },
        "target": "normal",
        "type": "Ghost"
    },
    "magikarpsrevenge": {
        "accuracy": True,
        "basePower": 120,
        "category": "Physical",
        "isNonstandard": True,
        "pp": 10,
        "priority": 0,
        "flags": {"contact", "recharge", "protect", "mirror"},
        "drain": [1, 2],
        "self": {
            "volatileStatus": 'mustrecharge'
        },
        "secondary": {
            "chance": 100,
            "volatileStatus": 'confusion',
            "boosts": {
                "def": -1,
                "spa": -1
            }
        },
        "target": "normal",
        "type": "Water"
    }
}
