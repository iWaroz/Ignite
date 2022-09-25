from _shibe.config import channels
import ignite as ig

async def logger(member):
    user = member.ignite().objectify()
    server_stats = member.guild.stats()

    embed_info = {
        "member": member,
        "verified": server_stats.verified,
        "unverified": server_stats.unverified
    }

    if user.uuid is None:
        await member.guild.get_channel(channels.welcome) \
            .send("", embed=ig.embed.UnverifiedMembershipStatusChange(
                change="joined",
                user=user,
                **embed_info))
    
    else:
        await member.guild.get_channel(channels.welcome) \
            .send("", embed=ig.embed.VerifiedMembershipStatusChange(
                change="came back",
                **embed_info))