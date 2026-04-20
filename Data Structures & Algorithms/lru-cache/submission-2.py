
class LRUCache:

    def __init__(self, capacity: int):
        self.lru_cache = list()
        self.capacity = capacity

    def find(self, key: int):

        for idx, (k, v) in enumerate(self.lru_cache):
            if k == key:
                return idx, (k, v)
        return (None, None)

    def evict_if_full(self) -> None:
        if len(self.lru_cache) == self.capacity:
            self.lru_cache.pop(0)
        

    def refresh(self, idx) -> None:
        element = self.lru_cache.pop(idx)
        self.lru_cache.append(element)


    def get(self, key: int) -> int:
        idx, element = self.find(key)
    
        if idx == None:
            return -1

        self.refresh(idx)
        return element[1]

    def put(self, key: int, value: int) -> None:
        idx, _ = self.find(key)

        if idx == None:
            self.evict_if_full()
            self.lru_cache.append((key, value))
        else:
            self.lru_cache.pop(idx)
            self.lru_cache.append((key, value))
