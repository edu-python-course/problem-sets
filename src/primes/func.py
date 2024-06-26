"""
Prime Lookup Functions

"""

import math
from typing import List


def is_prime(number: int) -> bool:
    """
    Return prime check result for a specified number

    :param number: number to check
    :type number: int

    :return: prime check result
    :rtype: bool

    The result of this function is True if a number is prime, otherwise
    False.

    Usage:

    >>> assert not is_prime(0)
    >>> assert not is_prime(1)
    >>> assert is_prime(2)
    >>> assert is_prime(3)
    >>> assert not is_prime(4)
    >>> assert is_prime(5)

    """

    if number < 2:
        return False

    for divider in range(2, int(math.sqrt(number)) + 1):
        if not number % divider:
            return False

    return True


def get_primes(limit: int) -> List[int]:
    """
    Return a list of prime numbers within specified range

    :param limit: a range limit to look for prime numbers
    :type limit: int

    :return: the list of prime numbers within a specified range
    :rtype: list

    Usage:

    >>> assert get_primes(10) == [2, 3, 5, 7]
    >>> assert get_primes(20) == [2, 3, 5, 7, 11, 13, 17, 19]

    """

    return [number for number in range(limit + 1) if is_prime(number)]


def eratosthenes_sieve(limit: int) -> List[int]:
    """
    Return a list of prime numbers till specified limit

    :param limit: a range limit to look for prime numbers
    :type limit: int

    :return: the list of prime numbers within a specified range
    :rtype: list

    In mathematics, the sieve of Eratosthenes is an ancient algorithm
    for finding all prime numbers up to any given limit.

    It does so by iteratively marking as composite (i.e., not prime) the
    multiples of each prime, starting with the first prime number, 2.
    The multiples of a given prime are generated as a sequence of
    numbers starting from that prime, with constant difference between
    them that is equal to that prime. This is the sieve's key
    distinction from using trial division to sequentially test each
    candidate number for divisibility by each prime. Once all the
    multiples of each discovered prime have been marked as composites,
    the remaining unmarked numbers are primes.

    This makes this algorithm one of the most efficient approach to find
    primes within a range.

    .. seealso:: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

    Usage:

    >>> assert eratosthenes_sieve(10) == [2, 3, 5, 7]
    >>> assert eratosthenes_sieve(20) == [2, 3, 5, 7, 11, 13, 17, 19]

    """

    sieve: List[bool] = [False, False] + [True] * limit

    for idx in range(2, int(math.sqrt(limit)) + 1):
        if sieve[idx]:
            for j in range(idx ** 2, limit + 1, idx):
                sieve[j] = False

    return [idx for idx in range(2, limit + 1) if sieve[idx]]
