from dynamic import memoization


def test_get_fibonacci_number():
    # test base cases
    assert memoization.get_fibonacci_number(-10) == 0
    assert memoization.get_fibonacci_number(0) == 0
    assert memoization.get_fibonacci_number(1) == 1
    assert memoization.get_fibonacci_number(2) == 1
    # test custom cases
    assert memoization.get_fibonacci_number(3) == 2
    assert memoization.get_fibonacci_number(10) == 55
    assert memoization.get_fibonacci_number(50) == 12_586_269_025
    assert memoization.get_fibonacci_number(100) == 354_224_848_179_261_915_075


def test_get_grid_travels():
    # test base cases
    assert memoization.get_grid_travels(0, 0) == 0
    assert memoization.get_grid_travels(0, 1) == 0
    assert memoization.get_grid_travels(1, 0) == 0
    assert memoization.get_grid_travels(1, 1) == 1
    # test custom cases
    assert memoization.get_grid_travels(2, 3) == 3
    assert memoization.get_grid_travels(3, 2) == 3
    assert memoization.get_grid_travels(3, 3) == 6
    assert memoization.get_grid_travels(18, 18) == 2_333_606_220


def test_can_get_target():
    # test base cases
    assert memoization.can_get_target(-10, [1]) is False
    assert memoization.can_get_target(10, []) is False
    assert memoization.can_get_target(0, []) is True
    assert memoization.can_get_target(0, [1, 1, 1]) is True
    # test custom cases
    assert memoization.can_get_target(7, [2, 3]) is True
    assert memoization.can_get_target(7, [2, 4, 6]) is False
    assert memoization.can_get_target(8, [1, 3, 5]) is True
    assert memoization.can_get_target(300, [7, 14, 28]) is False
