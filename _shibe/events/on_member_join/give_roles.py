import _shibe
from _shibe.config import roles, channels

import ignite as ig

ping_roles = (
    roles.PING_ANNOUNCE,
    roles.PING_POLL,
    roles.PING_EVENT,
    roles.PING_GIVE,
    roles.PING_MISC,
    roles.PING_UPDATE,
    roles.UNVERIFIED
)

async def give_roles(member):
    user = member.ignite().objectify()

    server_stats = member.guild.stats()
    embed_info = {
        "member": member,
        "verified": server_stats.verified,
        "unverified": server_stats.unverified
    }

    if user.uuid is None:
        role_to_give = roles.UNVERIFIED

        await member.guild.get_channel(channels.welcome) \
            .send("", embed=ig.embed.UnverifiedMembershipStatusChange(
                change="joined",
                user=user,
                **embed_info
            ))

    else:
        role_to_give = roles.MEMBER
        
        await member.guild.get_channel(channels.welcome) \
            .send("", embed=ig.embed.VerifiedMembershipStatusChange(
                change="came back",
                **embed_info
            ))

    await member.add_roles(*(
        _shibe.guild.get_role(role_id) for role_id in (
            *ping_roles,
            role_to_give
    )))