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
            # Checks if key currently exists and deletes it with its value
            # to maintain LIFO order (so as to be readded with current value)


            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if key in self.cache_data.keys():
                    del self.cache_data[key]
                else:
                    last_key = list(self.cache_data.keys())[-1]
                    print('DISCARD: ', last_key)
                    del self.cache_data[last_key]

            # Updates the cache_data with the current key and item
            self.cache_data[key] = item

    def get(self, key):
        ''' Retrieves the value/cache item from the cache_data dictionary
            using a given key
        '''
        if key is not None and key in self.cache_data:
            return self.cache_data.get(key)
        return None
