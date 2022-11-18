"""
Sequence functions implementations

"""

import string


def is_palindrome(origin: str) -> bool:
    """Return a palindrome check result

    :param origin: a string to test
    :type origin: str

    :return: return a palindrome check result
    :rtype: bool

    This function implements two pointers method. The left pointer is
    initialized at the beginning of an origin string, and the right one -
    at the end. The check cycle compares characters at left and right
    indexes. Once the comparison is false the function returns False.
    Once left pointer is greater or equal to the right one the function
    returns True. Punctuation, word boundaries and capitalization are
    ignored.

    Usage examples:

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


def are_parentheses_balanced(origin: str) -> bool:
    """Return a validation result for a given parentheses sequence

    :param origin: a parentheses sequence to validate
    :type origin: str

    :return: a validation result
    :rtype: bool

    Validation rules:

    * each opening parentheses must be closed by the same type parentheses
    * open parentheses must be closed in the correct order
    * any non-parentheses characters are to be ignored

    Usage examples:

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
