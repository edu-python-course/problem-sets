"""
Dynamic programming memoization functions

"""

import functools
from typing import Any, Callable, Dict, List, Optional, Tuple

from calc.func import get_factorial as fac_classic
from calc.func import get_fibonacci_number as fib_classic


def memoize(func: Callable) -> Callable:
    """
    Memoization decorator

    :param func: a function to decorate with memoization technique

    :return: the decorated function

    The memoization technique helps to reduce the number of recursive
    calls by caching the results already calculated for some inputs.

    Current implementation caches the inputs as tuples containing args,
    so it has limitations for "un-hashable" inputs, that can not be
    stored in a cache dictionary.

    """

    cache: Dict[Tuple[Any, ...], int] = {}

    @functools.wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)

        return cache[args]

    return wrapper


@memoize
@functools.wraps(fac_classic, ("__annotations__", "__doc__"))
def get_factorial(number, carrier=1):  # pylint: disable=C0116
    if number <= 1:
        return carrier

    return get_factorial(number - 1, carrier * number)


@memoize
@functools.wraps(fib_classic, ("__annotations__", "__doc__"))
def get_fibonacci_number(idx):  # pylint: disable=C0116
    if idx <= 0:
        return 0
    if idx < 3:
        return 1

    return get_fibonacci_number(idx - 1) + get_fibonacci_number(idx - 2)


@memoize
def get_grid_travels(height: int, width: int, /) -> int:
    """
    Calculate the number of available route for a specified grid size

    :param height: grid height
    :type height: int
    :param width: grid width
    :type width: int

    :return: the number of available routes
    :rtype: int

    The traveler starts the journey in the top-left corner of the grid
    and trying to reach the opposite grid corner (bottom-right).
    The only moves available are **move right** and **move down**.
    The task is to calculate the number of all available routes to do
    this.

    Usage:

    >>> assert get_grid_travels(1, 0) == 0
    >>> assert get_grid_travels(1, 1) == 1
    >>> assert get_grid_travels(2, 3) == 3
    >>> assert get_grid_travels(3, 2) == 3

    """

    if height <= 0 or width <= 0:
        return 0

    if height == 1 or width == 1:
        return 1

    return (get_grid_travels(height - 1, width)
            + get_grid_travels(height, width - 1))


def can_get_target(target: int, numbers: List[int],
                   cache: Optional[Dict[int, bool]] = None) -> bool:
    """
    Check if the target value can be generated using given numbers

    :param target: the desired number
    :type target: int
    :param numbers: the sequence of numbers available for usage
    :type numbers: list
    :param cache: optional dictionary that stores already calculated results
    :type cache: dict, optional

    :return: the check result
    :rtype: bool

    Numbers from the list can be used as many times as needed.

    Usage:

    >>> assert can_get_target(0, []) is True
    >>> assert can_get_target(0, [1, 1, 1]) is True
    >>> assert can_get_target(7, [2, 3]) is True
    >>> assert can_get_target(7, [2, 4, 6]) is False

    """

    # check base cases
    if target < 0:
        return False

    if not target:
        return True

    # check cached values
    cache = cache or {}
    if target in cache:
        return cache[target]

    # perform calculation
    for number in numbers:
        cache[target] = can_get_target(target - number, numbers, cache)
        if cache[target]:
            return True

    return False
