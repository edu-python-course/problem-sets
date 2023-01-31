import datasets


def test_brick_counter(regular_brick_wall):
    fixture, _, bricks_count = regular_brick_wall
    assert datasets.get_bricks_count(fixture) == bricks_count


def test_matrix_builder(regular_brick_wall):
    fixture, line_position, _ = regular_brick_wall
    assert datasets.get_weakest_point(fixture) == line_position
