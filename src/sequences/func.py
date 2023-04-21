"""
Sequence functions implementations

"""

import string


def is_palindrome(origin: str) -> bool:
    """
    Return a palindrome check result

    This function implements two pointers method. The left pointer is
    initialized at the beginning of an origin string, and the right one -
    at the end. The check cycle compares characters at left and right
    indexes. Once the comparison is false the function returns False.
    Once left pointer is greater or equal to the right one the function
    returns True. Punctuation, word boundaries and capitalization are
    ignored.

    :param origin: a string to test
    :type origin: str

    :return: return a palindrome check result
    :rtype: bool

    Usage:

    >>> assert is_palindrome("aba") is True
    >>> assert is_palindrome("abc") is False

    """

    origin = origin.lower()
    skip_chars: str = string.punctuation + string.whitespace
    left: int = 0
    right: int = len(origin) - 1

    while left < right:
        if origin[left] in skip_chars:
            left += 1
            continue

        if origin[right] in skip_chars:
            right -= 1
            continue

        if origin[left] != origin[right]:
            return False

        left += 1
        right -= 1

    return True


def get_longest_palindrome(origin: str) -> str:
    """
    Return the longest palindrome substring from the given input

    :param origin:
    :type origin: str

    :return: the longest palindrome
    :rtype: str

    Usage:

    >>> assert get_longest_palindrome("0123219") == "12321"
    >>> assert get_longest_palindrome("1012210") == "012210"

    """

    size: int = len(origin)

    def expand(left: int, right: int) -> int:
        while left >= 0 and right < size and origin[left] == origin[right]:
            left -= 1
            right += 1

        return right - left - 1

    start = end = 0

    for idx in range(size):
        length_1 = expand(idx, idx)
        length_2 = expand(idx, idx + 1)

        max_length = max(length_1, length_2)
        if max_length > end - start:
            start = idx - (max_length - 1) // 2
            end = idx + max_length // 2

    return origin[start:end + 1]


def are_parentheses_balanced(origin: str) -> bool:
    """
    Return a validation result for a given parentheses sequence

    Validation rules:

    - each opening parentheses must be closed by the same type parentheses
    - open parentheses must be closed in the correct order
    - any non-parentheses characters are to be ignored

    :param origin: a parentheses sequence to validate
    :type origin: str

    :return: a validation result
    :rtype: bool

    Usage:

    >>> assert are_parentheses_balanced("({[]})") is True
    >>> assert are_parentheses_balanced(")]}{[(") is False

    """

    opening = "{", "[", "(", "<"
    closing = "}", "]", ")", ">"
    parentheses_map = dict(zip(closing, opening))
    parentheses_stack = []

    for parentheses in origin:
        if parentheses in opening:
            parentheses_stack.append(parentheses)
            continue

        if parentheses in closing and not parentheses_stack:
            return False

        if parentheses in closing:
            if parentheses_stack.pop() != parentheses_map[parentheses]:
                return False

    return not parentheses_stack


def get_longest_uniq_length(origin: str) -> int:
    """
    Return the length of the longest on sequence of unique characters

    :param origin: original sequences
    :type origin: str

    :return: the length of the longest unique characters sequence
    :rtype: int

    Usage:

    >>> assert get_longest_uniq_length("abcdefg") == 7
    >>> assert get_longest_uniq_length("racecar") == 4

    """

    length: int = 0

    size: int = len(origin)
    left_idx: int = 0

    for right_idx in range(size):
        while origin[right_idx] in origin[left_idx:right_idx]:
            left_idx += 1
        length = max(length, right_idx - left_idx + 1)

    return length
