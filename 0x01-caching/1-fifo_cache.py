#!/usr/bin/env python3
''' Defines a class - FIFOCache '''
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    ''' Implements a FIFO caching system '''
    def put(self, key, item):
        '''
        Updates the cache_data dictionary (inherited from BaseCaching)
        with new cache data
        '''
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Creates an iterator using the keys in cache_data and uses
                # next to retrieve the next item (the first/oldest item)
                first_item_key = next(iter(self.cache_data))
                del self.cache_data[first_item_key]
                print("DISCARD: " + first_item_key)
            self.cache_data.update({key: item})

    def get(self, key):
        ''' Retrieves the value/cache item from the cache_data dictionary
            using a given key
        '''
        if key is not None and key in self.cache_data:
            return self.cache_data.get(key)
        return None
