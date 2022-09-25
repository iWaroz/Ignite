import ignite as ig

class test (ig.Event):
    def predicate(self, interaction):
        return True

    async def callback(self, interaction):
        print(interaction, dir(interaction))
        print(interaction.command, interaction.client, interaction.data, interaction.user)

        await interaction.client.get_guild(interaction.guild_id).get_channel(interaction.channel_id).send("yo")
