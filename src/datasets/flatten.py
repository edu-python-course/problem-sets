"""
Data flatten functions

"""

from typing import List, Union

NestedIntList = Union[int, List["NestedIntList"]]


def flatten_list(origin: List[NestedIntList]) -> List[int]:
    """
    Flattens a list of integers and nested lists of integers

    :param origin: an original list

    :return: a single-level list of integers

    Usage:

    >>> assert flatten_list([1, 2, 3]) == [1, 2, 3]
    >>> assert flatten_list(([[1], [2], [3]])) == [1, 2, 3]
    >>> assert flatten_list([1, [2, 3]]) == [1, 2, 3]
    >>> assert flatten_list([1, [[2], [3]]]) == [1, 2, 3]

    """

    result: List[int] = []

    for item in origin:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)

    return result
