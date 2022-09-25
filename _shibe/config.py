class emojis:
    dab = "<:dab:911246736306081802>"
    gangsta = "<:gangsta:758740652145770536>"
    upvote = "<:upvote:699614509777551391>"
    downvote = "<:downvote:699614552148672593>"
    stonks = "<:stonks:690173866760470633>"
    dot = "<:dot:827907423381487657>"

class notable_members:
    iWaroz = 715902532110516304
    qsyl = 652878672180543488

class roles:
    OWNER = 718085313137999883
    MEMBER = 693153982788403301
    PING_GIVE = 754388393223389285
    PING_ANNOUNCE = 783566316333432873
    PING_EVENT = 783566308456923166
    PING_POLL = 783566310416187412
    PING_UPDATE = 783566312399831050
    PING_MISC = 678656349600743470
    UNVERIFIED = 691646709209497640
    GUILD_MATE = 678247498455973891
    NITRO_BOOSTER = 694895046599639080
    DONOR_2 = 839117944071651390
    DONOR_5 = 839117942486597672
    DONOR_10 = 839117940502036500
    DONOR_20 = 839117938392432671
    DONOR_50 = 839117936357933086
    DONOR_100 = 893787747775565854
    XP_13 = 899306825286045746
    XP_12 = 899306827219632159
    XP_11 = 899306829983653929
    XP_10 = 899306832634474506
    XP_9 = 839077349122637854
    XP_8 = 839077351153074246
    XP_7 = 839077352880865302
    XP_6 = 839077355351048225
    XP_5 = 839077359838691328
    XP_4 = 839077357414252595
    XP_3 = 839077361890361384
    XP_2 = 839077363878723624
    XP_1 = 839077366038921236
    MUTED = 704580596185300993

class channels:
    welcome = 757187214298841109
    general = 677200393498787853
    media = 677200484729094154
    bingo = 926775886387245067
    memes = 683409009885052971
    development = 690963280818077697

    XP_RATES = {
        general: (15, 25),
        media: (10, 15),
        bingo: (15, 20),
        memes: (10, 15),
        development: (1, 3)
    }

class req:
    import topaz
    import _shibe

    hypixel = topaz.Client(
        domain='api.hypixel.net/', 
        args={"key": _shibe.secrets["hypixel_key"]}, 
        cache=1200
    )

    playerdb = topaz.Client(
        domain='playerdb.co/api/player/minecraft/', 
        cache=6000
    )

class cult_of_shiba:
    guild_id = "5a4d0bae0cf23e5c94512ada"

class limits:
    donations = {
        None: 0,
        roles.DONOR_2: 2_000_000,
        roles.DONOR_5: 5_000_000,
        roles.DONOR_10: 10_000_000,
        roles.DONOR_20: 20_000_000,
        roles.DONOR_50: 50_000_000,
        roles.DONOR_100: 100_000_000
    }

    xp_roles = {
        None: 0,
        roles.XP_13: 500_000,
		roles.XP_12: 200_000,
		roles.XP_11: 150_000,
		roles.XP_10: 80_000,
		roles.XP_9: 50_000,
		roles.XP_8: 30_000,
		roles.XP_7: 10_000,
		roles.XP_6: 5_000,
		roles.XP_5: 2_500,
		roles.XP_4: 1_500,
		roles.XP_3: 800,
		roles.XP_2: 400,
		roles.XP_1: 200
    }