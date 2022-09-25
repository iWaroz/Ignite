import discord

from ignite.misc.utils import DictProxy
import ignite as ig

# Utility class called by EmbedBuilder to make more readable embed generation code
# It uses the EmbedFactory annotations for info on what attributes an embed has
# When getting an attribute in there, either returns it if a literal or calls the function
class Resolver:
    def __init__(self, cls):
        self.cls = cls
    
    def __getattr__(self, attr: str):
        if not attr in EmbedFactory.__annotations__:
            return super().__getattr__(attr)

        val = getattr(self.cls, attr)
        if callable(val):
            val = val(self.options)
        
        if not isinstance(val, str):
            return val

        for var_name, var in ig.misc._inner.config.emojis.emojis.__dict__.items():
            #var = getattr(ig.misc._inner.config.emojis, var_name)
            if isinstance(var, str):
                val = val.replace(f"<{var_name}>", var)

        return val

# Called by ignite/client/initializer/factory_loader.py
# Used to convert an EmbedFactory subclass into a callable returning a discord Embed
class EmbedBuilder:
    def __init__(self, cls):
        self.cls = cls
        self.res = Resolver(cls)
    
    def __call__(self, **kwargs):
        self.res.options = DictProxy(kwargs)

        emb = discord.Embed(
            title=self.res.title or "",
            description=self.res.description or "",
            color=self.res.color or 0x000000
        )

        return emb

# Base class for embed builders in <bot>/factories/embeds.py
# Contains every default value for embed properties
class EmbedFactory:
    """Base Class for Embed Factories\n
    For each embed property, should have either a constant string or a function.\n
    In the case of a function, it should take one argument: `data`.
    It will contain an object with every keyword argument passed to the builder.\n
    This class will be converted into an EmbedBuilder by using the data of the class. Do not expect embed functions to be of type `EmbedFactory`."""
    title: str = ""
    description: str = ""
    color: int = 0x000000

# Is imported by the main module as ignite.embed
# Provides references to both the base embed class and the embed builder
class EmbedsExport:
    EmbedFactory = EmbedFactory
    EmbedBuilder = EmbedBuilder