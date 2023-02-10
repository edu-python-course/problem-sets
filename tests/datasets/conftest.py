import csv
from pathlib import Path

import pytest

FIXTURES_PATH = Path(__file__).resolve().parent.joinpath("fixtures")


@pytest.fixture
def small_bricks_wall():
    return [[1], [1], [1]]


@pytest.fixture
def bricks_wall():
    return [
        [5, 5, 3, 4, 1],
        [3, 2, 1, 4, 2, 1, 5],
        [2, 3, 1, 5, 5, 2],
        [3, 4, 3, 4, 3, 1],
        [5, 5, 3, 2, 3],
    ]


@pytest.fixture
def matrix():
    return {5: 4, 10: 4, 13: 3, 17: 2, 3: 2, 6: 2, 12: 1, 2: 1, 11: 1, 16: 1,
            7: 1, 14: 1, 15: 1}


@pytest.fixture
def position():
    return 5


@pytest.fixture
def bricks_count():
    return 29


@pytest.fixture
def least_bricks():
    return 1


def read_fixture(filename):
    with open(filename) as csv_file_handler:
        return [row for row in csv.DictReader(csv_file_handler)]


@pytest.fixture
def ds_sm():
    filename = FIXTURES_PATH.joinpath("ds_sm.csv")
    return read_fixture(filename)


@pytest.fixture
def ds_sm_f1():
    filename = FIXTURES_PATH.joinpath("ds_sm_f1.csv")
    return read_fixture(filename), "first_name"


@pytest.fixture
def ds_sm_f2():
    filename = FIXTURES_PATH.joinpath("ds_sm_f2.csv")
    return read_fixture(filename), "gender"


@pytest.fixture
def ds_sm_f3():
    filename = FIXTURES_PATH.joinpath("ds_sm_f3.csv")
    return read_fixture(filename), "first_name", "age"


@pytest.fixture
def ds_sm_f4():
    filename = FIXTURES_PATH.joinpath("ds_sm_f4.csv")
    return read_fixture(filename), "last_name", "gender"


@pytest.fixture
def ds_sm_f5():
    filename = FIXTURES_PATH.joinpath("ds_sm_f5.csv")
    return read_fixture(filename), "last_name", "city"


@pytest.fixture
def ds_lg():
    filename = FIXTURES_PATH.joinpath("ds_lg.csv")
    return read_fixture(filename)


@pytest.fixture
def ds_lg_f1():
    filename = FIXTURES_PATH.joinpath("ds_lg_f1.csv")
    return read_fixture(filename), "first_name"


@pytest.fixture
def ds_lg_f2():
    filename = FIXTURES_PATH.joinpath("ds_lg_f2.csv")
    return read_fixture(filename), "gender"


@pytest.fixture
def ds_lg_f3():
    filename = FIXTURES_PATH.joinpath("ds_lg_f3.csv")
    return read_fixture(filename), "first_name", "age"


@pytest.fixture
def ds_lg_f4():
    filename = FIXTURES_PATH.joinpath("ds_lg_f4.csv")
    return read_fixture(filename), "last_name", "gender"


@pytest.fixture
def ds_lg_f5():
    filename = FIXTURES_PATH.joinpath("ds_lg_f5.csv")
    return read_fixture(filename), "last_name", "city"
