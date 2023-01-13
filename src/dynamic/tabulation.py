"""
Dynamic programming tabulation functions

"""

import functools
from typing import List, Optional, Tuple, Union

from calc.func import get_fibonacci_number as fib_classic


@functools.wraps(fib_classic, ("__annotations__", "__doc__"))
def get_fibonacci_number(idx):  # pylint:disable=C0116
    if idx <= 0:
        return 0

    table: List[int] = [0, 1] + [0] * idx

    for i in range(idx):
        table[i + 1] += table[i]
        table[i + 2] += table[i]

    return table[idx]


def get_grid_travels(height: int, width: int, /) -> int:
    """Calculate the number of available route for a specified grid size

    :param height: grid height
    :param width: grid width

    :return: the number of available routes
    :rtype: int

    The traveler starts the journey in the top-left corner of the grid
    The only moves available are **move right** and **move down**.
    and trying to reach the opposite grid corner (bottom-right).
    The task is to calculate the number of all available routes to do
    this.

    """

    if height <= 0 or width <= 0:
        return 0

    table: List[List[int]] = [[0] * (width + 1) for _ in range(height + 1)]
    table[1][1] = 1

    for row_idx in range(height + 1):
        for col_idx in range(width + 1):
            # traveling down
            if row_idx + 1 <= height:
                table[row_idx + 1][col_idx] += table[row_idx][col_idx]

            # traveling right
            if col_idx + 1 <= width:
                table[row_idx][col_idx + 1] += table[row_idx][col_idx]

    return table[height][width]


def can_get_target(target: int, numbers: List[int]) -> bool:
    """Check if the target value can be generated using given numbers

    :param target: the desired number
    :type target: int
    :param numbers: the sequence of numbers available for usage
    :type numbers: list[int]

    :return: the check result
    :rtype: bool

    Numbers from the list can be used as many times as needed.

    """

    # check base cases
    if target < 0:
        return False

    # initialize values table
    table: List[bool] = [True] + [False] * target
    size: int = target + 1

    # inner function uses closure with ``idx`` variable from the outer scope
    def iterate_numbers():
        for number in numbers:
            set_value(idx + number)

    # inner function uses closure with ``size`` and ``table`` variables
    # from the outer scope
    def set_value(table_idx):
        if table_idx < size:
            table[table_idx] = True

    # perform calculation
    idx: int = 0
    while not table[target] and idx < size:
        if table[idx]:
            iterate_numbers()
        idx += 1

    return table[target]


def get_target_numbers(target: int, numbers: List[int]) -> Optional[List[int]]:
    """Return a collection of numbers to get the target one if possible

    :param target: the desired number
    :type target: int
    :param numbers: the sequence of numbers available for usage
    :type numbers: list[int]

    :return: None if impossible, otherwise list of numbers
    :rtype: list[int] | None

    This function returns the best collection of numbers to generate the
    target one. If it's impossible to generate None will be returned.

    The shortest one available sequence is considered the best one.

    Numbers can be used as many times as it needed.

    """

    # check base cases
    if target < 0:
        return None

    # initialize values table
    table: List[Union[None, List[int]]] = [None] * (target + 1)
    table[0] = []
    size: int = target + 1

    # inner function uses closure with ``idx`` variable from the outer scope
    def iterate_numbers():
        for number in numbers:
            set_value(idx + number, number)

    # inner function uses closure with ``idx`` and ``table`` variables
    # from the outer scope
    def set_value(table_idx, value):
        if table_idx >= size:
            return

        current = table[table_idx]
        updated = [*table[idx], value]

        if current is None or len(current) > len(updated):
            table[table_idx] = updated

    # perform calculation
    idx: int = 0
    while idx < size:
        if table[idx] is not None:
            iterate_numbers()

        idx += 1

    return table[target]


def get_chunks(origin: List[int]) -> Tuple[List[int], List[int]]:
    """Return two chunks of the origin list

    :param origin: an original sequence of numbers
    :type origin: list[int]

    :return: chunks of the origin list with equal (or closed to) sum
    :rtype: tuple[list[int, list[int]]

    The original list is split based on chunks sums. This means, that
    the difference between partitions sums is as minimal as possible.

    """

    # TODO: add implementation
    list_1: List[int] = []
    list_2: List[int] = sorted(origin)

    return list_1, list_2
