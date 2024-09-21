#!/usr/bin/env python3
""" MRU Caching """
BaseCaching = __import__("base_caching").BaseCaching


class MRUCache(BaseCaching):
    """ inherits from BaseCaching and is a caching system """
    manage_mru = []

    def put(self, key, item):
        """ assign to self.cache_data the item for the key key """
        if key and item:
            if key in self.manage_mru:
                self.manage_mru.remove(key)
                self.manage_mru.append(key)
            else:
                self.manage_mru.append(key)
            self.cache_data.update({key: item})

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                discarded = self.manage_mru[-2]

                del self.cache_data[discarded]
                self.manage_mru.remove(discarded)
                print("DISCARD: {}".format(discarded))

    def get(self, key):
        """ returns the value in self.cache_data linked to key """
        if key:
            try:
                gotten = self.cache_data[key]
                self.manage_mru.remove(key)
                self.manage_mru.append(key)
                return gotten
            except Exception:
                return None
        return None
