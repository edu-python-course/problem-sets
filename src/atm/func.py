"""
ATM package functions

"""

from typing import Iterable, List, Optional, Sequence, Tuple

COINS: Tuple[int, ...] = 50, 25, 10, 5, 2, 1
BILLS: Tuple[int, ...] = 100_00, 50_00, 20_00, 10_00, 5_00, 2_00, 1_00
DENOMINATIONS: Tuple[int, ...] = BILLS + COINS


def withdraw(target: int,
             denominations: Optional[Sequence[int]] = None
             ) -> List[Tuple[int, int]]:
    """Return pairs of denominations and their multipliers

    :param target: the target amount to get
    :type target: int
    :param denominations: a list of denominations available to use. Defaults
        to ``(10000, 5000, 2000, 1000, 500, 200, 100, 50, 25, 10, 5, 2, 1)``
    :type denominations: tuple, Optional

    :return: a list of pairs containing denominations and their multipliers
    :rtype: list

    This algorithm uses a greedy approach, where the highest denomination
    available is always used as many times as possible to minimize the total
    number of coins/bills. If no exact solution is possible, the algorithm
    returns the largest possible amount that is less than the target amount.

    Usage:

    >>> assert withdraw(0) == []
    >>> assert withdraw(135) == [(1, 10), (1, 25), (1, 100)]
    >>> assert withdraw(100000) == [(10, 10000)]

    """

    # check base cases
    if target <= 0:
        return []

    # sort denominations in descending order
    if denominations is None:
        denominations = DENOMINATIONS
    denominations = sorted(denominations, reverse=True)

    size: int = len(denominations)
    multipliers = [0] * size

    for idx in range(size):
        multipliers[idx] = target // denominations[idx]
        target -= multipliers[idx] * denominations[idx]

    # filter zero multipliers
    filtered = filter(lambda val: val[0] > 0, zip(multipliers, denominations))

    return sorted(filtered, key=lambda val: val[1])


def withdraw_rev(target: int,
                 denominations: Optional[Sequence[int]] = None,
                 limit: Optional[int] = 10
                 ) -> List[Tuple[int, int]]:
    """Return pairs of denominations and their multipliers to reach target

    :param target: the target amount
    :type target: int
    :param denominations: denominations available to use. Defaults
        to ``(10000, 5000, 2000, 1000, 500, 200, 100, 50, 25, 10, 5, 2, 1)``
    :type denominations: tuple, Optional
    :param limit: restricts the number of times a denomination can be used
        to make up the target amount. Defaults to 10.
    :type limit: int, Optional

    This function uses a "reverse" version of a greedy algorithm and tries
    to use the smallest denominations as many times as it possible (it's
    limited with ``limit`` argument).

    Usage:
    #
    # >>> assert withdraw_rev(0) == []
    # >>> assert withdraw_rev(14) == [(10, 1), (2, 2)]
    # >>> assert withdraw_rev(17) == [(9, 1), (4, 2)]

    """

    raise NotImplementedError


def get_total(values: Iterable[Tuple[int, int]]) -> int:
    """Calculate the total sum

    :param values: pairs of denominations and their multipliers
    :type values: list

    :return: the total sum
    :rtype: int

    ``pairs`` is a list of tuples. Each ``pair`` tuple contains multiplier
    at the first position and denomination at the second one.

    Usage:

    >>> assert get_total([(1, 50), (1, 500), (2, 2000), (2, 10000)]) == 24550
    >>> assert get_total([(1, 10000), (1, 5000), (1, 2000), (1, 500)]) == 17500
    >>> assert get_total([(1, 2000)]) == 2000

    """

    return sum(map(lambda val: val[0] * val[1], values))
