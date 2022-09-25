import importlib

def modulize(name: str, client):
    botmod = importlib.import_module(name)

    botmod.client = client