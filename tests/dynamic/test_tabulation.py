from dynamic import tabulation


def test_get_fibonacci_number():
    assert tabulation.get_fibonacci_number(-10) == 0
    assert tabulation.get_fibonacci_number(0) == 0
    assert tabulation.get_fibonacci_number(1) == 1
    assert tabulation.get_fibonacci_number(3) == 2
    assert tabulation.get_fibonacci_number(10) == 55
    assert tabulation.get_fibonacci_number(50) == 12_586_269_025
    assert tabulation.get_fibonacci_number(100) == 354_224_848_179_261_915_075
