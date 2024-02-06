#!/usr/bin/python3
'''
This is  defines a an eviction cache method LFU
'''
from base_caching import BaseCaching
from collections import OrderedDict


class LFUCache(BaseCaching):
    '''defines a cache replacement policy of LFU'''
    def __init__(self):
        '''defines a constructor function to intialse args'''
        super().__init__()
        self.ordered_cache = OrderedDict(self.cache_data)
        self.frequency = OrderedDict()

    def put(self, key, item):
        '''
        assign to the dictionary self.cache_data the item value for the key

        Parameter
        key : key to be used in the in the dictionary to store the value
        item: the value to be stored with the key in the cache
        '''
        if key and item:
            # find the the least frequent before you add the new item
            if len(self.ordered_cache) == BaseCaching.MAX_ITEMS:
                lfu_value = min(self.frequency.values())
                lfu_keys = [key for key in self.frequency.keys()
                            if self.frequency[key] == lfu_value]

            self.ordered_cache[key] = item
            self.ordered_cache.move_to_end(key, False)
            self.frequency[key] = self.frequency.get(key, 0) + 1
            self.frequency.move_to_end(key, False)

            # check if the capacity has been breached
            if len(self.ordered_cache) > BaseCaching.MAX_ITEMS:
                if len(lfu_keys) == 1:
                    lfu_key = lfu_keys[0]
                    self.ordered_cache.pop(lfu_key)

                else:
                    # if more the than one item use the LRU policy
                    # since the keys are ordered the last one will be LRU
                    lfu_key = lfu_keys[-1]
                    self.ordered_cache.pop(lfu_keys[-1])

                self.frequency.pop(lfu_key)
                print('DISCARD: {}'.format(lfu_key))

            self.cache_data = dict(self.ordered_cache)

    def get(self, key):
        '''gets the value associated with the key from the cache

        Parameter
        key: the the ckey to be seeached in the cache dictionary

        Return
        the value or None if key is None or the key is not in the cache
        '''
        if key:
            value = self.cache_data.get(key)
            if value:
                # move the value to left to show that it was recently accessed
                self.ordered_cache.move_to_end(key, False)
                self.frequency[key] = self.frequency.get(key, 0) + 1
                self.frequency.move_to_end(key, False)
                self.cache_data = dict(self.ordered_cache)
            return value
        return None
