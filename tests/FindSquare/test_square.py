from square import calculate_square
def test_square_calculation():
    from square import calculate_square

    # Test with a positive number
    assert calculate_square(4) == 16

    # Test with a negative number
    assert calculate_square(-3) == 9

    # Test with a decimal number
    assert calculate_square(2.5) == 6.25


