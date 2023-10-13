from pathlib import Path

import quiz


def test_load_questions_from_file(questions):
    fixture = Path(__file__).resolve().parent.joinpath("fixtures", "quiz.csv")
    assert quiz.load_questions_from_file(fixture) == questions


def test_perform_quiz(questions):
    ...  # TODO


def test_display_question(question):
    ...  # TODO:


def test_gather_answer(question):
    ...  # TODO


def test_is_correct(question):
    assert quiz.is_correct(question, 1) is False
    assert quiz.is_correct(question, 2) is False
    assert quiz.is_correct(question, 3) is True
    assert quiz.is_correct(question, 4) is False
