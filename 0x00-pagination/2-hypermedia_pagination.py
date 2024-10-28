#!/usr/bin/env python3
"""get page method"""


import csv
import math
from typing import List


def index_range(page, page_size):
    """
    Write a function named index_range
    that takes two integer arguments
    page and page_size.

    The function should return a tuple
    of size two containing a start index
    and an end index corresponding to the
    range of indexes to return in a list
    for those particular pagination parameters.
    """
    start = (page - 1) * page_size
    end = start + page_size
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
        """
        get page
        """
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        start, end = index_range(page, page_size)
        return self.dataset()[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        return dict
        """
        total_pages = math.ceil(len(self.dataset()) / page_size)
        return {
            'page_size': len(self.get_page(page, page_size)),
            'page': page,
            'data': self.get_page(page, page_size),
            'next_page': page + 1 if page + 1 <= total_pages else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': total_pages
        }
