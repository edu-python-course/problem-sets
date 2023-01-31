"""
Datasets functions implementation

"""

from typing import Dict, List


# brick wall challenge
def get_bricks_count(structure: List[List[int]]) -> int:
    """Return number of bricks in the wall structure

    :param structure: represents wall structure as sequences of integers
    :type structure: list[list[int]]

    :return: total number of bricks in the entire wall structure
    :rtype: int

    Usage:

    >>> get_bricks_count([[1], [1], [1]]) == 3
    >>> get_bricks_count([[1, 1, 1], [1, 1, 1]]) == 6
    >>> get_bricks_count([[2, 1, 2], [1, 1, 1, 1, 1]]) == 8

    """

    return sum(len(row) for row in structure)


def get_position_frequency(structure: List[List[int]]) -> Dict[int, int]:
    """Return a matrix of position-bricks pairs for a structure

    :param structure: represents wall structure as sequences of integers
    :type structure: list[list[int]]

    :return: the position - frequency matrix
    :rtype: dict[int, int]

    Usage:

    >>> assert get_position_frequency([[1], [1], [1]]) == {}
    >>> assert get_position_frequency([[1, 2], [2, 1], [3]]) = {1: 1, 2: 1}
    >>> assert get_position_frequency([[1, 1, 1], [1, 1, 1]]) = {1: 2, 2: 2}

    """

    structure_matrix = {}

    for row in structure:
        row_length = 0
        for brick_length in row[:-1]:
            row_length += brick_length
            if row_length not in structure_matrix:
                structure_matrix[row_length] = 0
            structure_matrix[row_length] += 1

    return structure_matrix


def get_least_bricks_position(structure: List[List[int]]) -> int:
    """Return a pointer to the weakest line in the structure

    :param structure: represents wall structure as sequences of integers
    :type structure: list[list[int]]

    :return: the distance from the left edge to the weakest line location
    :rtype: int

    This function uses helper function ``get_structure_matrix`` to build
    the matrix of distances from the left edge of the "wall".

    Usage:

    >>> assert get_least_bricks_position([[1], [1], [1]]) == 0
    >>> assert get_least_bricks_position([[1, 1, 1], [1, 1, 1]]) == 1

    """

    matrix = get_position_frequency(structure)
    if not matrix:
        return 0

    return max(matrix, key=matrix.get)  # type: ignore


def get_least_bricks_count(structure: List[List[int]]) -> int:
    """Return the least number of bricks in a vertical line

    :param structure: represents wall structure as sequences of integers
    :type structure: list[list[int]]

    :return: minimum number of bricks in a line
    :rtype: int

    Usage:

    >>> assert get_least_bricks_count([[1], [1], [1]]) == 3
    >>> assert get_least_bricks_count([[1, 2], [2, 1], [3], [1, 1, 1]]) == 2
    >>> assert get_least_bricks_count([[1, 1, 1], [1, 1, 1]]) == 0

    """

    max_value: int = 0
    matrix = get_position_frequency(structure)
    for count in matrix.values():
        max_value = max(max_value, count)

    return len(structure) - max_value
