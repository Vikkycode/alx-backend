#!/usr/bin/env python3
"""
LIFOCache moduole
"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache class
    """

    def __init__(self):
        """
        Initialize the class with the parent's init method
        """
        super().__init__()
        self.last_key = None

    def put(self, key, item):
        """
        Add an item to the cache
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if key not in self.cache_data:
                    print("DISCARD: {}".format(self.last_key))
                    del self.cache_data[self.last_key]
            self.cache_data[key] = item
            self.last_key = key

    def get(self, key):
        """
        Get an item from the cache
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
