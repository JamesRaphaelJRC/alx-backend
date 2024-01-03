#!/usr/bin/env python3
''' Defines a class - LIFOCache '''
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    ''' Implements the LIFO caching system '''
    def put(self, key, item):
        '''
        Updates the cache_data dictionary (inherited from BaseCaching)
        following the LIFO caching algorithm
        '''
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                last_key = list(self.cache_data.keys())[-1]
                print('DISCARD: ', last_key)
                del self.cache_data[last_key]
            self.cache_data[key] = item

    def get(self, key):
        ''' Retrieves the value/cache item from the cache_data dictionary
            using a given key
        '''
        if key is not None and key in self.cache_data:
            return self.cache_data.get(key)
        return None
