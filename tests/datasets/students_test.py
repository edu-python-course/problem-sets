from datasets import students


def test_average_score(student_data):
    assert students.get_avg_score(student_data) == 8.0


def test_get_top_student(students_list, top_student_data):
    assert students.get_top_student(students_list) == top_student_data


def test_get_low_student(students_list, low_student_data):
    assert students.get_low_student(students_list) == low_student_data


def test_both_top_and_low(students_list, top_student_data, low_student_data):
    result = students.get_both_top_low_students(students_list)
    assert result == (top_student_data, low_student_data)
