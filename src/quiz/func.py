"""
Quiz functions

A single question is a dictionary of a strict structure:
```
{
    "question": "Question text...",
    "options": ["opt 1", "opt 2", "opt 3", "opt 4"],
    "answer": "opt 1",
}
```

"""

from __future__ import annotations

from typing import List, TYPE_CHECKING, TypedDict, Union

if TYPE_CHECKING:
    import pathlib

Question = TypedDict("Question", {
    "question": str,
    "options": List[str],
    "answer": str,
})
Questions = List[Question]


def load_questions_from_file(source: Union[str, pathlib.Path]) -> Questions:
    """
    Load quiz data from the given source file

    :param source: path for the source file
    :type source: str | :class: `pathlib.Path`

    :return: quiz data
    :rtype: list

    """


def display_question(question: Question) -> None:
    """
    Display a question to the user

    :param question: a question dictionary
    :type question: dict

    """


def gather_answer(question: Question) -> int:
    """
    Collect a question answer from the user

    :param question: a question dictionary
    :type question: dict

    :return: the answer option number
    :rtype: int

    """


def is_correct(question: Question, option: int) -> bool:
    """
    Check if the given answer option is correct for the question

    :param question: a question dictionary
    :type question: dict
    :param option: the answer option number starting from 1
    :type option: int

    :return: check result
    :rtype: bool

    """


def perform_quiz(questions: Questions) -> int:
    """
    Perform quiz and evaluate the user's response

    :param questions: a list of question dictionaries
    :type questions: list

    :return: the number of questions answered correctly
    :rtype: int

    """
