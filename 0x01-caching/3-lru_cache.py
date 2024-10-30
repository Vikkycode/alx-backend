#!/usr/bin/env python3
"""
LRUCache module
"""

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache class
    """

    def __init__(self):
        """
        Initialize the class with the parent's init method
        """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """
        Add an item to the cache
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if key not in self.cache_data:
                    discarded_key = self.keys.pop(0)
                    del self.cache_data[discarded_key]
                    print("DISCARD: {}".format(discarded_key))
            if key in self.keys:
                self.keys.remove(key)
            self.keys.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Get an item from the cache
        """
        if key is not None and key in self.cache_data:
            if key in self.keys:
                self.keys.remove(key)
                self.keys.append(key)
            return self.cache_data[key]
        return None
