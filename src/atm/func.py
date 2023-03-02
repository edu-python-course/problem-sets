"""
ATM package functions

"""

from typing import Iterable, List, Optional, Sequence, Tuple

COINS: Tuple[int, ...] = 1, 2, 5, 10, 25, 50
BILLS: Tuple[int, ...] = 100_00, 50_00, 20_00, 10_00, 5_00, 2_00, 1_00
DENOMINATIONS: Tuple[int, ...] = BILLS + COINS


def withdraw(target: int,
             denominations: Optional[Sequence[int]] = None
             ) -> List[Tuple[int, int]]:
    """Return pairs of denominations and their multipliers to get target number


    :param target: the target amount to get
    :type target: int
    :param denominations: a list of denominations available to use. Defaults
        to ``DENOMINATIONS``
    :type denominations: tuple, Optional

    :return: a list of pairs containing denominations and their multipliers
    :rtype: list

    Usage examples:

    >>> assert withdraw(0) == []
    >>> assert withdraw(100) == [(1, 100)]
    >>> assert withdraw(135) == [(1, 10), (1, 25), (1, 100)]

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
    filtered = filter(lambda pair: pair[0] > 0, zip(multipliers, denominations))

    return sorted(filtered, key=lambda pair: pair[1])


def withdraw_rev(target: int,
                 denominations: Optional[Sequence[int]] = None,
                 limit: Optional[int] = 10
                 ) -> List[Tuple[int, int]]:
    """Return pairs of denominations and their multipliers to reach target

    :param target: the target amount
    :type target: int
    :param denominations: denominations available to use. Defaults
        to ``DENOMINATIONS``.
    :type denominations: tuple, Optional
    :param limit: restricts the number of times a denomination can be used
        to make up the target amount. Defaults to 10.
    :type limit: int, Optional

    Usage examples:

    >>> assert withdraw_rev(0) == []
    >>> assert withdraw_rev(14) == [(10, 1), (2, 2)]
    >>> assert withdraw_rev(17) == [(9, 1), (4, 2)]

    """

    if target < 1:
        return []

    if denominations is None:
        denominations = DENOMINATIONS
    denominations = sorted(denominations)

    size: int = len(denominations)
    multipliers = [0] * size

    for idx in range(size):
        multipliers[idx] = min(limit, target // denominations[idx])
        target -= multipliers[idx] * denominations[idx]

    # filter zero multipliers
    filtered = filter(lambda pair: pair[0] > 0, zip(multipliers, denominations))

    return sorted(filtered, key=lambda pair: pair[1])


def get_total(pairs: Iterable[Tuple[int, int]]) -> int:
    """Calculate the total sum

    :param pairs: pairs of denominations and their multipliers
    :type pairs: list

    :return: the total sum
    :rtype: int

    ``pairs`` is a list of tuples. Each ``pair`` tuple contains multiplier
    at the first position and denomination at the second one.

    Usage examples:

    >>> assert get_total([(1, 50), (1, 500), (2, 2000), (2, 10000)]) == 24500
    >>> assert get_total([(1, 500), (1, 2000), (1, 5000), (1, 10000)]) == 17545
    >>> assert get_total([(1, 2000)]) == 2000

    """

    return sum(map(lambda pair: pair[0] * pair[1], pairs))
