#!/usr/bin/env python3
"""
MRUCache module
"""

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache class
    """

    def __init__(self):
        """
        Initialize the class with the parent's init method
        """
        super().__init__()
        self.most_recent_key = None

    def put(self, key, item):
        """
        Add an item to the cache
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if key not in self.cache_data:
                    print("DISCARD: {}".format(self.most_recent_key))
                    del self.cache_data[self.most_recent_key]
            self.cache_data[key] = item
            self.most_recent_key = key

    def get(self, key):
        """
        Get an item from the cache
        """
        if key is not None and key in self.cache_data:
            self.most_recent_key = key
            return self.cache_data[key]
        return None
