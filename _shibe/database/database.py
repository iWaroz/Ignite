import _shibe

_db = {}

class database:
    def getter(key: str):
        val = _db.get(key)
        print("\033[92mGet\033[0m", key, "\033[95m=>\033[0m", val)
        return val

    def setter(key: str, value: str):
        print("\033[93mSet\033[0m", key, "\033[95m=>\033[0m", value)
        _db[key] = value
    
    def deleter(key: str):
        print("\033[91mDel\033[0m", key)
        del _db[key]