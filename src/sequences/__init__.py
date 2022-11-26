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

Balanced Parentheses
--------------------

A parentheses is said to be balanced if each left parenthesis has its
respective right parenthesis to match its pair in a well-nested format.

.. autofunction:: are_parentheses_balanced

"""

from .func import *

__all__ = ["is_palindrome", "are_parentheses_balanced"]