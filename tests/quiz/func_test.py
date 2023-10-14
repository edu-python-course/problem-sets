from pathlib import Path
from unittest.mock import patch

import quiz


def test_load_questions_from_file(questions):
    fixture = Path(__file__).resolve().parent.joinpath("fixtures", "quiz.csv")
    assert quiz.load_questions_from_file(fixture) == questions


def test_perform_quiz(questions):
    ...  # TODO


def test_display_question(question):
    ...  # TODO:


def test_gather_answer(question):
    with patch("builtins.input", return_value="1"):
        answer = quiz.gather_answer(question)
    assert answer == 0


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
