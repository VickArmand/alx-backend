#!/usr/bin/python3
"""3-lru_cache module has a class LFUCache that
inherits from BaseCaching and is a caching system:"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    You must use self.cache_data - dictionary
    from the parent class BaseCaching
    You can overload def __init__(self):
    but don’t forget to call the parent init: super().__init__()
    """
    def __init__(self):
        """initialize"""
        super().__init__()
        self.frequencyUsed = {}
        self.recentlyUsed = []

    def put(self, key, item):
        """
        Must assign to the dictionary self.cache_data
        the item value for the key key.
        If key or item is None, this method should not do anything.
        If the number of items in self.cache_data is higher than
        BaseCaching.MAX_ITEMS:
        you must discard the least recently used item (LFU algorithm)
        you must print DISCARD: with the key discarded and
        following by a new line
        """
        if key is not None and item is not None:
            existing_keys = self.cache_data.keys()
            size = len(existing_keys)
            if size == self.MAX_ITEMS and key not in existing_keys:
                minVal = min(self.frequencyUsed.values())
                frequentList = []
                for k in self.frequencyUsed.keys():
                    if self.frequencyUsed[k] == minVal:
                        frequentList.append(k)
                if len(frequentList) == 1:
                    self.cache_data.pop(frequentList[0])
                    self.frequencyUsed.pop(frequentList[0])
                    print(f"DISCARD: {frequentList[0]}")
                else:
                    for k in self.recentlyUsed:
                        if k in frequentList:
                            self.cache_data.pop(k)
                            self.frequencyUsed.pop(k)
                            print(f"DISCARD: {k}")
                            break
            self.cache_data[key] = item
            if key in self.recentlyUsed:
                self.recentlyUsed.remove(key)
            self.recentlyUsed.append(key)
            value = self.frequencyUsed.get(key)
            if value:
                self.frequencyUsed[key] = value + 1
            else:
                self.frequencyUsed[key] = 1
        print(self.frequencyUsed)

    def get(self, key):
        """
        Must return the value in self.cache_data linked to key.
        If key is None or if the key doesn’t exist in self.cache_data,
        return None.
        """
        if key is None:
            return None
        value = self.cache_data.get(key)
        frequency = self.frequencyUsed.get(key)
        if key in self.recentlyUsed:
            self.recentlyUsed.remove(key)
        if value:
            if frequency:
                self.frequencyUsed[key] = frequency + 1
            else:
                self.frequencyUsed[key] = 1
            self.recentlyUsed.append(key)
        print(self.frequencyUsed)
        return value
