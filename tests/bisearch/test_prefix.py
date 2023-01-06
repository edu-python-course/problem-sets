from bisearch import prefix


def test_prefix_right(strings_fixtures, pr_fixture):
    search, test_value = pr_fixture
    assert prefix.bisect_right(strings_fixtures, search) == test_value


def test_prefix_left(strings_fixtures, pl_fixture):
    search, test_value = pl_fixture
    assert prefix.bisect_left(strings_fixtures, search) == test_value


def test_find_all(strings_fixtures, fa_fixture):
    search, test_value = fa_fixture
    assert prefix.find_all(strings_fixtures, search) == test_value
