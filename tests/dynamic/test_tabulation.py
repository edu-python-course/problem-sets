from dynamic import tabulation


def test_get_fibonacci_number():
    # test base cases
    assert tabulation.get_fibonacci_number(-10) == 0
    assert tabulation.get_fibonacci_number(0) == 0
    assert tabulation.get_fibonacci_number(1) == 1
    assert tabulation.get_fibonacci_number(2) == 1
    # test custom cases
    assert tabulation.get_fibonacci_number(3) == 2
    assert tabulation.get_fibonacci_number(10) == 55
    assert tabulation.get_fibonacci_number(50) == 12_586_269_025
    assert tabulation.get_fibonacci_number(100) == 354_224_848_179_261_915_075


def test_get_grid_travels():
    # test base cases
    assert tabulation.get_grid_travels(0, 0) == 0
    assert tabulation.get_grid_travels(0, 1) == 0
    assert tabulation.get_grid_travels(1, 0) == 0
    assert tabulation.get_grid_travels(1, 1) == 1
    # test custom cases
    assert tabulation.get_grid_travels(2, 3) == 3
    assert tabulation.get_grid_travels(3, 2) == 3
    assert tabulation.get_grid_travels(3, 3) == 6
    assert tabulation.get_grid_travels(18, 18) == 2_333_606_220


def test_can_get_target():
    # test base cases
    assert tabulation.can_get_target(-10, [1]) is False
    assert tabulation.can_get_target(10, []) is False
    assert tabulation.can_get_target(0, []) is True
    assert tabulation.can_get_target(0, [1, 1, 1]) is True
    # test custom cases
    assert tabulation.can_get_target(7, [2, 3]) is True
    assert tabulation.can_get_target(7, [2, 4, 6]) is False
    assert tabulation.can_get_target(8, [1, 3, 5]) is True
    assert tabulation.can_get_target(300, [7, 14, 28]) is False


def test_get_target_numbers():
    # test base cases
    assert tabulation.get_target_numbers(-10, [1]) is None
    assert tabulation.get_target_numbers(10, []) is None
    assert tabulation.get_target_numbers(0, []) == []
    assert tabulation.get_target_numbers(0, [1, 1, 1]) == []

    # test custom cases
    assert tabulation.get_target_numbers(7, [1]) == [1, 1, 1, 1, 1, 1, 1]
    assert tabulation.get_target_numbers(7, [1, 2, 3]) == [1, 3, 3]
    assert tabulation.get_target_numbers(8, [1, 3, 5]) == [3, 5]
    assert tabulation.get_target_numbers(300, [7, 14, 28]) is None


def test_get_subsequences():
    # test base cases
    assert tabulation.get_chunks([]) == [], []
    assert tabulation.get_chunks([0]) == [], [0]
    assert tabulation.get_chunks([10]) == [], [10]
    assert tabulation.get_chunks([-1, 1]) == [], [-1, 1]
    # test custom cases
    assert tabulation.get_chunks([1, 2, 3, 4, 5]) == [1, 2, 4], [3, 5]
    assert tabulation.get_chunks([1, 3, 3, 4, 5]) == [1, 3, 4], [3, 5]
