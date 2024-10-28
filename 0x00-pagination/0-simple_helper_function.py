#!/usr/bin/env python3
""" Calculates the start and end indices for a given page and page size.  """
from typing import Tuple


def index_range(page: int, page_size: int) -> tuple:
    """
    Calculates the start and end indices for a given page and page size.

     Args:
        page (int): Page number (1-indexed).
        page_size (int): Number of items per page.

    Returns:
        tuple: A tuple containing the start index and end index.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
