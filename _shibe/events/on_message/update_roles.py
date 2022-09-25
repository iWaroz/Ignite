import discord
import time

import ignite as ig
import _shibe.config as config

class update_roles (ig.Event):
    def predicate(self, message):
        # Only allow verified users and if the function hasn't been called for 3 days
        with message.author.ignite() as user:
            return (
                user.uuid is not None and
                (time.time() - user.lastupdated) > 86400 * 3
            )

    async def callback(self, message):
        # load database info and verify username stored is correct
        with message.author.ignite() as user:
            user.lastupdated = int(time.time())

            user_uuid = user.uuid
            user_donations = user.donations
            user_ign = user.username

            pdb_res = config.req.playerdb.get(user_uuid)
            correct_ign = pdb_res.find("data/player/username")

            if correct_ign != user_ign:
                user.username = correct_ign
        
        # change user nickname if mc username changed
        if correct_ign != message.author.nick:
            try:
                await message.author.edit(nick=correct_ign)
            except discord.Forbidden:
                pass

        user_guild_id = config.req.hypixel.get("guild", player=user_uuid).find("guild/_id")

        # add/remove @Shiba Cultist role if eligible or not
        if user_guild_id == config.cult_of_shiba.guild_id:
            if message.author.has_role(config.roles.GUILD_MATE):
                await message.author.add_roles(message.guild.get_role(config.roles.GUILD_MATE))
            else:
                await message.author.remove_roles(message.guild.get_role(config.roles.GUILD_MATE))
        
        # figure out the top donation role x or y player should have
        top_donation_role = max(
            (
                (k, config.limits.donations[k])
                for k in config.limits.donations
                if config.limits.donations[k] <= user_donations
            ),
            key=lambda item: item[1]
        )[0]

        # if deserving of a donation role and not having their top role
        if not (top_donation_role is None or message.author.has_role(top_donation_role)):
            # remove all donation roles
            await message.author.remove_roles(*(
                message.guild.get_role(role_id)
                for role_id in config.limits.donations
                if message.author.has_role(role_id)
            ))
            # then add the correct one (this is efficient since previous step wouldn't have removed the top role anyways)
            await message.author.add_roles(message.guild.get_role(top_donation_role))