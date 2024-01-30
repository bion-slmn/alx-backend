#!/usr/bin/env python3
''' defines a class server to paginate a database'''
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

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''
        gets the contents of a page

        Parameter
        -page (int): the page number where the content is located
        - page_size (int): the size of a page

        Return
        list of list of row in the page
        '''
        page_rows = []
        assert type(page) == int
        assert page > 0
        assert type(page_size) == int
        assert page_size > 0
        start_index, end_index = self.index_range(page, page_size)

        data = self.dataset()
        length = len(data)
        if start_index <= length and end_index <= length:
            for i in range(start_index, end_index):
                page_rows.append(data[i])
        return page_rows

    def index_range(self, page: int, page_size: int) -> Tuple[int, int]:
        '''
        Calculate the start and end indices for a given page
        in a paginated data set.

        Parameters:
        - page (int): The page number
        - page_size (int): The number of items per page.

        Returns:
        tuple: A tuple containing the start and end indices for the given page
        '''
        start_index = (page - 1) * page_size
        end_index = start_index + page_size

        return start_index, end_index
