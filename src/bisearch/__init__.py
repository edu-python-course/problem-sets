"""
Binary Search
=============

The binary search algorithm (a.k.a **half-interval search** or **bisect**)
is a search algorithm that finds the position of a target value within
a sorted array. The origin dataset is required to be sorted before applying
to bisect. This algorithm runs in a logarithmic time in the worst case,
making O(log_n) comparisons.

The general idea is to divide the initial array in two equal portions, and
to compare the middle value with the requested one. Since array in case
the middle value is greater than the search one, the left portion can be
excluded from the future search (vice versa the right one excluded). After
that the search algorithm is applied for the right part only.

.. seealso:: https://en.wikipedia.org/wiki/Binary_search_algorithm

"""
