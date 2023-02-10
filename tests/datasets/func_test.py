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


def test_dataset_filter_sm1(ds_sm, ds_sm_f1):
    filtered, *keys = ds_sm_f1
    assert datasets.filter_by_values(ds_sm, keys) == filtered


def test_dataset_filter_sm2(ds_sm, ds_sm_f2):
    filtered, *keys = ds_sm_f2
    assert datasets.filter_by_values(ds_sm, keys) == filtered


def test_dataset_filter_sm3(ds_sm, ds_sm_f3):
    filtered, *keys = ds_sm_f3
    assert datasets.filter_by_values(ds_sm, keys) == filtered


def test_dataset_filter_sm4(ds_sm, ds_sm_f4):
    filtered, *keys = ds_sm_f4
    assert datasets.filter_by_values(ds_sm, keys) == filtered


def test_dataset_filter_sm5(ds_sm, ds_sm_f5):
    filtered, *keys = ds_sm_f5
    assert datasets.filter_by_values(ds_sm, keys) == filtered


def test_dataset_filter_lg1(ds_lg, ds_lg_f1):
    filtered, *keys = ds_lg_f1
    assert datasets.filter_by_values(ds_lg, keys) == filtered


def test_dataset_filter_lg2(ds_lg, ds_lg_f2):
    filtered, *keys = ds_lg_f2
    assert datasets.filter_by_values(ds_lg, keys) == filtered


def test_dataset_filter_lg3(ds_lg, ds_lg_f3):
    filtered, *keys = ds_lg_f3
    assert datasets.filter_by_values(ds_lg, keys) == filtered


def test_dataset_filter_lg4(ds_lg, ds_lg_f4):
    filtered, *keys = ds_lg_f4
    assert datasets.filter_by_values(ds_lg, keys) == filtered


def test_dataset_filter_lg5(ds_lg, ds_lg_f5):
    filtered, *keys = ds_lg_f5
    assert datasets.filter_by_values(ds_lg, keys) == filtered
