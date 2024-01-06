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

import csv
from typing import List, TYPE_CHECKING, TypedDict, Union

if TYPE_CHECKING:  # pragma: no cover
    import pathlib  # pragma: no cover

Question = TypedDict("Question", {
    "question": str,
    "options": List[str],
    "answer": str,
})
Questions = List[Question]


# noinspection PyTypeChecker
def load_questions_from_file(source: Union[str, pathlib.Path]) -> Questions:
    """
    Load quiz data from the given source file

    :param source: path for the source file
    :type source: str | :class: `pathlib.Path`

    :return: quiz data
    :rtype: list

    """

    fieldnames = ["question", "options", "answer"]
    questions = []
    with open(source) as io_buff:  # pylint: disable=W1514
        reader = csv.DictReader(io_buff, fieldnames=fieldnames)
        for question in reader:
            questions.append({
                fieldnames[0]: question[fieldnames[0]],
                fieldnames[1]: [option.strip() for option in
                                question[fieldnames[1]].split(",")],
                fieldnames[2]: question[fieldnames[2]],
            })
    return questions  # type: ignore


def display_question(question: Question) -> None:
    """
    Display a question to the user

    :param question: a question dictionary
    :type question: dict

    """

    print("%s\n" % question["question"])  # pylint: disable=C0209
    for opt_idx, option in enumerate(question["options"], 1):
        print("%d: %s" % (opt_idx, option))  # pylint: disable=C0209


def gather_answer(question: Question) -> int:
    """
    Collect a question answer from the user

    :param question: a question dictionary
    :type question: dict

    :return: the answer option number
    :rtype: int

    """

    # this assignment does not assume input type validation
    choice = -1
    choice_limit = len(question["options"])
    while not 0 <= choice - 1 < choice_limit:
        choice = int(input("Option no. to submit: "))

    return choice


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

    return question["answer"] == question["options"][option - 1]


def perform_quiz(questions: Questions) -> int:
    """
    Perform quiz and evaluate the user's response

    :param questions: a list of question dictionaries
    :type questions: list

    :return: the number of questions answered correctly
    :rtype: int

    """

    score: int = 0

    for question in questions:
        display_question(question)
        option_idx = gather_answer(question)
        score += is_correct(question, option_idx)

    return score
