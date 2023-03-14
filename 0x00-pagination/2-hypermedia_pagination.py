#!/usr/bin/env python3
"""
This module implements a simple pagigation on data
"""

import csv
from typing import List
index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Returns a data range based on the page and page size values
        """

        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = index_range(page, page_size)

        return self.dataset()[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10):
        """
        Returns HATEOAS data
        """

        data = self.get_page(page, page_size)
        total_pages = len(self.dataset()) // page_size

        prev_page = next_page = None

        if page - 1 > 0:
            prev_page = page - 1

        if page + page_size <= total_pages:
            next_page = page + page_size - 1

        return {"page_size": page_size, "page": page, "data": data,
                "next_page": next_page, "prev_page": prev_page,
                "total_pages": total_pages}
