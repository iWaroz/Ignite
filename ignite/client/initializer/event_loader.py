import os
import importlib

from ignite.misc.consts import overridable_events
import ignite as ig

# Called by ignite/client/initializer/__init__.py
def load(client, path: str):
    event_types = os.listdir(path)

    for event_type in event_types:
        if event_type == "slash":
            slash_loader(client, path)

        if event_type in overridable_events:
            event_loader(client, path, event_type)

# Loads a folder with the name of an event
def event_loader(client, path: str, event_type: str):
    event_files = os.listdir(f"{path}/{event_type}")

    for event_file in event_files:
        if not event_file.endswith('.py'): continue
        mod_path: str = f"{path.replace('/', '.')}.{event_type}.{event_file[:-3]}"
        module = importlib.import_module(mod_path)
        event_obj = getattr(module, event_file[:-3])
        priority = 1
        if isinstance(event_obj, type):
            if issubclass(event_obj, ig.Event):
                priority = event_obj.priority
                event_obj = event_obj().executer()
        event_obj.priority = priority
        client.event_callbacks[event_type] = client.event_callbacks.get(event_type, []) + [event_obj]

def slash_loader(client, path: str):
    assert "TO DO"