import ignite as ig

class ig_SlashCommand:
    description: str
    allow_default: int

    args: ig.Args

class ig_perm:
    CREATE_INSTANT_INVITE = INVITE = (1 << 0)
    KICK_MEMBERS = KICK = (1 << 1)
    BAN_MEMBERS = BAN = (1 << 2)
    ADMINISTRATOR = ADMIN = (1 << 3)
    MANAGE_CHANNELS = (1 << 4)
    MANAGE_GUILD = MANAGE_SERVER = (1 << 5)
    ADD_REACTIONS = REACT = (1 << 6)
    VIEW_AUDIT_LOG = (1 << 7)
    PRIORITY_SPEAKER = (1 << 8)
    STREAM = (1 << 9)
    VIEW_CHANNEL = (1 << 10)
    SEND_MESSAGES = (1 << 11)
    SEND_TTS_MESSAGES = (1 << 12)
    MANAGE_MESSAGES = (1 << 13)
    EMBED_LINKS = (1 << 14)
    ATTACH_FILES = (1 << 15)
    READ_MESSAGE_HISTORY = (1 << 16)
    MENTION_EVERYONE = (1 << 17)
    USE_EXTERNAL_EMOJIS = (1 << 18)
    VIEW_GUILD_INSIGHTS = (1 << 19)
    CONNECT = (1 << 20)
    SPEAK = (1 << 21)
    MUTE_MEMBERS = MUTE = (1 << 22)
    DEAFEN_MEMBERS = DEAFEN = (1 << 23)
    MOVE_MEMBERS = (1 << 24)
    USE_VAD = (1 << 25)
    CHANGE_NICKNAME = (1 << 26)
    MANAGE_NICKNAMES = (1 << 27)
    MANAGE_ROLES = (1 << 28)
    MANAGE_WEBHOOKS = (1 << 29)
    MANAGE_EMOJIS_AND_STICKERS = (1 << 30)
    USE_APPLICATION_COMMANDS = (1 << 31)
    REQUEST_TO_SPEAK = (1 << 32)
    MANAGE_EVENTS = (1 << 33)
    MANAGE_THREADS = (1 << 34)
    CREATE_PUBLIC_THREADS = (1 << 35)
    CREATE_PRIVATE_THREADS = (1 << 36)
    USE_EXTERNAL_STICKERS = (1 << 37)
    SEND_MESSAGES_IN_THREADS = (1 << 38)
    USE_EMBEDDED_ACTIVITIES = (1 << 39)
    MODERATE_MEMBERS = (1 << 40)

class ig_Args:
    ...

ig.SlashCommand = ig_SlashCommand
ig.perm = ig_perm

class forceverify (ig.SlashCommand):
    description = "Forcefully link a discord and minecraft account"
    perm = ig.perm.ADMIN | ig.perm.MANAGE_SERVER

    args = ig.Args(
        username = ig.arg.STR(
            desc = "Username of person you wish to see. Leave empty for the account you are verified as."
        ),
        account = ig.arg.MEMBER(
            desc = "Name of the profile you wish to calculate. Leave empty to get highest profile."
        )
    )

    async def callback(ctx, account, username):
        await ctx.reply("Done! (not)")

