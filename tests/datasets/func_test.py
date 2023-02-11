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


def test_dataset_filter_1(dataset, filter_1):
    filtered, *keys = filter_1
    assert datasets.filter_by_values(dataset, keys) == filtered


def test_dataset_filter_2(dataset, filter_2):
    filtered, *keys = filter_2
    assert datasets.filter_by_values(dataset, keys) == filtered


def test_dataset_filter_3(dataset, filter_3):
    filtered, *keys = filter_3
    assert datasets.filter_by_values(dataset, keys) == filtered


def test_dataset_filter_4(dataset, filter_4):
    filtered, *keys = filter_4
    assert datasets.filter_by_values(dataset, keys) == filtered


def test_dataset_filter_5(dataset, filter_5):
    filtered, *keys = filter_5
    assert datasets.filter_by_values(dataset, keys) == filtered


def test_dataset_filter_no_keys(dataset):
    # no unique rows in dataset
    assert datasets.filter_by_values(dataset) == dataset

    # 9 - 4 filter
    dataset = [
        {"x": 1, "y": 1}, {"x": 1, "y": 2}, {"x": 2, "y": 1},
        {"x": 1, "y": 1}, {"x": 2, "y": 1}, {"x": 2, "y": 2},
        {"x": 1, "y": 2}, {"x": 2, "y": 2}, {"x": 1, "y": 1},
    ]
    test_dataset = [
        {"x": 1, "y": 1}, {"x": 1, "y": 2}, {"x": 2, "y": 1}, {"x": 2, "y": 2},
    ]
    assert datasets.filter_by_values(dataset) == test_dataset
