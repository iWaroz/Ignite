# Converts a dictionary into an object for dot notation
class DictProxy:
    def __init__(self, data: dict):
        self.__dict__ = data

# Decorator to mark a function as being an ignite override
def override(fn):
    fn.ignite_override = True
    return fn