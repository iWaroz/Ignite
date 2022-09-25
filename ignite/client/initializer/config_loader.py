import importlib

import ignite.misc._inner

def load(client, path: str):
    path = path.split('.')[0].replace('/', '.')
    module = importlib.import_module(path)
    for elem_name in dir(module):
        if elem_name.startswith("_"): continue
        elem = getattr(module, elem_name)
        #print("load", elem_name, elem)
        if hasattr(ignite.misc._inner.config, elem_name):
            attr = getattr(ignite.misc._inner.config, elem_name)
            #print("has", attr)
            setattr(attr, elem_name, elem)
            #for sub_elem in dir(attr):
            #    setattr(attr, sub_elem, getattr(getattr(module, elem), sub_elem))