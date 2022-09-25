from deta import Deta
import _shibe

deta = Deta(_shibe.secrets["deta_key"])

def get_table(key: str):
    table, key = key.split('.')
    if table == "Member[677155964188753921]": 
        table = "members"
    else:
        table = table.lower()
    return deta.Base(table), key

class database:
    def getter(key: str):
        table, key = get_table(key)
        return table.get(key)

    def setter(key: str, value: dict):
        table, key = get_table(key)
        table.put(value, key)

    def deleter(key: str):
        table, key = get_table(key)
        table.delete(key)

_db = {}

class database_gay:
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