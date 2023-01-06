"""
Dynamic programming tabulation functions

"""

import functools
from typing import List

from calc.func import get_fibonacci_number as fib_classic


@functools.wraps(fib_classic, ("__annotations__", "__doc__"))
def get_fibonacci_number(idx):
    if idx <= 0:
        return 0

    table: List[int] = [0, 1] + [0] * idx

    for i in range(idx):
        table[i + 1] += table[i]
        table[i + 2] += table[i]

    return table[idx]
