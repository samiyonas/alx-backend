#!/usr/bin/env python3
""" implement simple pagination """
import csv
import math
from typing import List
import math
index_range = __import__('0-simple_helper_function').index_range


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
        """ get page of specified size """
        thePage = []
        page_info = [page, page_size]
        assert all(isinstance(i, int) and i > 0 for i in page_info)
        rang = list(index_range(page, page_size))
        dataset = self.dataset()

        if rang[0] >= len(dataset):
            return thePage
        if rang[1] >= len(dataset):
            rang[1] = len(dataset)

        for i in range(rang[0], rang[1]):
            thePage.append(dataset[i])

        return thePage

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ hypermedia pagination """
        data = self.get_page(page, page_size)
        theDataset = self.dataset()
        total_pages = math.ceil(len(theDataset) / page_size)
        next_page = page + 1
        prev_page = page - 1

        if next_page >= total_pages:
            next_page = None
        if prev_page < 1:
            prev_page = None

        pageDict = {
                "page_size": page_size,
                "page": page,
                "data": data,
                "next_page": next_page,
                "prev_page": prev_page,
                "total_pages": total_pages
                }
        return pageDict
