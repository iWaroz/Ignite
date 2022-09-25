import discord
import ignite.client.initializer

from ignite.events import EventList
from ignite.misc.consts import overridable_events

import ignite

# Subclass of discord client used by the developer
class Client(discord.Client):
    def __init__(self, *args, **kwargs):
        self.event_callbacks = {}
        super().__init__(*args, **kwargs)

    # Run by developer to prepare the bot from the <bot> folder
    def init(self, folder):
        ignite.client.initializer.init_folder(self, folder)

    # Custom management of object attribute getting to generate event callbacks
    def __getattr__(self, attr: str):
        if attr in overridable_events:
            return EventList(self.event_callbacks.get(attr, []))
        return getattr(super(), attr)