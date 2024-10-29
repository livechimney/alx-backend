#!/usr/bin/env python3
""" Implements a caching system with LIFO
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LIFOCache(BaseCaching):
    """ Implements a caching system with LIFO
    """
    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            """ Discard the last item (LIFO algorithm) """
            last, _ = self.cache_data.popitem(True)
            print("DISCARD: {}".format(last))
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """ Get an item from the cache by key
        """
        return self.cache_data.get(key, None)
