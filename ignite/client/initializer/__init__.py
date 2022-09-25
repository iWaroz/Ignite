import os

import ignite.client.initializer.event_loader as event_loader
import ignite.client.initializer.factory_loader as factory_loader
import ignite.client.initializer.config_loader as config_loader
import ignite.client.initializer.database_loader as database_loader

import ignite.client.initializer.modulizer as modulizer

loaders = {
    "events": event_loader,
    "factories": factory_loader,
    "database": database_loader,
    "config.py": config_loader
}

# Utility to load a folder into the client
def init_folder(client, folder):
    # load every subfolder of the client
    botfolder = os.listdir(folder.__name__)

    for sub in botfolder:
        if sub in loaders:
            loaders[sub].load(client, f"{folder.__name__}/{sub}")
    
    # load module of name <bot>
    modulizer.modulize(folder.__name__, client)