import importlib
import os

import discord

from ignite.db import new_ignite_proxy

import ignite
ignite.database_interface = None

def load(client, path: str):
    files = os.listdir(path)

    file_loaders = {
        "database.py": load_database_py,
        "injections.py": load_injections_py
    }

    for file_name in files:
        if file_name in file_loaders:
            file_loaders.get(file_name)(client, path)

def load_injections_py(client, path: str):
    mod = importlib.import_module(path.replace('/', '.') + '.injections')
    for obj_name in dir(mod):
        obj = getattr(mod, obj_name)
        if not isinstance(obj, type):
            continue

        if not hasattr(discord, obj_name):
            continue
        
        load_class(obj_name, obj)

def load_class(name: str, cls: type):
    dsc_attr = getattr(discord, name)

    to_inject = {}

    for attr_name in dir(cls):
        if attr_name.startswith('_') and not hasattr(getattr(cls, attr_name), "ignite_override"):
            continue
    
        to_inject[attr_name] = getattr(cls, attr_name)
    
    for annot, value in cls.__annotations__.items():
        to_inject[annot] = value
    
    dependancies = {}

    for obj_name, obj in to_inject.items():
        if hasattr(obj, "ignite_database_dependancy"):
            dependancies[obj_name] = obj

        else:
            setattr(dsc_attr, obj_name, obj)
    
    setattr(dsc_attr, "_ignite_database_dependancies", dependancies)
    setattr(dsc_attr, "ignite", new_ignite_proxy)

def load_database_py(client, path: str):
    mod = importlib.import_module(path.replace('/', '.') + ".database")

    ignite.database_interface = mod.database
