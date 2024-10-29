#!/usr/bin/env python3
""" Implements a caching system with FIFO
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ Implements a caching system with FIFO
    """
    def __init__(self):
        """ Initiliaze
        """
        super().__init__()  # Call parent's __init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            """ Discard the first item (FIFO algorithm) """
            first = next(iter(self.cache_data))
            del self.cache_data[first]
            print("DISCARD: {}".format(first))
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item from the cache by key
        """
        return self.cache_data.get(key, None)
