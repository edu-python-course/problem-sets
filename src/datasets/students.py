"""
Students dataset challenge functions

"""

from typing import List, Tuple, TypedDict

StudentData = TypedDict("StudentData", {
    "name": str,
    "groups": List[str],
    "scores": List[int],
})
StudentsList = List[StudentData]


def get_avg_score(student_data: StudentData) -> float:
    """Return average score of a student"""

    scores: List[int] = student_data["scores"]

    return round(sum(scores) / len(scores))


def get_top_student(students_data: StudentsList) -> StudentData:
    """
    Return a student who has the highest average score

    :param students_data: a list of students data (names and scores)
    :type students_data: list

    :return: student data
    :rtype: dict

    """

    threshold = float("-inf")  # negative infinite, less that any number

    result = StudentData(name="", groups=[], scores=[])
    for student in students_data:
        avg_score = get_avg_score(student)
        if avg_score > threshold:
            threshold = avg_score
            result = student

    return result


def get_low_student(students_data: StudentsList) -> StudentData:
    """
    Return the student who has the lowest average score

    :param students_data: a list of students data (names and scores)
    :type students_data: list

    :return: student data entity
    :rtype: dict

    """

    threshold = float("+inf")  # positive infinite, bigger that any number
    result = StudentData(name="", groups=[], scores=[])

    for student in students_data:
        avg_score = get_avg_score(student)
        if avg_score < threshold:
            threshold = avg_score
            result = student

    return result


def get_both_top_low_students(students_data: StudentsList
                              ) -> Tuple[StudentData, StudentData]:
    """
    Return both top and low students data

    :param students_data: A list of dictionaries containing the student data.
    :type students_data: list

    :return: A tuple of two dictionaries representing the student with
        the highest average score and the student with the lowest average
        score. Each dictionary contains the keys 'name' and 'scores',
        where 'name' is a string and 'scores' is a list of floats
        representing the student's scores on various exams.
    :rtype: tuple

    Given a list of student data, returns a tuple of the student with
    the highest average score and the student with the lowest average score.
    The student data is represented as a list of dictionaries, where each
    dictionary contains the keys 'name' and 'scores', where 'name' is
    a string and 'scores' is a list of floats representing the student's
    scores on various exams.

    """

    min_score_threshold, max_score_threshold = float("+inf"), float("-inf")
    top_student = StudentData(name="", groups=[], scores=[])
    low_student = StudentData(name="", groups=[], scores=[])

    for student in students_data:
        avg_score = get_avg_score(student)
        if avg_score > max_score_threshold:
            max_score_threshold = avg_score
            top_student = student
        if avg_score < min_score_threshold:
            min_score_threshold = avg_score
            low_student = student

    return top_student, low_student
