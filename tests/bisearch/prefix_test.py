import pytest

from bisearch import prefix
from bisearch.prefix import NotFound


def test_prefix_right(strings_large_fixture, prefix_right_fixture):
    search, test_value = prefix_right_fixture
    assert prefix.bisect_right(strings_large_fixture, search) == test_value


def test_prefix_left(strings_large_fixture, prefix_left_fixture):
    search, test_value = prefix_left_fixture
    assert prefix.bisect_left(strings_large_fixture, search) == test_value


def test_find_all(strings_large_fixture, find_all_fixture):
    search, test_value = find_all_fixture
    assert prefix.find_all(strings_large_fixture, search) == test_value


def test_prefix_right_default(strings_small_fixture):
    string_idx = len(strings_small_fixture)
    assert prefix.bisect_right(strings_small_fixture) == string_idx


def test_prefix_left_default(strings_small_fixture):
    assert prefix.bisect_left(strings_small_fixture) == 0


def test_find_all_default(strings_small_fixture):
    assert prefix.find_all(strings_small_fixture) == strings_small_fixture


def test_prefix_right_last(strings_small_fixture):
    string_idx = len(strings_small_fixture)
    search = strings_small_fixture[-1]
    assert prefix.bisect_right(strings_small_fixture, search) == string_idx


def test_prefix_left_last(strings_small_fixture):
    string_idx = len(strings_small_fixture) - 1
    search = strings_small_fixture[-1]
    assert prefix.bisect_left(strings_small_fixture, search) == string_idx


def test_prefix_right_negative(strings_small_fixture):
    with pytest.raises(NotFound):
        prefix.bisect_right(strings_small_fixture, "d")


def test_prefix_left_negative(strings_small_fixture):
    with pytest.raises(NotFound):
        prefix.bisect_left(strings_small_fixture, "d")


def test_find_all_negative(strings_small_fixture):
    assert prefix.find_all(strings_small_fixture, "d") == []
