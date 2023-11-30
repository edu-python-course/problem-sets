"""
Sequence Functions
==================

Palindrome Check
----------------

A palindrome is a word, number, phrase, or other sequence of characters
which reads the same backward as forward, such as madam or racecar.
Sentence-length palindromes ignore capitalization, punctuation, and word
boundaries.

.. seealso:: https://en.wikipedia.org/wiki/Palindrome

.. autofunction:: is_palindrome

Get the Longest Palindromic Substring
-------------------------------------

It's similar to `is_palindrome` check, but for now it tries to find the
longest palindromic substring inside another string.

.. autofunction:: get_longest_palindrome

Balanced Parentheses
--------------------

A parentheses are said to be balanced if each left parenthesis has its
respective right parenthesis to match its pair in a well-nested format.

.. autofunction:: are_parentheses_balanced

"""

__all__ = [
    "add_spaces",
    "get_consecutive_slices",
    "get_palindrome_squares",
    "get_palindrome_primes",
    "is_palindrome",
    "is_vowel",
    "get_longest_palindrome",
    "are_parentheses_balanced",
    "get_longest_uniq_length",
]

from sequences.func import (
    add_spaces,
    are_parentheses_balanced,
    get_consecutive_slices,
    get_longest_palindrome,
    get_longest_uniq_length,
    get_palindrome_primes,
    get_palindrome_squares,
    is_palindrome,
    is_vowel,
)
