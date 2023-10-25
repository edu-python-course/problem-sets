import datasets


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
