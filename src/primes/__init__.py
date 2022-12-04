"""
Prime Numbers
=============

A prime number (or a prime) is a natural number greater than 1 that is not
a product of two smaller natural numbers.

Test Individual Number
----------------------

.. autofunction:: is_prime

Get Primes in Range
-------------------

.. autofunction:: get_primes

The Sieve of Eratosthenes
-------------------------

The more efficient algorithm to get primes within a range.

.. autofunction:: eratosthenes_sieve

"""

from .func import *

__all__ = [
    "is_prime",
    "get_primes",
    "eratosthenes_sieve",
]
