import calc


def test_get_factorial():
    assert calc.get_factorial(0) == 1
    assert calc.get_factorial(5) == 120


def test_get_fibonacci_number():
    # test base cases
    assert calc.get_fibonacci_number(-10) == 0
    assert calc.get_fibonacci_number(0) == 0
    assert calc.get_fibonacci_number(1) == 1
    # test custom cases
    assert calc.get_fibonacci_number(2) == 1
    assert calc.get_fibonacci_number(3) == 2
    assert calc.get_fibonacci_number(10) == 55


def test_fibonacci_number_nr():
    # test base cases
    assert calc.get_fibonacci_number_nr(-10) == 0
    assert calc.get_fibonacci_number_nr(0) == 0
    assert calc.get_fibonacci_number_nr(1) == 1
    assert calc.get_fibonacci_number_nr(2) == 1
    # test custom cases
    assert calc.get_fibonacci_number_nr(3) == 2
    assert calc.get_fibonacci_number_nr(10) == 55
    assert calc.get_fibonacci_number_nr(50) == 12_586_269_025
    assert calc.get_fibonacci_number_nr(100) == 354_224_848_179_261_915_075


def test_sum_of_strings():
    assert calc.get_sum_of_strings("123", "456") == "579"
    assert calc.get_sum_of_strings("123", "789") == "912"
    assert calc.get_sum_of_strings("99", "1") == "100"


def test_sum_of_strings_big_integers():
    x, y, test_value = "490053634", "20846201", "510899835"
    assert calc.get_sum_of_strings(x, y) == test_value

    x, y, test_value = "616526149", "364644330", "981170479"
    assert calc.get_sum_of_strings(x, y) == test_value


def test_sum_of_strings_leading_zeros():
    assert calc.get_sum_of_strings("009", "000001") == "10"
    assert calc.get_sum_of_strings("020", "000000") == "20"
    assert calc.get_sum_of_strings("000", "000000") == "0"


def test_sum_of_strings_empty():
    assert calc.get_sum_of_strings("123", "") == "123"
    assert calc.get_sum_of_strings("", "456") == "456"
    assert calc.get_sum_of_strings("", "") == "0"
