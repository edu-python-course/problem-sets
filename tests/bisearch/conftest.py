from pathlib import Path

import pytest


@pytest.fixture
def strings_small():
    return sorted(["a", "b", "c", "ab", "bc", "ca", "abc", "bca", "cab"])


@pytest.fixture
def strings_large():
    # 10_000 strings generated with https://random.org
    fixture_path = Path(__file__).parent.joinpath("fixtures/strings.txt")
    with open(fixture_path) as fixture_file:
        return fixture_file.read().splitlines()


@pytest.fixture
def find_all_fixture():
    return ("ua",
            ["uaeafwqbag", "uasyolgnuc", "uaszazvdez", "uavmfgakey",
             "uawwitgssy", "uaxxgxmsrn", "uayppkjtny"])


@pytest.fixture
def prefix_right_fixture():
    return "sh", 7045


@pytest.fixture
def prefix_left_fixture():
    return "vp", 8291
