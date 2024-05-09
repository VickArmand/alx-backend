#!/usr/bin/python3
"""3-lru_cache module has a class LRUCache that
inherits from BaseCaching and is a caching system:"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    You must use self.cache_data - dictionary
    from the parent class BaseCaching
    You can overload def __init__(self):
    but don’t forget to call the parent init: super().__init__()
    """
    def __init__(self):
        """initialize"""
        super().__init__()
        self.recentlyUsed = []

    def put(self, key, item):
        """
        Must assign to the dictionary self.cache_data
        the item value for the key key.
        If key or item is None, this method should not do anything.
        If the number of items in self.cache_data is higher than
        BaseCaching.MAX_ITEMS:
        you must discard the least recently used item (LRU algorithm)
        you must print DISCARD: with the key discarded and
        following by a new line
        """
        if key is not None and item is not None:
            existing_keys = self.cache_data.keys()
            size = len(existing_keys)
            if size == self.MAX_ITEMS and key not in existing_keys:
                leastRecentlyUsed = self.recentlyUsed[0]
                self.cache_data.pop(leastRecentlyUsed)
                self.recentlyUsed.remove(leastRecentlyUsed)
                print(f"DISCARD: {leastRecentlyUsed}")
            self.cache_data[key] = item
            if key in self.recentlyUsed:
                self.recentlyUsed.remove(key)
            self.recentlyUsed.append(key)

    def get(self, key):
        """
        Must return the value in self.cache_data linked to key.
        If key is None or if the key doesn’t exist in self.cache_data,
        return None.
        """
        if key is None:
            return None
        value = self.cache_data.get(key)
        if key in self.recentlyUsed:
            self.recentlyUsed.remove(key)
        if value:
            self.recentlyUsed.append(key)
        return value
