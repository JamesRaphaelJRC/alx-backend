#!/usr/bin/env python3
import csv
import math
from typing import List, Tuple


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    @staticmethod
    def index_range(self, page: int, page_size: int) -> Tuple[int, int]:
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

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        start_index, end_index = self.index_range(page, page_size)
        return self.dataset()[start_index:end_index]
