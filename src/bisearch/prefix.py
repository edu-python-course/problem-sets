"""
Prefix challenge
================

The objective is to get all strings, that start with a specified prefixes,
from the sorted collection.

The most efficient way is to use binary search algorithm for this task.

"""

from typing import List


class NotFound(Exception):
    """Raised in case the search function failed to find requested value"""


def bisect_right(origin: List[str], search: str = "") -> int:
    """Return the most right index

    :param origin: a list of strings
    :type origin: list[str]
    :param search: a prefix to search
    :type search: str

    :return: the index after the last string starting with search prefix
    :rtype: int

    :raise: NotFound

    """

    low: int = 0
    high: int = len(origin)
    prefix_size: int = len(search)

    while low < high:
        idx = low + (high - low) // 2  # the same as (high + low) // 2
        cur = origin[idx][:prefix_size]

        if cur <= search:
            low = idx + 1
        else:
            high = idx

    if low >= len(origin) and not origin[-1].startswith(search):
        raise NotFound(f"'{search}'")

    return low


def bisect_left(origin: List[str], search: str = "") -> int:
    """Return the most left index

    :param origin: a list of strings
    :type origin: list[str]
    :param search: a prefix to search
    :type search: str

    :return: the index of the first string starting with search prefix
    :rtype: int

    :raise: NotFound

    """

    low: int = 0
    high: int = len(origin)
    prefix_size: int = len(search)

    while low < high:
        idx = low + (high - low) // 2  # the same as (high + low) // 2
        cur = origin[idx][:prefix_size]

        if cur < search:
            low = idx + 1
        else:
            high = idx

    if low >= len(origin):
        raise NotFound(f"'{search}'")

    return low


def find_all(origin: List[str], search: str = "") -> List[str]:
    """Return strings starting with prefix

    :param origin: the list of strings
    :type origin: list[str]
    :param search: the prefix to search, defaults to empty string
    :type search: str

    :return: the list of strings starting with the search prefix
    :rtype: list[str]

    """

    try:
        start = bisect_left(origin, search)
        end = bisect_right(origin, search)

        return origin[start:end]

    except NotFound:
        return []
