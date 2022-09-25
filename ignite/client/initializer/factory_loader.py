import os
import importlib

import ignite.embed

# Called by ignite/client/initializer/__init__.py
def load(client, path: str):
    factories = os.listdir(path)

    for factory in factories:
        if hasattr(FactoryLoaders, factory[:-3]):
            getattr(FactoryLoaders, factory[:-3])(client, path.replace('/', '.') + '.' + factory[:-3])

# Contains scripts for loading every type of factory
class FactoryLoaders:
    def embeds(client, path: str):
        module = importlib.import_module(path)
        for obj_name in dir(module):
            obj = getattr(module, obj_name)
            if not isinstance(obj, type):
                continue
            if not issubclass(obj, ignite.embed.EmbedFactory):
                continue
            setattr(ignite.embed, obj.__name__, ignite.embed.EmbedBuilder(obj))