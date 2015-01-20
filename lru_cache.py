class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = 1 if capacity <= 0 else capacity;
        self.ordered_keys = []
        self.cache = {}

    # @return an integer
    def get(self, key):
        if self.cache.has_key(key):
            self.ordered_keys.remove(key)
            self.ordered_keys.insert(0, key)
            return self.cache[key]
        return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if self.cache.has_key(key):
            self.cache[key] = value
            self.ordered_keys.remove(key)
            self.ordered_keys.insert(0, key)
        else:
            if len(self.cache) == self.capacity :
                last_key = self.ordered_keys.pop()
                del self.cache[last_key]
            self.cache[key] = value
            self.ordered_keys.insert(0, key)

if __name__ == '__main__':
    lru_cache = LRUCache(2)
    print(lru_cache.get(2))
    lru_cache.set(2, 6)
    print(lru_cache.get(1))

    lru_cache.set(1, 5)
    lru_cache.set(1, 2)
    print(lru_cache.get(1))
    print(lru_cache.get(2))

