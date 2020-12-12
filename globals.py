

class GlobalsManager:

    MANAGER_INSTANCE = None

    @classmethod
    def get_manager(cls):
        if cls.MANAGER_INSTANCE is None:
            cls.MANAGER_INSTANCE = GlobalsManager()
        return cls.MANAGER_INSTANCE

    def __init__(self):
        self.global_dict = dict()
        self.global_dict.update({"target_row": 0})

    def get_global(self, key):
        value = self.global_dict.get(key)
        if value is None:
            print("Key doesnt exist")
            return None
        return value

    def update_global(self, key, value):
        self.global_dict[key] = value


def get_global(key):
    return GlobalsManager.get_manager().get_global(key)


def update_global(key, value):
    return GlobalsManager.get_manager().update_global(key, value)
