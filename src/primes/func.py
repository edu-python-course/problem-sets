"""
Prime Lookup Functions

"""

import math
from typing import List


def is_prime(number: int) -> bool:
    """Return prime check result for a specified number

    The result of this function is True if a number is prime, otherwise
    False.

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
    """Return a list of prime numbers within specified range

    :param limit: a range limit to look for prime numbers
    :type limit: int

    :return: the list of prime numbers within a specified range
    :rtype: list[int]

    """

    return [number for number in range(limit + 1) if is_prime(number)]


def eratosthenes_sieve(limit: int) -> List[int]:
    """Return a list of prime numbers till specified limit

    In mathematics, the sieve of Eratosthenes is an ancient algorithm for
    finding all prime numbers up to any given limit.

    It does so by iteratively marking as composite (i.e., not prime) the
    multiples of each prime, starting with the first prime number, 2.
    The multiples of a given prime are generated as a sequence of numbers
    starting from that prime, with constant difference between them that is
    equal to that prime. This is the sieve's key distinction from using
    trial division to sequentially test each candidate number for
    divisibility by each prime. Once all the multiples of each discovered
    prime have been marked as composites, the remaining unmarked numbers
    are primes.

    This makes this algorithm one of the most efficient approach to find
    primes within a range.

    .. seealso:: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

    :param limit: a range limit to look for prime numbers
    :type limit: int

    :return: the list of prime numbers within a specified range
    :rtype: list[int]


    """

    sieve: List[bool] = [False, False] + [True] * limit

    for idx in range(2, int(math.sqrt(limit)) + 1):
        if sieve[idx]:
            for j in range(idx ** 2, limit + 1, idx):
                sieve[j] = False

    return [idx for idx in range(2, limit + 1) if sieve[idx]]
