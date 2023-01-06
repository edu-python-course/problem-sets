from pathlib import Path

import pytest


@pytest.fixture
def strings_fixtures():
    fixture_path = Path(__file__).parent.joinpath("fixtures/strings.txt")
    with open(fixture_path) as fixture_file:
        return fixture_file.read().splitlines()


@pytest.fixture
def fa_fixture():
    return (
        "ua",
        ["uaeafwqbag", "uasyolgnuc", "uaszazvdez", "uavmfgakey", "uawwitgssy",
         "uaxxgxmsrn", "uayppkjtny", ]
    )


@pytest.fixture
def pr_fixture():
    return "sh", 7045


@pytest.fixture
def pl_fixture():
    return "vp", 8291
