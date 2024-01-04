#!/usr/bin/env python3
''' Defines a class - LRUCache '''
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    '''
    Implements the LRU (Least Recently Used) cache
    algorithm
    '''
    def __init__(self):
        ''' Initializes LRUCache instances '''
        super().__init__()
        self.cache_data = OrderedDict(self.cache_data)

    def put(self, key, item):
        '''
        Updates the cache_data dictionary (inherited from BaseCaching)
        following the LRU caching algorithm
        '''
        if key is not None and item is not None:
            if key in self.cache_data.keys():
                self.cache_data.move_to_end(key)
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    lru_item = self.cache_data.popitem(last=False)
                    print('DISCARD: ' + lru_item[0])
            self.cache_data[key] = item

    def get(self, key):
        ''' Retrieves the value/cache item from the cache_data dictionary
            using a given key
        '''
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key)
            return self.cache_data.get(key)
        return None
