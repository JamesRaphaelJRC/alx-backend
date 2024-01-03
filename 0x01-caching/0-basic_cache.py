#!/usr/bin/env python3
''' Defines a class - BasicCache '''
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    ''' The BasicCache class definition '''
    def put(self, key, item):
        '''
        Updates the cache_data dictionary (inherited from BaseCaching)
        with new cache data
        '''
        if key or item is not None:
            self.cache_data.update({key: item})

    def get(self, key):
        ''' Retrieves the value/cache item from the cache_data dictionary
            using a given key
        '''
        if key is not None and key in self.cache_data:
            return self.cache_data.get(key)
        return None
