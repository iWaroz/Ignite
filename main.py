import ignite as ig
import os

import discord

bot = ig.Client(intents=discord.Intents.all())

import _shibe

import json
with open('secrets.json') as secrets:
    _shibe.secrets = json.loads(secrets.read()) # os.getenv("DISCORD_TOKEN")

token = _shibe.secrets["bot_token"]
bot.init(_shibe, token=token)
# print(bot)



bot.run()