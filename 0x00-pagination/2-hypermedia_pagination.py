#!/usr/bin/env python3
'''Hypermedia pagination
'''
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    '''return a tuple of size two containing
       a start index and an end index
    '''
    start = (page - 1) * page_size
    end = (start + page_size)
    return (start, end)


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

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''apply indes_range to get start and end indices
            and return the correct page
        '''
        assert isinstance(page, int) and page > 0 and\
            isinstance(page_size, int) and page_size > 0
        indexes = index_range(page, page_size)
        dataset = self.dataset()
        if indexes[0] > indexes[1] or indexes[0] > len(dataset):
            return []
        elif indexes[1] > len(dataset):
            return []
        page = [self.__dataset[data] for data
                in range(indexes[0], indexes[1])]
        return page

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''get Hypermedia pagination
        '''
        dataset = self.dataset()
        page_data = self.get_page(page, page_size)
        next_page = page + 1 if page * page_size < len(dataset) else None
        result = {
            "page_size": len(page_data),
            "page": page,
            "data": page_data,
            "next_page": next_page,
            "prev_page": None if page <= 1 else page - 1,
            "total_pages": math.ceil(len(dataset) / page_size)
        }
        return result
