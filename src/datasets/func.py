"""
Datasets functions implementation

"""

from typing import Any, Dict, Hashable, List, Optional, Set, Tuple, Union


def swap_dict_loop(origin: Dict[Hashable, Hashable]
                   ) -> Dict[Hashable, Hashable]:
    """
    Return a new dictionary with swapped keys and values from the original

    :param origin: the dictionary to swap the keys and values of
    :type origin: dict
    :return: a new dictionary with the swapped keys and values
    :rtype: dict

    The function iterates through the dictionary keys using a ``for`` loop.
    On each iteration step the value assigned at the original dictionary key
    is accessed. After that the values and key are written down to a new
    dictionary, but not using the value as key and vice versa.

    This is the most descriptive algorithm to solve the swap task.

    Example usage:

    >>> swap_dict_loop({1: "one", 2: "two", 3: "three"})
    {"one": 1, "two": 2, "three": 3}

    """

    result = {}

    for key in origin:
        value = origin[key]
        result[value] = key

    return result


def swap_dict(origin: Dict[Hashable, Hashable]) -> Dict[Hashable, Hashable]:
    """
    Return a new dictionary with swapped keys and values from the original

    :param origin: the dictionary to swap the keys and values of
    :type origin: dict
    :return: a new dictionary with the swapped keys and values
    :rtype: dict

    Works similar to ``swap_dict_loop`` function, but uses dictionary
    comprehension instead of the ``for`` loop.

    Example usage:

    >>> swap_dict({1: "one", 2: "two", 3: "three"})
    {"one": 1, "two": 2, "three": 3}

    """

    return {value: key for key, value in origin.items()}


# define typing hints aliases
StudentData = Dict[str, Union[str, List[int]]]  # student data type alias
StudentsList = List[StudentData]  # students data type alias


def get_avg_score(student_data: StudentData) -> float:
    """Return average score of a student"""

    scores: List[int] = student_data["scores"]  # type: ignore

    return round(sum(scores) / len(scores))


def get_top_student(students_data: StudentsList) -> StudentData:
    """
    Return a student who has the highest average score

    :param students_data: a list of students data (names and scores)
    :type students_data: list

    :return: student data entity
    :rtype: dict

    """

    threshold = float("-inf")  # negative infinite, less that any number
    result = {"name": "", "scores": []}

    for student in students_data:
        avg_score = get_avg_score(student)
        if avg_score > threshold:
            threshold = avg_score
            result = student  # type: ignore

    return result  # type: ignore


def get_low_student(students_data: StudentsList) -> StudentData:
    """
    Return the student who has the lowest average score

    :param students_data: a list of students data (names and scores)
    :type students_data: list

    :return: student data entity
    :rtype: dict

    """

    threshold = float("+inf")  # positive infinite, bigger that any number
    result = {"name": "", "scores": []}

    for student in students_data:
        avg_score = get_avg_score(student)
        if avg_score < threshold:
            threshold = avg_score
            result = student  # type: ignore

    return result  # type: ignore


def get_both_top_low_students(students_data: StudentsList
                              ) -> Tuple[StudentData, StudentData]:
    """
    Return both top and low students data

    Given a list of student data, returns a tuple of the student with
    the highest average score and the student with the lowest average score.
    The student data is represented as a list of dictionaries, where each
    dictionary contains the keys 'name' and 'scores', where 'name' is
    a string and 'scores' is a list of floats representing the student's
    scores on various exams.

    :param students_data: A list of dictionaries containing the student data.
    :type students_data: list

    :return: A tuple of two dictionaries representing the student with
        the highest average score and the student with the lowest average
        score. Each dictionary contains the keys 'name' and 'scores',
        where 'name' is a string and 'scores' is a list of floats
        representing the student's scores on various exams.
    :rtype: tuple

    """

    min_score_threshold, max_score_threshold = float("+inf"), float("-inf")
    top_student = {"name": "", "scores": []}
    low_student = {"name": "", "scores": []}

    for student in students_data:
        avg_score = get_avg_score(student)
        if avg_score > max_score_threshold:
            max_score_threshold = avg_score
            top_student = student  # type: ignore
        if avg_score < min_score_threshold:
            min_score_threshold = avg_score
            low_student = student  # type: ignore

    return top_student, low_student  # type: ignore


