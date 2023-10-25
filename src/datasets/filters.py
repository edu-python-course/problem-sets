"""
Dataset filtering functions

"""

from typing import Any, Dict, Hashable, List, Optional, Set


def filter_by_values(origin: List[Dict[str, Hashable]],
                     keys: Optional[List[str]] = None
                     ) -> List[Dict[str, Any]]:
    """
    Return a filtered datasets by unique values in a given keys sets

    :param origin: an original dataset with entries to filter
    :type origin: list
    :param keys: a collection of keys to use for filtering
    :type keys: list, optional

    :return: a filtered dataset
    :rtype: list

    The origin dataset is a list of dictionaries. All the dictionaries have
    the same set of keys of a string type. All dictionaries values are of
    a hashable type.

    In case no data provided (``origin`` is an empty list) the function will
    return an empty list.

    The keys parameter is used to set the dictionary keys to filter unique
    values. Keys list is considered to be validated before passing to this
    function, all values (if any) are valid. In case this parameter is
    omitted - all available keys should be used.

    Usage:

    >>> ds = [{"x": 1, "y": 2, "z": 3}, {"x": 0, "y": 2, "z": 3}]
    >>> assert filter_by_values(ds, ["x"]) == ds       # the same as origin
    >>> assert filter_by_values(ds, ["x", "z"]) == ds  # the same as origin
    >>> assert filter_by_values(ds, ["y"]) == [{"x": 1, "y": 2, "z": 3}]
    >>> assert filter_by_values(ds, ["y", "z"]) == [{"x": 1, "y": 2, "z": 3}]

    """

    # check base cases
    if not origin:
        return []

    # declare variables to store runtime data
    filtered_dataset: List[Dict[str, Hashable]] = []
    filtered_values: Set[int] = set()

    keys = keys or origin[0].keys()  # type: ignore
    for entry in origin:
        entry_values = hash(tuple(map(entry.get, keys)))  # type: ignore
        if entry_values in filtered_values:
            continue

        filtered_values.add(entry_values)
        filtered_dataset.append(entry)

    return filtered_dataset
