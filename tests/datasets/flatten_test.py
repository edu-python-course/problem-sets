import datasets


def test_flatten_list():
    assert datasets.flatten_list([1, 2, 3]) == [1, 2, 3]
    assert datasets.flatten_list(([[1], [2], [3]])) == [1, 2, 3]
    assert datasets.flatten_list([1, [2, 3]]) == [1, 2, 3]
    assert datasets.flatten_list([1, [[2], [3]]]) == [1, 2, 3]
