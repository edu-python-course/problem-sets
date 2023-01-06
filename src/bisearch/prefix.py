from typing import List


def bisect_right(origin: List[str], search: str = "") -> int:
    """Return the most right index

    :param origin: a list of strings
    :type origin: list[str]
    :param search: a prefix to search
    :type search: str

    :return: the index of the first string starting with search prefix
    :rtype: int

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

    return low


def bisect_left(origin: List[str], search: str = "") -> int:
    """Return the most left index

    :param origin: a list of strings
    :type origin: list[str]
    :param search: a prefix to search
    :type search: str

    :return: the index after the last string starting with search prefix
    :rtype: int

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

    return low


def find_all(origin: List[str], search: str = "") -> List[str]:
    start = bisect_left(origin, search)
    end = bisect_right(origin, search)

    return origin[start:end]
