import datasets


def test_brick_counter(bricks_wall, bricks_count):
    assert datasets.get_bricks_count(bricks_wall) == bricks_count


def test_matrix_builder(bricks_wall, position):
    assert datasets.get_least_bricks_position(bricks_wall) == position


def test_least_bricks(bricks_wall, small_bricks_wall):
    assert datasets.get_least_bricks_count(bricks_wall) == 1
    assert datasets.get_least_bricks_count(small_bricks_wall) == 3


def test_original_case():
    wall = [[1, 2, 2, 1],
            [3, 1, 2],
            [1, 3, 2],
            [2, 4],
            [3, 1, 2],
            [1, 3, 1, 1]]
    assert datasets.get_least_bricks_count(wall) == 2
