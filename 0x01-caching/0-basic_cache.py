#!/usr/bin/env python3
""" Basic dictionary """
BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """ inherits from BaseCaching and is a caching system """
    def put(self, key, item):
        """ assign to self.cache_data the item value for the key key """
        if key and item:
            self.cache_data.update({key: item})

    def get(self, key):
        """ must return the value in self.cache_data linked to key """
        if key:
            try:
                return self.cache_data[key]
            except Exception:
                return None
