#!/usr/bin/python3
'''
This is  defines a an eviction cache method FIFO
'''
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    '''defines a cache replacement policy of FIF0'''
    def __init__(self):
        '''defines a constructor function to intialse args'''
        super().__init__()

    def put(self, key, item):
        '''
        assign to the dictionary self.cache_data the item value for the key

        Parameter
        key : key to be used in the in the dictionary to store the value
        item: the value to be stored with the key in the cache
        '''
        if key and item:
            self.cache_data[key] = item
            # check if the capacity has been breached
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                first_key = next(iter(self.cache_data))
                self.cache_data.pop(first_key)
                print('DISCARD: {}'.format(first_key))

    def get(self, key):
        '''gets the value associated with the key from the cache

        Parameter
        key: the the ckey to be seeached in the cache dictionary

        Return
        the value or None if key is None or the key is not in the cache
        '''
        if key:
            return self.cache_data.get(key)
        return None
