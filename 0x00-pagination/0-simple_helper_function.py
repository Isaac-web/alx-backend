#!/usr/bin/env python3
"""
This module contains a function that generate the start
and end indices of a data range.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return the start and end indices of a data range
    """

    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
