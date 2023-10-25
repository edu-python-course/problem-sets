"""
Datasets functions implementation

"""

from typing import Dict, Hashable


def swap_dict_loop(origin: Dict[Hashable, Hashable]
                   ) -> Dict[Hashable, Hashable]:
    """
    Return a new dictionary with swapped keys and values from the original

    :param origin: the dictionary to swap the keys and values of
    :type origin: dict
    :return: a new dictionary with the swapped keys and values
    :rtype: dict

    The function iterates through the dictionary keys using a ``for`` loop.
    On each iteration step the value assigned at the original dictionary key
    is accessed. After that the values and key are written down to a new
    dictionary, but not using the value as key and vice versa.

    This is the most descriptive algorithm to solve the swap task.

    Usage:

    >>> swap_dict_loop({1: "one", 2: "two", 3: "three"})
    {"one": 1, "two": 2, "three": 3}

    """

    result = {}

    for key in origin:
        value = origin[key]
        result[value] = key

    return result


def swap_dict(origin: Dict[Hashable, Hashable]) -> Dict[Hashable, Hashable]:
    """
    Return a new dictionary with swapped keys and values from the original

    :param origin: the dictionary to swap the keys and values of
    :type origin: dict
    :return: a new dictionary with the swapped keys and values
    :rtype: dict

    Works similar to ``swap_dict_loop`` function, but uses dictionary
    comprehension instead of the ``for`` loop.

    Usage:

    >>> swap_dict({1: "one", 2: "two", 3: "three"})
    {"one": 1, "two": 2, "three": 3}

    """

    return {value: key for key, value in origin.items()}
