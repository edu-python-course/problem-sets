"""
Search functions

"""

from typing import List


def is_present(value: int, matrix: List[List[int]]) -> bool:
    """
    Check if value is present within a 2D matrix

    :param value: an integer number to search
    :type value: int
    :param matrix: a 2d list of integers
    :type matrix: list

    :return: check result
    :rtype: bool

    The matrix of numbers follows the rules:

    - All numbers within a row are sorted ascending left-to-right
    - All numbers within a column are sorted ascending top-to-bottom

    """


def is_present_bf(value: int, matrix: List[List[int]]) -> bool:
    """
    Check if value is present within a 2D matrix

    :param value: an integer number to search
    :type value: int
    :param matrix: a 2d list of integers
    :type matrix: list

    :return: check result
    :rtype: bool

    The matrix of numbers follows the rules:

    - All numbers within a row are sorted ascending left-to-right
    - All numbers within a column are sorted ascending top-to-bottom

    This implementation uses the brute force approach.

    """
