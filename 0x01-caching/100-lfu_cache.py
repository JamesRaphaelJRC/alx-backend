#!/usr/bin/env python3
''' Defines a class - LFUCache '''
from collections import OrderedDict
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    ''' Implements the LFU cache algorithm '''
    def __init__(self):
        ''' Initializes LRUCache instances '''
        super().__init__()
        self.cache_data = OrderedDict(self.cache_data)
        self.usage_counter = {}  # Dictionary to store usage frequency

    def put(self, key, item):
        if key is not None and item is not None:
            if key in self.cache_data.keys():
                self.cache_data.move_to_end(key)
                self.usage_counter[key] += 1  # Increment usage frequency
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    lfu_item = min(
                        self.usage_counter, key=self.usage_counter.get)
                    self.cache_data.pop(lfu_item)
                    print('DISCARD:', lfu_item)
                    del self.usage_counter[lfu_item]

                self.cache_data[key] = item
                self.usage_counter[key] = 1  # Set initial usage frequency

    def get(self, key):
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key)
            self.usage_counter[key] += 1  # Increment usage frequency
            return self.cache_data.get(key)
        return None
