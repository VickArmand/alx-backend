#!/usr/bin/python3
"""2-lifo_cache module has a class LIFOCache
that inherits from BaseCaching and is a caching system"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    You must use self.cache_data - dictionary
    from the parent class BaseCaching
    You can overload def __init__(self)
    but don’t forget to call the parent init: super().__init__()
    """
    def __init__(self):
        """initialize"""
        super().__init__()

    def get(self, key):
        """
        Must return the value in self.cache_data linked to key.
        If key is None or if the key doesn’t exist in self.cache_data,
        return None.
        """
        if key is None:
            return None
        return self.cache_data.get(key)

    def put(self, key, item):
        """
        Must assign to the dictionary self.cache_data the item value
        for the key key.
        If key or item is None, this method should not do anything.
        If the number of items in self.cache_data is higher than
        BaseCaching.MAX_ITEMS:
        you must discard the last item put in cache (LIFO algorithm)
        you must print DISCARD: with the key discarded and followed
        by a new line
        """
        if key is not None and item is not None:
            sorted_keys = list(reversed(self.cache_data.keys()))
            print(sorted_keys)
            size = len(sorted_keys)
            lastKey = sorted_keys[0]
            if size == self.MAX_ITEMS and key not in sorted_keys:
                self.cache_data.pop(lastKey)
                print("DISCARD: {}".format(lastKey))
        self.cache_data[key] = item
