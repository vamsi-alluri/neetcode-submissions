from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.lru_cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.lru_cache:
            return self.lru_cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.lru_cache:
            self.lru_cache.move_to_end(key)
            self.lru_cache[key] = value
        else:
            if len(self.lru_cache) == self.capacity:
                self.lru_cache.popitem(last=False)
            self.lru_cache[key] = value
        
