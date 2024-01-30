#!/usr/bin/env python3
'''  Basic dictionary
'''


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    ''' inherits from BaseCaching
        and is a caching system
    '''
    def __init__(self):
        ''' init method
            the constructor
        '''
        super().__init__()

    def put(self, key, item):
        '''override method to put() in super
        assign item to key in dictionary
        '''
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        '''return the value in self.cache_data
        linked to key
        '''
        if not key:
            return None
        return self.cache_data.get(key)
