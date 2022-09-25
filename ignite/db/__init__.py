import ignite

# used for declaring database fields in <bot>/database/injections.py
class field:
    ignite_database_dependancy = True

    def __init__(self, val):
        self.val = val

# used as a decorator class for functions needing database fields in <bot>/database/injections.py
class dependant:
    ignite_database_dependancy = True
    
    def __init__(self, fn):
        self.fn = fn

class IgniteProxyObject:
    def __init__(self, obj):
        self.obj = obj
        if obj.__class__.__name__ != "Member":
            self.key = f"{obj.__class__.__name__}.{obj.id}"
        else:
            self.key = f"Member[{obj.guild.id}].{obj.id}"
        
        self.entered = False

    def objectify(self):
        data = ignite.database_interface.getter(self.key) or {}
        for field_name, value in self.obj._ignite_database_dependancies.items():
            if isinstance(value, field):
                if not field_name in data:
                    data[field_name] = value.val
            if isinstance(value, dependant):
                fn = value.fn
                data[field_name] = lambda *args: fn(self, *args)
        
        return ignite.utils.DictProxy(data)

    def __enter__(self):
        data = ignite.database_interface.getter(self.key) or {}
        for field_name, value in self.obj._ignite_database_dependancies.items():
            if isinstance(value, field):
                if not field_name in data:
                    data[field_name] = value.val
            if isinstance(value, dependant):
                fn = value.fn
                data[field_name] = lambda *args: fn(self, *args)
        
        self.entered = True
        self.data = data

        return self
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.entered = False

        ignite.database_interface.setter(
            self.key, 
            { k:v for k,v in self.data.items() if not callable(v) }
        )

        del self.data
    
    def __getattr__(self, attr: str):
        if attr in ["obj", "key", "data", "entered"]:
            return object.__getattribute__(self, attr)
        
        if self.entered and attr in self.data:
            return self.data[attr]

        return getattr(self.obj, attr)
    
    def __setattr__(self, attr: str, value):
        if attr in ["obj", "key", "data", "entered"]:
            super().__setattr__(attr, value)
        
        elif self.entered and attr in self.data:
            self.data[attr] = value

        else:
            setattr(self.obj, attr, value)

# self will represent any kind of discord object so this will let the IgniteProxyObject access it
def new_ignite_proxy(self) -> IgniteProxyObject:
    return IgniteProxyObject(self)