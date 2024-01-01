#!/usr/bin/env python3
''' Defines an index_range function '''
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''
    Return a tuple of size 2 containing a start and end indexes
    corresponding to rangen of indexes to return.
    Args:
        page (int): the current page
        page_size (int): the amount of items in a page
    Returns:
        (tuple): a tuple of the start and end index for the given page
    '''
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return start_index, end_index
