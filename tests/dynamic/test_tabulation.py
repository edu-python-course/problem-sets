from dynamic import tabulation


def test_get_fibonacci_number():
    assert tabulation.get_fibonacci_number(-10) == 0
    assert tabulation.get_fibonacci_number(0) == 0
    assert tabulation.get_fibonacci_number(1) == 1
    assert tabulation.get_fibonacci_number(3) == 2
    assert tabulation.get_fibonacci_number(10) == 55
    assert tabulation.get_fibonacci_number(50) == 12_586_269_025
    assert tabulation.get_fibonacci_number(100) == 354_224_848_179_261_915_075


def test_get_grid_travels():
    assert tabulation.get_grid_travels(0, 0) == 0
    assert tabulation.get_grid_travels(0, 1) == 0
    assert tabulation.get_grid_travels(1, 0) == 0
    assert tabulation.get_grid_travels(1, 1) == 1
    assert tabulation.get_grid_travels(2, 3) == 3
    assert tabulation.get_grid_travels(3, 2) == 3
    assert tabulation.get_grid_travels(3, 3) == 6
    assert tabulation.get_grid_travels(18, 18) == 2_333_606_220
