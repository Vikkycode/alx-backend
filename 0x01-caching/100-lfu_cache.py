#!/usr/bin/env python3
"""
LFUCache module
"""

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache class
    """

    def __init__(self):
        """
        Initialize the class with the parent's init method
        """
        super().__init__()
        self.key_frequency = {}
        self.key_timestamps = {}
        self.timestamp = 0

    def put(self, key, item):
        """
        Add an item to the cache
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if key not in self.cache_data:
                    self.discard_lfu()
            self.cache_data[key] = item
            self.key_frequency[key] = self.key_frequency.get(key, 0) + 1
            self.key_timestamps[key] = self.timestamp
            self.timestamp += 1

    def get(self, key):
        """
        Get an item from the cache
        """
        if key is not None and key in self.cache_data:
            self.key_frequency[key] += 1
            self.key_timestamps[key] = self.timestamp
            self.timestamp += 1
            return self.cache_data[key]
        return None

    def discard_lfu(self):
        """
        Discard the least frequently used item
        """
        min_frequency = min(self.key_frequency.values())
        lfu_keys = [
            key for key, frequency in self.key_frequency.items()
            if frequency == min_frequency
        ]
        if len(lfu_keys) == 1:
            discarded_key = lfu_keys[0]
        else:
            discarded_key = min(
                lfu_keys, key=lambda k: self.key_timestamps[k]
            )
        del self.cache_data[discarded_key]
        del self.key_frequency[discarded_key]
        del self.key_timestamps[discarded_key]
        print("DISCARD: {}".format(discarded_key))
