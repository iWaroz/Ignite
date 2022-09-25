import random

import ignite as ig
import _shibe.config as config

class give_exp (ig.Event):
    def predicate(self, message):
        return (
            message.channel.id in config.channels.XP_RATES
        )

    async def callback(self, message):
        with message.author.ignite() as user:
            reward = random.randint(*config.channels.XP_RATES(message.channel.id))
            boost = user.xp_boost().rate
            user.exp += int(reward * boost)
            print(f"Gave {message.author} {reward} XP and who now has {user.exp}.")

            user = user.objectify()
        
        top_xp_role = max(
            (
                (k, config.limits.xp_roles[k])
                for k in config.limits.xp_roles
                if config.limits.xp_roles[k] <= user.exp
            ),
            key=lambda item: item[1]
        )[0]

        top_role_obj = message.guild.get_role(top_xp_role)

        if not message.author.has_role(top_xp_role):
            await message.author.remove_roles(*(
                message.guild.get_role(i)
                for i in config.limits.xproles
                if message.author.has_role(i)
            ))

            await message.author.add_roles(top_role_obj)
            level = int(top_role_obj.name
                    .split("(")[1]
                    .split(")")[0]
                    .replace('T', ''))
            
            await message.reply('', embed=ig.embed.LevelUP(
                level=level,
                member=message.author,
                role=top_role_obj
            ))