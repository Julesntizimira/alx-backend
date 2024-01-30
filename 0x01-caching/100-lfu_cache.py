#!/usr/bin/env python3
'''  LFU caching
'''


BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    ''' inherits from BaseCaching
        and is a caching system
    '''
    def __init__(self):
        ''' init method
            the constructor
        '''
        super().__init__()
        self.frequency = {}
        self.recents = []

    def put(self, key, item):
        '''override method to put() in super
        assign item to key in dictionary
        '''
        if key and item:
            if key in self.frequency.keys():
                self.frequency[key] = self.frequency[key] + 1
                self.recents.remove(key)
            elif len(self.recents) >= super().MAX_ITEMS:
                my_list = list(self.frequency.keys())
                min = my_list[0]
                for k in self.frequency.keys():
                    if self.frequency[k] < self.frequency[min]:
                        min = k
                duplicate = []
                for k in self.frequency.keys():
                    if self.frequency[k] == self.frequency[min]:
                        duplicate.append(k)
                if len(duplicate) == 1:
                    rem_key = min
                elif len(duplicate) > 1:
                    for el in self.recents:
                        if el in duplicate:
                            rem_key = el
                            break
                self.recents.remove(rem_key)
                del (self.frequency[rem_key])
                del (self.cache_data[rem_key])
                print(f"DISCARD: {rem_key}")
                self.frequency[key] = 0
            else:
                self.frequency[key] = 0
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
        self.frequency[key] = self.frequency[key] + 1
        return self.cache_data.get(key)
