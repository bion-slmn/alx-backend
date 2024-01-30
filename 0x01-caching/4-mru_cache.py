#!/usr/bin/python3
'''
This is  defines a an eviction cache method MRU
'''
from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    '''defines a cache replacement policy of MRU'''
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
            if key in self.cache_data:
                self.cache_data.pop(key)
            self.cache_data[key] = item
            # check if the capacity has been breached
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                last_key = list(self.cache_data.keys())[-2]
                self.cache_data.pop(last_key)
                print('DISCARD: {}'.format(last_key))

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
                self.cache_data.pop(key)
                self.cache_data[key] = value
            return value
        return None
