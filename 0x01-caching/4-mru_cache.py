#!/usr/bin/env python3
''' Defines a class - MRUCache '''
from collections import OrderedDict
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    ''' Implements MRU (Most Recently Used) Caching style '''
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict(self.cache_data)

    def put(self, key, item):
        '''
        Updates the cache_data dictionary (inherited from BaseCaching)
        following the MRU caching algorithm
        '''
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data.move_to_end(key)
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    mru_item = self.cache_data.popitem()
                    print('DISCARD: ' + mru_item[0])
            self.cache_data[key] = item

    def get(self, key):
        ''' Retrieves the value/cache item from the cache_data dictionary
            using a given key
        '''
        value = self.cache_data.get(key, None)
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
        return value
