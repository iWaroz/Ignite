class ConfigObject:
    def __setattr__(self, key, value):
        #print("set", key, "=>", value)
        super().__setattr__(key, value)

config = ConfigObject()
config.emojis = ConfigObject()