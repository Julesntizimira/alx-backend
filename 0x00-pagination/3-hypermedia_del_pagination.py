#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        '''return a dictionary with the key-value pairs
        '''
        dataset = self.indexed_dataset()
        if index is not None:
            assert index < len(dataset)
        else:
            index = 0
        page_data = []
        new_index = index
        while (not dataset.get(index) and new_index < len(dataset)):
            new_index = new_index + 1

        for i in range(new_index, new_index + page_size):
            if i < len(dataset):
                data = dataset.get(i)
                if data:
                    page_data.append(data)
                else:
                    page_size = page_size + 1
            else:
                break

        next_index = i + 1 if (i + 1) < len(dataset) else None
        result = {
            "index": new_index,
            "next_index": next_index,
            "page_size": len(page_data),
            "data": page_data
        }
        return result
