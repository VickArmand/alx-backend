#!/usr/bin/env python3
"""This file has a class Server and function index_range"""
import csv
import math
from typing import List, Tuple, Dict


def index_range(page: int, page_size: int) -> Tuple[int]:
    """
    The function should return a tuple of size
    two containing a start index and an end index
    corresponding to the range of indexes to return
    in a list for those particular pagination parameters.
    Page numbers are 1-indexed, i.e. the first page is page 1.
    """
    startIndex = 0
    endIndex = startIndex + page_size
    index = 1
    while index < page:
        startIndex += page_size
        endIndex += page_size
        index += 1
    return (startIndex, endIndex)


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
        takes two integer arguments page with
        default value 1 and page_size with default value 10.
        Use assert to verify that both arguments are integers greater than 0.
        Use index_range to find the correct indexes
        to paginate the dataset correctly and
        return the appropriate page of the dataset
        (i.e. the correct list of rows).
        If the input arguments are out of range for the dataset,
        an empty list should be returned.
        """
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        indexes = index_range(page, page_size)
        self.dataset()
        if self.__dataset and len(self.__dataset) >= indexes[1]:
            return self.__dataset[indexes[0]: indexes[1]]
        return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        takes the same arguments (and defaults) as get_page and
        returns a dictionary containing the following key-value pairs:
        page_size: the length of the returned dataset page
        page: the current page number
        data: the dataset page (equivalent to return from previous task)
        next_page: number of the next page, None if no next page
        prev_page: number of the previous page, None if no previous page
        total_pages: the total number of pages in the dataset as an integer
        """
        data = self.get_page(page, page_size)
        prev_page = None if page == 1 else page - 1
        total_pages = math.ceil(len(self.__dataset) / page_size)
        next_page = page + 1 if page < total_pages else None
        return {"page_size": page_size, "page": page, "data": data,
                "next_page": next_page, "prev_page": prev_page,
                "total_pages": total_pages}
