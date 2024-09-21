#!/usr/bin/env python3
""" LRU Caching """
BaseCaching = __import__("base_caching").BaseCaching


class LRUCache(BaseCaching):
    """ inherits from BaseCaching and is caching system """
    manage_lru = []

    def put(self, key, item):
        """ assign to self.cache_data the item for the key key """
        if key and item:
            if key in self.manage_lru:
                self.manage_lru.remove(key)
                self.manage_lru.append(key)
            else:
                self.manage_lru.append(key)
            self.cache_data.update({key: item})

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                discarded = self.manage_lru[0]

                del self.cache_data[discarded]
                self.manage_lru.remove(discarded)
                print("DISCARD: {}".format(discarded))

    def get(self, key):
        """ returns the value in self.cache_data linked to key """
        if key:
            try:
                gotten = self.cache_data[key]
                self.manage_lru.remove(key)
                self.manage_lru.append(key)
                return gotten
            except Exception:
                return None
        return None
