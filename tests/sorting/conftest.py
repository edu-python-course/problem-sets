import pytest


@pytest.fixture
def unsorted_list():
    return [89, 83, 73, 3, 90, 96, 7, 24, 51, 38, 80, 56, 41, 44, 41, 3, 86, 44]


@pytest.fixture
def sorted_list():
    return [3, 3, 7, 24, 38, 41, 41, 44, 44, 51, 56, 73, 80, 83, 86, 89, 90, 96]


@pytest.fixture
def reversed_list():
    return [96, 90, 89, 86, 83, 80, 73, 56, 51, 44, 44, 41, 41, 38, 24, 7, 3, 3]


@pytest.fixture
def sorted_list_a():
    return [3, 38, 41, 41, 44, 44, 56, 80, 86]


@pytest.fixture
def sorted_list_b():
    return [3, 7, 24, 51, 73, 83, 89, 90, 96]
