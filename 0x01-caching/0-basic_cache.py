#!/usr/bin/python3
'''
This module define a class BasicCache that inherits from the BaseCaching
'''
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    '''class to implement put  and get methods for adding to and getting
    from the cache'''
    def put(self, key, item):
        '''assingns a a key to an item and place them in the cache

        -Parametes
        key : the key to be used in the cache dictionary
        item: value of the key to be stored in the cache
        '''
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        '''check if the keyis in the dictionary cache and return it

        Parameters
        - key:  the key to be used to check for the value in the cache

        Return:
        the value or None if the value not there in the cache
        '''
        if key:
            value = self.cache_data.get(key)
            return value
        return None
