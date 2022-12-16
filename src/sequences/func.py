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


def get_longest_palindrome(origin: str) -> str:
    # noinspection SpellCheckingInspection
    """Return the longest palindrome substring from the given input

    :param origin:
    :type origin: str

    :return: the longest palindrome
    :rtype: str

    Usage examples:

    >>> assert get_longest_palindrome("ABBABBC") == "BBABB"

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


def get_fibonacci_number(idx: int) -> int:
    """Return a Fibonacci's sequence number at a specified index

    :param idx: a Fibonacci sequence index starting from 0
    :type idx: int

    :return: a sequence's member
    :rtype: int

    The Fibonacci number is a number from the Fibonacci sequence, in which
    each number is the sum of the two preceding ones. This sequence commonly
    starts from 0 and 1: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144...

    Usage examples:

    >>> assert get_fibonacci_number(0) == 0
    >>> assert get_fibonacci_number(1) == 1
    >>> assert get_fibonacci_number(2) == 1
    >>> assert get_fibonacci_number(3) == 2
    >>> assert get_fibonacci_number(4) == 3

    """

    if idx <= 0:
        return 0

    if 0 < idx < 3:  # the same as ``idx == 1 or idx == 2``
        return 1

    return get_fibonacci_number(idx - 1) + get_fibonacci_number(idx - 2)


def get_longest_uniq_length(origin: str) -> int:
    """Return the length of the longest on sequence of unique characters

    Usage examples:
    
    >>> assert get_longest_uniq_length("abcdefg") == 7
    >>> assert get_longest_uniq_length("abcacba") == 3

    :param origin: original sequences
    :type origin: str

    :return: the length of the longest unique characters sequence
    :rtype: int

    """

    length: int = 0

    size: int = len(origin)
    left_idx: int = 0

    for right_idx in range(size):
        while origin[right_idx] in origin[left_idx:right_idx]:
            left_idx += 1
        length = max(length, right_idx - left_idx + 1)

    return length


def get_strings_sum(number_1: str, number_2: str) -> str:
    """Return the sum of two numbers of string type as string

    :param number_1: first number
    :type number_1: str
    :param number_2: second number
    :type number_2: str

    :return: the sum of two numbers
    :rtype: str

    """

    result: str = ""
    size: int = max(len(number_1), len(number_2))

    # reverse numbers
    number_1, number_2 = number_1[::-1], number_2[::-1]

    # make strings of the same lengths
    while len(number_1) < size:
        number_1 += "0"
    while len(number_2) < size:
        number_2 += "0"

    carry: int = 0
    for digit_1, digit_2 in zip(number_1, number_2):
        sum_of_digits = int(digit_1) + int(digit_2) + carry
        result += str(sum_of_digits % 10)
        carry = sum_of_digits // 10

    if carry:
        result += str(carry)

    return result[::-1]


if __name__ == "__main__":
    print(f"{get_strings_sum('456', '789') = }")
