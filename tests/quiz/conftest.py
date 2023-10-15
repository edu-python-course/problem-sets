import pytest


@pytest.fixture
def question():
    return {
        "question": "What's up doc?",
        "options": ["option 1", "option 2", "option 3", "option 4"],
        "answer": "option 3",
    }


@pytest.fixture
def questions():
    return [
        {
            "question": "Question no.1",
            "options": ["opt 1", "opt 2", "opt 3", "opt 4"],
            "answer": "opt 1",
        },
        {
            "question": "Question no.2",
            "options": ["opt 1", "opt 2", "opt 3", "opt 4"],
            "answer": "opt 2",
        },
        {
            "question": "Question no.3",
            "options": ["opt 1", "opt 2", "opt 3", "opt 4"],
            "answer": "opt 4",
        },
        {
            "question": "Question no.4",
            "options": ["opt 1", "opt 2", "opt 3", "opt 4"],
            "answer": "opt 3",
        },
        {
            "question": "Question no.5",
            "options": ["opt 1", "opt 2", "opt 3", "opt 4"],
            "answer": "opt 3",
        },
    ]


@pytest.fixture
def correct_answers():
    return "1", "2", "4", "3", "3"


@pytest.fixture
def incorrect_answers():
    return "2", "1", "2", "1", "2"
