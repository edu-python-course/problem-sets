import pytest

from bisearch import prefix
from bisearch.prefix import NotFound


def test_prefix_right(strings_large, prefix_right_fixture):
    search, test_value = prefix_right_fixture
    assert prefix.bisect_right(strings_large, search) == test_value


def test_prefix_left(strings_large, prefix_left_fixture):
    search, test_value = prefix_left_fixture
    assert prefix.bisect_left(strings_large, search) == test_value


def test_find_all(strings_large, find_all_fixture):
    search, test_value = find_all_fixture
    assert prefix.find_all(strings_large, search) == test_value


def test_prefix_right_default(strings_small):
    assert prefix.bisect_right(strings_small) == len(strings_small)


def test_prefix_left_default(strings_small):
    assert prefix.bisect_left(strings_small) == 0


def test_find_all_default(strings_small):
    assert prefix.find_all(strings_small) == strings_small


def test_prefix_right_negative(strings_small):
    with pytest.raises(NotFound):
        prefix.bisect_right(strings_small, "d")


def test_prefix_left_negative(strings_small):
    with pytest.raises(NotFound):
        prefix.bisect_left(strings_small, "d")


def test_find_all_negative(strings_small):
    assert prefix.find_all(strings_small, "d") == []
