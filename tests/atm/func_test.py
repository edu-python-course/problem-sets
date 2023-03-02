import pytest

import atm


def test_get_total():
    assert atm.get_total([]) == 0

    assert atm.get_total([(1, 2000)]) == 2000
    assert atm.get_total([(2, 10000), (2, 2000), (1, 500), (1, 50)]) == 24550
    assert atm.get_total([(1, 10000), (1, 5000), (1, 2000), (1, 500)]) == 17500
    assert atm.get_total([(1, 2000), (1, 500), (1, 200), (1, 100),
                          (1, 25), (2, 10), (1, 2), (1, 1)]) == 2848


def test_withdraw():
    assert atm.withdraw(-100) == []
    assert atm.withdraw(0) == []

    assert atm.withdraw(24550) == [(1, 50), (1, 500), (2, 2000), (2, 10000)]
    assert atm.withdraw(17500) == [(1, 500), (1, 2000), (1, 5000), (1, 10000)]
    assert atm.withdraw(2848) == [(1, 1), (1, 2), (2, 10), (1, 25),
                                  (1, 100), (1, 200), (1, 500), (1, 2000)]
    assert atm.withdraw(2000) == [(1, 2000)]


def test_withdraw_outcome_balance():
    assert atm.get_total(atm.withdraw(24500)) == 24500
    assert atm.get_total(atm.withdraw(17545)) == 17545
    assert atm.get_total(atm.withdraw(2000)) == 2000


@pytest.mark.xfail(reason="not implemented")
def test_withdraw_rev():
    assert atm.withdraw_rev(-500) == []
    assert atm.withdraw_rev(0) == []

    assert atm.withdraw_rev(5) == [(5, 1)]
    assert atm.withdraw_rev(10) == [(10, 1)]
    assert atm.withdraw_rev(14) == [(10, 1), (2, 2)]
    assert atm.withdraw_rev(17) == [(9, 1), (4, 2)]
