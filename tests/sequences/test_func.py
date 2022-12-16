import sequences


def test_palindrome_simple():
    assert sequences.is_palindrome("palindrome") is False
    assert sequences.is_palindrome("tattarrattat") is True
    assert sequences.is_palindrome("malayalam") is True


def test_palindrome_names():
    assert sequences.is_palindrome("Serhii") is False
    assert sequences.is_palindrome("Hannah") is True


def test_palindrome_numbers():
    assert sequences.is_palindrome("12345") is False
    assert sequences.is_palindrome("12321") is True


def test_palindrome_dates():
    assert sequences.is_palindrome("24/02/2022") is False
    assert sequences.is_palindrome("1/11/2111") is True


def test_palindrome_phrase():
    assert sequences.is_palindrome("This is some sentence") is False
    assert sequences.is_palindrome("Mr. Owl ate my metal worm") is True
    assert sequences.is_palindrome("Satire: Veritas") is True
    assert sequences.is_palindrome("Dammit I'm Mad") is True


def test_get_longest_palindrome_odd():
    # noinspection SpellCheckingInspection
    assert sequences.get_longest_palindrome("ABBABBC") == "BBABB"


def test_get_longest_palindrome_even():
    assert sequences.get_longest_palindrome("abba") == "abba"


def test_get_longest_palindrome_one_char():
    assert sequences.get_longest_palindrome("abcdefg") == "g"


def test_get_longest_palindrome_empty():
    assert sequences.get_longest_palindrome("") == ""


def test_parentheses_validator():
    assert sequences.are_parentheses_balanced("<[{(()[{}<>{}]())}]>") is True
    assert sequences.are_parentheses_balanced("") is True
    assert sequences.are_parentheses_balanced("[<}{>]") is False
    assert sequences.are_parentheses_balanced("[]]") is False
    assert sequences.are_parentheses_balanced("(()") is False
    assert sequences.are_parentheses_balanced("(some <text>)") is True


def test_fibonacci_number_getter():
    assert sequences.get_fibonacci_number(-10) == 0  # special test case
    assert sequences.get_fibonacci_number(0) == 0
    assert sequences.get_fibonacci_number(1) == 1
    assert sequences.get_fibonacci_number(2) == 1
    assert sequences.get_fibonacci_number(3) == 2
    assert sequences.get_fibonacci_number(9) == 34


# noinspection SpellCheckingInspection
def test_get_longest_uniq_sequence_length():
    assert sequences.get_longest_uniq_length("abcdefg") == 7
    assert sequences.get_longest_uniq_length("abcacba") == 3
    assert sequences.get_longest_uniq_length("hwccjayhiszbmomlqkem") == 11


def test_sum_of_two_digits():
    assert sequences.get_strings_sum("123", "456") == "579"
    assert sequences.get_strings_sum("123", "789") == "912"
    assert sequences.get_strings_sum("99", "1") == "100"


def test_sum_of_two_digits_big():
    x, y, test_value = "490053634", "20846201", "510899835"
    assert sequences.get_strings_sum(x, y) == test_value

    x, y, test_value = "616526149", "364644330", "981170479"
    assert sequences.get_strings_sum(x, y) == test_value
