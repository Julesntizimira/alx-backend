#!/usr/bin/env python3
'''  FIFO caching
'''


BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    ''' inherits from BaseCaching
        and is a caching system
    '''
    def __init__(self):
        ''' init method
            the constructor
        '''
        super().__init__()
        self.queue = []

    def put(self, key, item):
        '''override method to put() in super
        assign item to key in dictionary
        '''
        if key and item:
            if key in self.queue:
                self.queue.remove(key)
            elif len(self.queue) >= super().MAX_ITEMS:
                rem_key = self.queue.pop(0)
                del (self.cache_data[rem_key])
                print(f"DISCARD: {rem_key}")
            self.queue.append(key)
            self.cache_data[key] = item
        else:
            return None

    def get(self, key):
        '''return the value in self.cache_data
        linked to key
        '''
        if not key:
            return None
        return self.cache_data.get(key)
