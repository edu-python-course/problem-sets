import functools
import logging
from typing import Dict, Tuple, Any

from calc.func import get_fibonacci_number as fib_classic

logging.basicConfig(level=logging.DEBUG)


def memoize(func):
    """Memoization decorator implementation

    The memoization technique helps to reduce the number of recursive
    calls by caching the results already calculated for some inputs.

    Current implementation caches the inputs as tuples containing args,
    so it has limitations for "un-hashable" inputs, that can not be
    stored in a cache dictionary.

    """

    cache: Dict[Tuple[Any], int] = {}

    @functools.wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
            logging.debug(f"cache updated: {args}, cache length: {len(cache)}")

        return cache[args]

    return wrapper


@memoize
@functools.wraps(fib_classic, ("__annotations__", "__doc__"))
def get_fibonacci_number(idx):
    if idx <= 0:
        return 0
    if idx < 3:
        return 1

    return get_fibonacci_number(idx - 1) + get_fibonacci_number(idx - 2)


@memoize
def get_grid_travels(height: int, width: int, /) -> int:
    """Calculate the number of available route for a specified grid size

    :param height: grid height
    :param width: grid width

    :return: the number of available routes
    :rtype: int

    The traveler starts the journey in the top-left corner of the grid
    and trying to reach the opposite grid corner (bottom-right).
    The only moves available are **move right** and **move down**.
    The task is to calculate the number of all available routes to do
    this.

    """

    if height <= 0 or width <= 0:
        return 0

    if height == 1 or width == 1:
        return 1

    return (get_grid_travels(height - 1, width)
            + get_grid_travels(height, width - 1))
