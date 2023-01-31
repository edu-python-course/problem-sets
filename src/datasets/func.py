"""
Datasets functions implementation

"""

from typing import Dict, List


# TODO: this solution should be transformed to find the least number of
#       bricks in a vertical line

# brick wall challenge
def get_bricks_count(structure: List[List[int]]) -> int:
    """Return number of bricks in the wall structure

    :param structure: represents wall structure as sequences of integers
    :type structure: list[list[int]]

    :return: total number of bricks in the entire wall structure
    :rtype: int

    """

    return sum(len(row) for row in structure)


def get_structure_matrix(structure: List[List[int]]) -> Dict[int, int]:
    """Return a distance matrix for a structure

    :param structure: represents wall structure as sequences of integers
    :type structure: list[list[int]]

    :return: the distance-count matrix
    :rtype: dict[int, int]

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


def get_weakest_point(structure: List[List[int]]) -> int:
    """Return a pointer to the weakest line in the structure

    :param structure: represents wall structure as sequences of integers
    :type structure: list[list[int]]

    :return: the distance from the left edge to the weakest line location
    :rtype: int

    This function uses helper function ``get_structure_matrix`` to build
    the matrix of distances from the left edge of the "wall".

    """

    matrix = get_structure_matrix(structure)
    return max(matrix, key=matrix.get)  # type: ignore
