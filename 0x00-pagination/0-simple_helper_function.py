#!/usr/bin/env python3
'''This module define a function called index_range'''
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
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
