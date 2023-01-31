import pytest


@pytest.fixture
def regular_brick_wall():
    structure = [
        [5, 5, 3, 4, 1],
        [3, 2, 1, 4, 2, 1, 5],
        [2, 3, 1, 5, 5, 2],
        [3, 4, 3, 4, 3, 1],
        [5, 5, 3, 2, 3],
    ]
    line_position = 5
    bricks_count = 29

    return structure, line_position, bricks_count
