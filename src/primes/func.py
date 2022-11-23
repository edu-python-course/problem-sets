import math
from typing import List


def is_prime(number: int) -> bool:
    """Return prime check result for a specified number

    :param number: number to check
    :type number: int

    :return: prime check result
    :rtype: bool

    """

    if number < 2:
        return False

    for divider in range(2, int(math.sqrt(number)) + 1):
        if not number % divider:
            return False

    return True


def get_primes(limit: int) -> List[int]:
    """Return a list of prime numbers till specified limit"""

    result: List[int] = []

    for number in range(2, limit + 1):
        if is_prime(number):
            result.append(number)

    return result


def eratosthenes_sieve(limit: int) -> List[int]:
    """Return a list of prime numbers till specified limit"""

    sieve: List[bool] = [False, False] + [True] * limit

    for idx in range(2, limit + 1):
        if sieve[idx]:
            for j in range(idx ** 2, limit + 1, idx):
                sieve[j] = False

    return [idx for idx in range(2, limit + 1) if sieve[idx]]
