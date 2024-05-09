#!/usr/bin/python3
"""
1-fifo_cache module has a class FIFOCache
which inherits from BaseCaching and is a caching system
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    You must use self.cache_data - dictionary from the parent class BaseCaching
    You can overload def __init__(self):
    but don’t forget to call the parent init: super().__init__()
    """
    def __init__(self):
        """initialize"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Must assign to the dictionary self.cache_data
        the item value for the key key.
        If key or item is None, nothing should be done.
        If the number of items in self.cache_data is higher than
        BaseCaching.MAX_ITEMS:
        you must discard the first item put in cache
        (FIFO algorithm)
        you must print DISCARD: with the key discarded
        and following by a new line
        """
        if key is not None and item is not None:
            existing_keys = self.cache_data.keys()
            size = len(existing_keys)
            if size == self.MAX_ITEMS and key not in existing_keys:
                firstKey = self.order[0]
                self.cache_data.pop(firstKey)
                self.order.remove(firstKey)
                print("DISCARD: {}".format(firstKey))
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """
        Must return the value in self.cache_data linked to key.
        If key is None or if the key doesn’t exist in self.cache_data,
        return None.
        """
        if key is None:
            return None
        return self.cache_data.get(key)
