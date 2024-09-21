#!/usr/bin/env python3
""" FIFO caching """
BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """ inherits from BaseCaching and is a caching system """
    def put(self, key, item):
        """ assign to self.cache_data the item for the key key """
        if key and item:
            self.cache_data.update({key: item})

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                discarded = list(self.cache_data)[0]
                del self.cache_data[discarded]

                print("DISCARD: {}".format(discarded))

    def get(self, key):
        """ returns the value in self.cache_data linked to key """
        if key:
            try:
                return self.cache_data[key]
            except Exception:
                return None
        return None
