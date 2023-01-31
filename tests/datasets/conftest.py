import pytest


@pytest.fixture
def short_bricks_wall():
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
def regular_brick_wall_mtx():
    return {5: 4, 10: 4, 13: 3, 17: 2, 3: 2, 6: 2, 12: 1, 2: 1, 11: 1, 16: 1,
            7: 1, 14: 1, 15: 1}


@pytest.fixture
def weakest_point():
    return 5


@pytest.fixture
def number_of_bricks():
    return 29


@pytest.fixture
def least_bricks():
    return 1