def get_bricks_count(structure: List[List[int]]) -> int:
    """
    Return number of bricks in the wall structure

    :param structure: represents wall structure as sequences of integers
    :type structure: list

    :return: total number of bricks in the entire wall structure
    :rtype: int

    Usage:

    >>> assert get_bricks_count([[1], [1], [1]]) == 3
    >>> assert get_bricks_count([[1, 1, 1], [1, 1, 1]]) == 6
    >>> assert get_bricks_count([[2, 1, 2], [1, 1, 1, 1, 1]]) == 8

    """

    return sum(len(row) for row in structure)


def get_position_frequency(structure: List[List[int]]) -> Dict[int, int]:
    """
    Return a matrix of position-bricks pairs for a structure

    :param structure: represents wall structure as sequences of integers
    :type structure: list

    :return: the position - frequency matrix
    :rtype: dict

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
    """
    Return a pointer to the weakest line in the structure

    This function uses helper function ``get_structure_matrix`` to build
    the matrix of distances from the left edge of the "wall".

    :param structure: represents wall structure as sequences of integers
    :type structure: list

    :return: the distance from the left edge to the weakest line location
    :rtype: int

    Usage:

    >>> assert get_least_bricks_position([[1], [1], [1]]) == 0
    >>> assert get_least_bricks_position([[1, 1, 1], [1, 1, 1]]) == 1

    """

    matrix = get_position_frequency(structure)
    if not matrix:
        return 0

    return max(matrix, key=matrix.get)  # type: ignore


def get_least_bricks_count(structure: List[List[int]]) -> int:
    """
    Return the least number of bricks in a vertical line

    :param structure: represents wall structure as sequences of integers
    :type structure: list

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


def filter_by_values(origin: List[Dict[str, Hashable]],
                     keys: Optional[List[str]] = None
                     ) -> List[Dict[str, Any]]:
    """
    Return a filtered datasets by unique values in a given keys sets

    The origin dataset is a list of dictionaries. All the dictionaries have
    the same set of keys of a string type. All dictionaries values are of
    a hashable type.

    In case no data provided (``origin`` is an empty list) the function will
    return an empty list.

    The keys parameter is used to set the dictionary keys to filter unique
    values. Keys list is considered to be validated before passing to this
    function, all values (if any) are valid. In case this parameter is
    omitted - all available keys should be used.

    :param origin: an original dataset with entries to filter
    :type origin: list
    :param keys: a collection of keys to use for filtering
    :type keys: list, optional

    :return: a filtered dataset
    :rtype: list

    Usage:

    >>> ds = [{"x": 1, "y": 2, "z": 3}, {"x": 0, "y": 2, "z": 3}]
    >>> assert filter_by_values(ds, ["x"]) == ds       # the same as origin
    >>> assert filter_by_values(ds, ["x", "z"]) == ds  # the same as origin
    >>> assert filter_by_values(ds, ["y"]) == [{"x": 1, "y": 2, "z": 3}]
    >>> assert filter_by_values(ds, ["y", "z"]) == [{"x": 1, "y": 2, "z": 3}]

    """

    # check base cases
    if not origin:
        return []

    # declare variables to store runtime data
    filtered_dataset: List[Dict[str, Hashable]] = []
    filtered_values: Set[int] = set()

    keys = keys or origin[0].keys()  # type: ignore
    for entry in origin:
        entry_values = hash(tuple(map(entry.get, keys)))  # type: ignore
        if entry_values in filtered_values:
            continue

        filtered_values.add(entry_values)
        filtered_dataset.append(entry)

    return filtered_dataset


NestedIntList = Union[int, List["NestedIntList"]]


def flatten(origin: List[NestedIntList]) -> List[int]:
    """
    Flattens a list of integers and nested lists of integers

    :param origin: an original list

    :return: a single-level list of integers

    Usage:

    >>> assert flatten([1, 2, 3]) == [1, 2, 3]
    >>> assert flatten(([[1], [2], [3]])) == [1, 2, 3]
    >>> assert flatten([1, [2, 3]]) == [1, 2, 3]
    >>> assert flatten([1, [[2], [3]]]) == [1, 2, 3]

    """

    result: List[int] = []

    for item in origin:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)

    return result
