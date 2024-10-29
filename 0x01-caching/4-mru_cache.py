#!/usr/bin/env python3
"""
Implements a caching system with Most
Recently Used (MRU) Algorithm
"""
from base_caching import BaseCaching

from collections import OrderedDict


class MRUCache(BaseCaching):
    """ Represents an object that allows for a caching
    system in a dictionary with Most Recently Used (MRU)
    Algorithm when the limit is reached
    """
    def __init__(self):
        """ Initiliaze
        """
        super().__init__()  # Call the parent's __init__
        self.cache_data = OrderedDict()  # To track the LRU order

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                """ Discard the lru_key recently used item """
                mru_key, _ = self.cache_data.popitem(False)
                print("DISCARD:", mru_key)
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        else:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item from the cache by key
        """
        if key is None or key not in self.cache_data:
            return None
        self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)
