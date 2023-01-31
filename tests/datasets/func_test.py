import datasets


def test_brick_counter(bricks_wall, number_of_bricks):
    assert datasets.get_bricks_count(bricks_wall) == number_of_bricks


def test_matrix_builder(bricks_wall, weakest_point):
    assert datasets.get_weakest_point(bricks_wall) == weakest_point
