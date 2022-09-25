import ignite as ig
import _shibe

class BobEmbed (ig.embed.EmbedFactory):
    color = lambda data: _shibe.bot.color

class Message (BobEmbed):
    def description(data):
        return data.msg

class Chonk (BobEmbed):
    title = lambda data: f"{data.emoji} {ig.utils.escape(data.username)} {'♲' * data.is_ironman}"
    description = lambda data: f"Total Chonk: **{data.total_chonk}**"

class UnverifiedMembershipStatusChange (ig.embed.EmbedFactory):
    color = 0x28cd84
    description = lambda data: f"""{'<stonks>' if data.change == 'joined' else '<notstonks>'} {data.member} {data.change} (new).
    <dot> Mention: {data.member.mention}
    *There are now {data.verified} verified and {data.unverified} unverified members.*"""

class VerifiedMembershipStatusChange (ig.embed.EmbedFactory):
    color = 0xe86059
    title = lambda data: f"{'<stonks>' if data.change == 'came back' else '<notstonks>'} {data.member} came back (verified)."
    description = lambda data: f"""<dot> Mention: {data.member.mention}
    <dot> UUID: {data.user.uuid}
    <dot> Username: {data.user.username}
    <dot> XP: {data.user.xp:,}
    <dot> Donated: {data.user.donations:,}
    *There are now {data.verified} verified and {data.unverified} unverified members.*"""

class LevelUp (BobEmbed):
    description = lambda data: f"""**LEVEL UP!** Chatting {data.level-1}** ➜ **{data.level}
    {data.member.mention}, you are now a {data.role.mention}!"""