#!/usr/bin/env python3
'''  LRU caching
'''


BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    ''' inherits from BaseCaching
        and is a caching system
    '''
    def __init__(self):
        ''' init method
            the constructor
        '''
        super().__init__()
        self.recents = []

    def put(self, key, item):
        '''override method to put() in super
        assign item to key in dictionary
        '''
        if key and item:
            if key in self.recents:
                self.recents.remove(key)
            elif len(self.recents) >= super().MAX_ITEMS:
                rem_key = self.recents.pop(0)
                del (self.cache_data[rem_key])
                print(f"DISCARD: {rem_key}")
            self.recents.append(key)
            self.cache_data[key] = item
        else:
            return None

    def get(self, key):
        '''return the value in self.cache_data
        linked to key
        '''
        if not key or not self.cache_data.get(key):
            return None
        self.recents.remove(key)
        self.recents.append(key)
        return self.cache_data.get(key)
