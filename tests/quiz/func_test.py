from pathlib import Path
from unittest.mock import patch

import quiz


def test_load_questions_from_file(questions):
    fixture = Path(__file__).resolve().parent.joinpath("fixtures", "quiz.csv")
    assert quiz.load_questions_from_file(fixture) == questions


def test_perform_quiz(questions, correct_answers, incorrect_answers):
    with patch("builtins.input", side_effect=correct_answers):
        assert quiz.perform_quiz(questions) == len(questions)

    with patch("builtins.input", side_effect=incorrect_answers):
        assert quiz.perform_quiz(questions) == 0


def test_display_question(question):
    ...  # TODO:


def test_gather_answer(question):
    with patch("builtins.input", side_effect=["1", "3", "4", "2"]):
        assert quiz.gather_answer(question) == 1
        assert quiz.gather_answer(question) == 3
        assert quiz.gather_answer(question) == 4
        assert quiz.gather_answer(question) == 2


def test_gather_answer_repeat():
    question = {
        "options": ["opt 1", "opt 2"],
        "question": "", "answer": "",
    }

    side_effect = ["0", "3", "2"]
    with patch("builtins.input", side_effect=side_effect) as mock_input:
        quiz.gather_answer(question)
        assert mock_input.call_count == 3

    side_effect = ["0", "3", "1"]
    with patch("builtins.input", side_effect=side_effect) as mock_input:
        quiz.gather_answer(question)
        assert mock_input.call_count == 3


def test_is_correct(question):
    assert quiz.is_correct(question, 1) is False
    assert quiz.is_correct(question, 2) is False
    assert quiz.is_correct(question, 3) is True
    assert quiz.is_correct(question, 4) is False
