"""
functions
"""

from typing import List, Optional, Tuple

COINS = 50, 25, 10, 5, 2, 1
BILLS = 100_00, 50_00, 20_00, 10_00, 5_00, 2_00, 1_00
DENOMINATIONS = BILLS + COINS


def withdraw(amount: int,
             denominations: Optional[List[int]] = None
             ) -> List[Tuple[int, int]]:
    if amount <= 0:
        return []

    denominations = denominations or DENOMINATIONS
    multipliers = [0] * len(denominations)
    den_idx = 0

    while amount > 0:
        if amount // denominations[den_idx]:
            multipliers[den_idx] += 1
            amount -= denominations[den_idx]
        else:
            den_idx += 1

    # filter zero multipliers
    filtered = filter(lambda pair: pair[0] > 0, zip(multipliers, denominations))

    return list(filtered)


def get_total(amount: List[Tuple[int, int]]) -> int:
    balance = 0
    for multiplier, denomination in amount:
        balance += multiplier * denomination

    return balance
