#!/usr/bin/env python3
""" LFU Caching """
BaseCaching = __import__("base_caching").BaseCaching


class LFUCache(BaseCaching):
    """ inherits from BaseCaching and is caching system """
    manage_lfu = []
    manage_lfu_dict = {}

    def put(self, key, item):
        """ assign to self.cache_data the item for key key """
        if key and item:
            if key in self.manage_lfu_dict:
                self.manage_lfu_dict[key] += 1
                self.manage_lfu.remove(key)
                self.manage_lfu.append(key)
            else:
                self.manage_lfu_dict[key] = 0
                self.manage_lfu.append(key)
            self.cache_data.update({key: item})

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                sorted_fl = sorted(
                        self.manage_lfu_dict.items(),
                        key=lambda x: x[1]
                        )
                if sorted_fl[0][1] != sorted_fl[1][1]:
                    del self.cache_data[sorted_fl[0][0]]
                    discarded = sorted_fl[0][0]

                    self.manage_lfu.remove(discarded)
                    del self.manage_lfu_dict[sorted_fl[0][0]]

                    print("DISCARD: {}".format(discarded))
                else:
                    x = []
                    x.append(sorted_fl[0][0])

                    for i in range(len(sorted_fl)):
                        if i == 0:
                            continue
                        if sorted_fl[0][1] == sorted_fl[i][1]:
                            x.append(sorted_fl[i][0])

                    for j in self.manage_lfu:
                        if j in x:
                            del self.cache_data[j]
                            self.manage_lfu.remove(j)
                            del self.manage_lfu_dict[j]
                            print("DISCARD: {}".format(j))
                            break

    def get(self, key):
        """ returns the value in self.cache_data linked to key"""
        if key:
            try:
                gotten = self.cache_data[key]
                self.manage_lfu_dict[key] += 1
                self.manage_lfu.remove(key)
                self.manage_lfu.append(key)
                return gotten
            except Exception:
                return None
        return None
