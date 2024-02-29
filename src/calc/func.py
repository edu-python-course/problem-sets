"""
Calculation functions implementations

"""

from typing import List


def get_square(number: int) -> int:
    """
    Calculate the square value of a given number

    :param number: The input number for which the square value is calculated.
    :type number: int

    :return: the square value of the input number
    :rtype: int

    """

    return number ** 2


def get_squares(limit: int, /) -> List[int]:
    """
    Return a list of squares within a specified limit

    :param limit: range limit
    :type limit: int

    :return: list of squares
    :rtype: list

    """

    return [get_square(number) for number in range(limit)]


def get_factorial(number: int, carrier: int = 1, /) -> int:
    """
    Return the factorial value for a given number

    In mathematics the factorial is the product of all positive integers
    less than or equal to given number.
    E.g. 5! = 5 * 4! = 5 * 4 * 3 * 2 * 1 = 120.
    The value of 0! = 1 according to the convention of an empty product.

    :param number: the number to calculate the factorial value for
    :type number: int
    :param carrier: the calculation result carrier, defaults to 1
    :type carrier: int, optional

    :return: the factorial value
    :rtype: int

    Usage:

    >>> assert get_factorial(0) == 1
    >>> assert get_factorial(5) == 120

    """

    if number <= 1:
        return carrier

    return get_factorial(number - 1, carrier * number)


def get_factorial_nr(number: int, /) -> int:
    """
    Return the factorial value for a given number

    In mathematics the factorial is the product of all positive integers
    less than or equal to given number.
    E.g. 5! = 5 * 4! = 5 * 4 * 3 * 2 * 1 = 120.
    The value of 0! = 1 according to the convention of an empty product.

    :param number:
    :type number: int

    :return: the factorial value
    :rtype: int

    This function implements the non-recursive algorithm, which is more
    efficient, since it does not have multiple recursive calls.

    Usage:

    >>> assert get_factorial(0) == 1
    >>> assert get_factorial(5) == 120

    """

    factorial = 1
    for iter_number in range(1, number + 1):
        factorial *= iter_number

    return factorial


def get_fibonacci_number(idx: int, /) -> int:
    """
    Return a Fibonacci's sequence number at a specified index

    The Fibonacci number is a number from the Fibonacci sequence, in which
    each number is the sum of the two preceding ones. This sequence commonly
    starts from 0 and 1: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144...

    :param idx: a Fibonacci sequence index starting from 0
    :type idx: int

    :return: a sequence's member
    :rtype: int

    Usage:

    >>> assert get_fibonacci_number(0) == 0
    >>> assert get_fibonacci_number(1) == 1
    >>> assert get_fibonacci_number(2) == 1
    >>> assert get_fibonacci_number(3) == 2
    >>> assert get_fibonacci_number(4) == 3

    """

    if idx <= 0:
        return 0

    if idx <= 1:
        return 1

    return get_fibonacci_number(idx - 1) + get_fibonacci_number(idx - 2)


def get_fibonacci_number_nr(idx: int, /) -> int:
    """
    Return a Fibonacci's sequence number at a specified index

    :param idx: a Fibonacci sequence index starting from 0
    :type idx: int

    :return: a sequence's member
    :rtype: int

    This function implements the non-recursive algorithm, which is more
    efficient, since it does not have multiple recursive calls.

    Usage:

    >>> assert get_fibonacci_number(0) == 0
    >>> assert get_fibonacci_number(1) == 1
    >>> assert get_fibonacci_number(2) == 1
    >>> assert get_fibonacci_number(3) == 2
    >>> assert get_fibonacci_number(4) == 3

    """

    if idx <= 0:
        return 0

    if idx <= 1:
        return 1

    previous, fib_number = 0, 1
    for _ in range(idx - 1):
        previous, fib_number = fib_number, previous + fib_number

    return fib_number


def get_sum_of_strings(number_1: str, number_2: str, /) -> str:
    """
    Return the sum of two numbers of string type as string

    :param number_1: first number
    :type number_1: str
    :param number_2: second number
    :type number_2: str

    :return: the sum of two numbers
    :rtype: str

    Valid input is a string of any length containing numeric characters from
    0 to 9. Empty strings are allowed as well and should be considered as 0.

    Usage:

    >>> assert get_sum_of_strings("123", "456") == "579"
    >>> assert get_sum_of_strings("099", "001") == "100"
    >>> assert get_sum_of_strings("", "10") == "10"
    >>> assert get_sum_of_strings("", "") == "0"

    """

    # remove leading zeros
    number_1 = number_1.lstrip("0")
    number_2 = number_2.lstrip("0")

    if not number_1 or not number_2:
        return number_1 or number_2 or "0"

    result: str = ""
    size: int = max(len(number_1), len(number_2))

    # reverse numbers
    number_1, number_2 = number_1[::-1], number_2[::-1]

    # make strings of the same lengths
    number_1 += "0" * (size - len(number_1))
    number_2 += "0" * (size - len(number_2))

    carry: int = 0
    for digit_1, digit_2 in zip(number_1, number_2):
        sum_of_digits = int(digit_1) + int(digit_2) + carry
        result += str(sum_of_digits % 10)
        carry = sum_of_digits // 10

    if carry:
        result += str(carry)

    return result[::-1]


def get_digits_multiplies(origin: int) -> List[int]:
    """
    Return the digits multiplies for a given number

    :param origin: a number to find multiplies
    :type origin: int

    :return: a list of digits multiplies starting from position 10 ** 1
    :rtype: list

    """

    return [int(digit) for digit in str(origin)[::-1]]
