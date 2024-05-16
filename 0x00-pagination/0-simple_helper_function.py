#!/usr/bin/env python3
"""
0-simple_helper_function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    ''' returns the start and end index pased of page number and page isze '''
    start_index: int = (page - 1) * page_size
    return (start_index, start_index + page_size)
