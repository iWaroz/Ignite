import ignite as ig

from _shibe.config import roles, notable_members

import discord

class shut (ig.Event):
    def predicate(self, message):
        return (
            # Only allow iWaroz and qsyl to use the command
            message.author.id in [notable_members.iWaroz, notable_members.qsyl] and
            # Message is a reply to another message
            message.reference is not None and
            message.content in ["shut", "stfu", "shut up"]
        )
    
    async def callback(self, message: discord.Message):
        reply_id = message.reference.message_id
        reply = await message.channel.fetch_message(reply_id)
        await reply.author.add_roles(message.guild.get_role(roles.MUTED))
        await message.reply('', embed=ig.embed.Message(
            msg=f"<gangsta> {message.author.mention} has been stfu'd"
        ))
        return exit