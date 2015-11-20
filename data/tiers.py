formats = {'uber','ou','uu','ru','nu','pu','lc','monotype','cap', 'cc'}
tiers = {
'uberpoke':{"Groudon-Primal","Arceus","Ho-Oh","Salamence-Mega","Xerneas","Arceus-Ground","Darkrai","Gengar-Mega","Lugia","Arceus-Ghost","Arceus-Water","Latios","Klefki","Sableye-Mega","Arceus-Rock","Deoxys-Attack","Deoxys-Speed","Dialga","Mewtwo","Rayquaza","Yveltal","Diancie-Mega","Excadrill","Ferrothorn","Giratina-Origin","Kyogre-Primal","Latias","Mewtwo-Mega-X","Mewtwo-Mega-Y","Skarmory","Shaymin-Sky","Tyranitar","Aegislash","Blissey","Clefable","Groudon","Kangaskhan-Mega","Wobbuffet","Zekrom","Arceus-Dark","Arceus-Dragon","Blaziken","Blaziken-Mega","Bronzong","Lucario-Mega","Metagross-Mega","Scizor-Mega","Aerodactyl-Mega","Alomomola","Arceus-Ice","Arceus-Fairy","Cloyster","Forretress","Genesect","Greninja","Jirachi","Kyurem-White","Slowbro-Mega","Scolipede","Tentacruel"},
'oupoke':{"Charizard-Mega-X","Clefable","Hoopa-Unbound","Manaphy","Alakazam-Mega","Altaria-Mega","Azumarill","Bisharp","Diancie-Mega","Excadrill","Ferrothorn","Garchomp","Heatran","Hippowdon","Keldeo","Landorus-Therian","Lopunny-Mega","Latios","Metagross-Mega","Sableye-Mega","Scizor-Mega","Talonflame","Thundurus","Tornadus-Therian","Weavile","Charizard-Mega-Y","Gardevoir-Mega","Gengar","Gliscor","Gyarados-Mega","Kyurem-B","Latias","Manectric-Mega","Mew","Skarmory","Slowbro","Slowbro-Mega","Tyranitar","Venusaur-Mega","Aerodactyl-Mega","Alakazam","Celebi","Gyarados","Jirachi","Klefki","Magnezone","Medicham-Mega","Pinsir-Mega","Politoed","Raikou","Rotom-Wash","Serperior","Starmie","Volcarona","Breloom","Diggersby","Dragalge","Dragonite","Feraligatr","Gallade-Mega","Heracross-Mega","Kabutops","Kingdra","Latias-Mega","Mamoswine","Slowking","Suicune","Swampert-Mega","Terrakion","Togekiss","Victini","Beedrill-Mega","Chansey","Empoleon","Garchomp-Mega","Gothitelle","Hawlucha","Hydreigon","Omastar","Quagsire","Reuniclus","Sceptile-Mega","Scizor","Scolipede","Sharpedo-Mega","Tangrowth","Tyranitar-Mega","Zapdos","Amoonguss","Azelf","Chesnaught","Crawdaunt","Gastrodon","Lucario","Magneton","Mandibuzz","Pidgeot-Mega","Sylveon","Tentacruel","Thundurus-Therian","Toxicroak","Tyrantrum","Alomomola","Ampharos-Mega","Blastoise-Mega","Bronzong","Cobalion","Conkeldurr","Entei","Houndoom-Mega","Infernape","Kyurem","Metagross","Nidoking","Rhyperior","Seismitoad","Staraptor","Wobbuffet"},
'bl':{},
'uupoke':{"Feraligatr","Zapdos","Hydreigon","Reuniclus","Salamence","Suicune","Aerodactyl-Mega","Beedrill-Mega","Cobalion","Entei","Florges","Krookodile","Mamoswine","Sharpedo-Mega","Swampert-Mega","Abomasnow-Mega","Azelf","Blastoise-Mega","Chandelure","Cresselia","Crobat","Doublade","Empoleon","Heracross","Mandibuzz","Mienshao","Nidoqueen","Porygon2","Shaymin","Slowking","Snorlax","Whimsicott","Aggron-Mega","Ampharos-Mega","Dragalge","Forretress","Infernape","Kyurem","Lucario","Machamp","Rotom-Mow","Slurpuff","Swampert","Toxicroak","Tyrantrum","Arcanine","Bronzong","Chesnaught","Darmanitan","Froslass","Galvantula","Gligar","Heliolisk","Haxorus","Jellicent","Moltres","Nidoking","Porygon-Z","Qwilfish","Roserade","Rotom-Heat","Sceptile-Mega","Tangrowth","Tentacruel","Tornadus","Umbreon","Venomoth","Yanmega","Absol-Mega","Alomomola","Aromatisse","Blissey","Camerupt-Mega","Dugtrio","Escavalier","Honchkrow","Houndoom-Mega","Magneton","Meloetta","Noivern","Pangoro","Rhyperior","Seismitoad","Sharpedo","Aerodactyl","Amoonguss","Blastoise","Donphan","Fletchinder","Goodra","Granbull","Kingdra","Steelix-Mega","Vaporeon","Virizion","Zoroark","Cloyster","Cofagrigus","Drapion","Durant","Espeon","Glalie-Mega","Gourgeist-Super","Hitmonlee","Milotic","Mismagius","Poliwrath","Quagsire","Registeel","Shuckle","Smeargle","Spiritomb","Togetic","Weezing","Xatu"},
'bl2':{},
'rupoke':{"Steelix-Mega","Abomasnow","Slowking","Granbull","Alomomola","Durant","Emboar","Flygon","Glalie-Mega","Meloetta","Scrafty","Sigilyph","Tangrowth","Tyrantrum","Virizion","Aromatisse","Bronzong","Camerupt-Mega","Delphox","Escavalier","Fletchinder","Hitmonlee","Houndoom","Jellicent","Qwilfish","Rhyperior","Rotom-Mow","Seismitoad","Sneasel","Drapion","Druddigon","Dugtrio","Exploud","Gallade","Gurdurr","Jolteon","Mesprit","Quagsire","Samurott","Sawk","Spiritomb","Togetic","Uxie","Accelgor","Amoonguss","Audino-Mega","Audino","Braviary","Clawitzer","Eelektross","Golbat","Gourgeist-Super","Granbull","Hitmontop","Jynx","Malamar","Piloswine","Poliwrath","Torterra","Vivillon","Xatu","Archeops","Banette-Mega","Cofagrigus","Gastrodon","Gourgeist-Small","Kabutops","Lanturn","Magneton","Musharna","Omastar","Pelipper","Registeel","Roselia","Rotom-Frost","Shiftry","Skuntank","Weezing","Zangoose"},
'bl3':{},
'nupoke':{"Archeops","Tauros","Audino-Mega","Garbodor","Kabutops","Kangaskhan","Lanturn","Lilligant","Mawile","Mesprit","Sawk","Xatu","Carracosta","Gurdurr","Klinklang","Ludicolo","Magmortar","Malamar","Musharna","Pyroar","Samurott","Scyther","Torterra","Aurorus","Cacturne","Electivire","Exeggutor","Gourgeist-Small","Jynx","Hitmonchan","Liepard","Quagsire","Regirock","Rhydon","Rotom","Swellow","Barbaracle","Claydol","Ferroseed","Floatzel","Gorebyss","Hariyama","Haunter","Huntail","Mismagius","Shiftry","Pawniard","Skuntank","Piloswine","Prinplup","Tangela","Weezing","Vivillon","Zangoose","Bouffalant","Crustle","Cryogonal","Golurk","Gourgeist-Super","Kecleon","Leafeon","Ninetales","Pelipper","Poliwrath","Rotom-Fan","Stunfisk","Vileplume","Articuno","Flareon","Mantine","Primeape","Rampardos","Roselia","Sandslash","Swanna","Ursaring","Vanilluxe","Arbok","Audino","Avalugg","Beheeyem","Chatot","Cradily","Dodrio","Drifblim","Fraxure","Gogoat","Golem","Grumpig","Jumpluff","Kadabra","Meowstic","Miltank","Muk","Ninjask","Probopass","Raichu","Rapidash","Rotom-Frost","Sawsbuck","Servine","Simipour","Stoutland","Victreebel","Zebstrika","Zweilous","Carbink","Ditto","Dusknoir","Frogadier","Kricketune","Lampent","Leavanny","Lickilicky","Linoone","Marowak","Misdreavus","Mr. Mime","Quilladin","Regice","Shedinja","Simisage","Basculin","Delibird","Heatmor","Hippopotas","Kingler","Lapras","Metang","Monferno","Volbeat","Vullaby"},
'bl4':{},
'pupoke':{"Roselia","Exeggutor","Pawniard","Gorebyss","Gothitelle","Bouffalant","Floatzel","Simipour","Jumpluff","Zebstrika","Kadabra","Dodrio","Rapidash","Tangela","Raichu","Stoutland","Ursaring","Grumpig","Regice","Fraxure","Probopass","Sawsbuck","Stunfisk","Ninetales","Misdreavus","Simisage","Machoke","Mr. Mime","Mightyena","Clefairy","Arbok","Articuno","Duosion","Golduck","Golem","Gourgeist-Super","Pelipper","Rotom-Frost","Simisear","Swanna","Vigoroth","Basculin","Chatot","Gabite","Gogoat","Gourgeist-Small","Klang","Leafeon","Leavanny","Lickilicky","Linoone","Metang","Monferno","Ninjask","Politoed","Purugly","Venipede","Volbeat","Armaldo","Beheeyem","Ditto","Dusknoir","Hippopotas","Meowstic","Murkrow","Quilladin","Vibrava","Vullaby","Whirlipede","Zweilous","Avalugg","Beartic","Furfrou","Hypno","Luxray","Marowak","Munchlax","Persian","Rampardos","Regigigas","Servine","Solrock","Weepinbell"},
'lcpoke':{"Mienfoo","Pawniard","Abra","Timburr","Diglett","Fletchling","Magnemite","Porygon","Spritzee","Archen","Chinchou","Drilbur","Ferroseed","Gastly","Ponyta","Snubbull","Staryu","Vullaby","Vulpix","Carvanha","Cottonee","Drifloon","Foongus","Gothita","Houndour","Larvesta","Omanyte","Pumpkaboo-Super","Snivy","Shellder","Skrelp","Bellsprout","Bunnelby","Corphish","Croagunk","Dwebble","Hippopotas","Munchlax","Pancham","Tirtouga","Zigzagoon","Cranidos","Doduo","Elekid","Onix","Riolu","Scraggy","Stunky","Surskit","Taillow","Torchic","Aipom","Amaura","Chespin","Lickitung","Pumpkaboo-Small","Shellos","Slowpoke","Tentacool","Aron","Axew","Binacle","Buneary","Darumaka","Frillish","Honedge","Inkay","Koffing","Lileep","Magby","Numel","Snover","Trubbish","Tyrunt","Wynaut"}
}