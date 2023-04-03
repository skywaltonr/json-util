class JsonUtil:
    def __init__(self) -> None:
        pass

    def find_key(self, data, key_to_check):
        if isinstance(data, list):
            for item in data:
                yield from self.find_key(item, key_to_check)
        if isinstance(data, dict):
            for key in data.keys():
                if str(key) == key_to_check:
                    yield data[key]
                yield from self.find_key(data[key], key_to_check)


    def contains_key(self, data, key):
        return any(True for _ in self.find_key(data, key))

    def get_first_value(self, data, key):
        return next(self.find_key(data, key), None)
