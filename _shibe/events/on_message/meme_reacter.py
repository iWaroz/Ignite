import ignite as ig
import _shibe.config as config

class meme_reacter (ig.Event):
    def predicate(self, message):
        return message.channel.name == "memes"
    
    async def callback(self, message):
        await message.add_reaction(config.emojis.upvote)
        await message.add_reaction(config.emojis.downvote)

