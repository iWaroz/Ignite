# List of Event Objects usable as a callback for a native discord.py event
class EventList:
    def __init__(self, events: list):
        self.events = events
        
    async def __call__(self, *args):
        for event in sorted(self.events, key=lambda obj: obj.priority, reverse=True):
            await event(*args)

# Base class used in <bot>/events containing default predicate and callback
class Event:
    """Base class for Ignite Events\n
    Should have two methods:\n
    ```py
    def predicate(self, <args>) -> bool
        ...
    ```
    returning whether or not the event should be called\n
    ```py
    async def callback(self, <args>) -> None
        ...
    ```
    determining what exactly to do if the event is called"""
    predicate = lambda *args: True
    async def callback(*args): pass
    priority = 1

    def executer(self):
        async def execute(*args):
            if self.predicate(*args):
                await self.callback(*args)
        return execute