import functools
from typing import Dict, Tuple, Any

from calc.func import get_fibonacci_number as fib_classic


def memoize(func):
    cache: Dict[Tuple[Any], int] = {}

    @functools.wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)

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
