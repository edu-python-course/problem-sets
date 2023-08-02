import sequences


def test_palindrome_simple():
    assert sequences.is_palindrome("palindrome") is False
    assert sequences.is_palindrome("tattarrattat") is True
    assert sequences.is_palindrome("malayalam") is True


def test_palindrome_names():
    assert sequences.is_palindrome("Serhii") is False
    assert sequences.is_palindrome("Hannah") is True


def test_palindrome_numbers():
    assert sequences.is_palindrome(12345) is False
    assert sequences.is_palindrome(12321) is True


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


def test_get_palindrome_primes():
    test = [2, 3, 5, 7, 11, 101, 131, 151, 181, 191, 313, 353, 373, 383, 727]
    assert sequences.get_palindrome_primes(730) == test


def test_get_palindrome_squares():
    test = [0, 1, 4, 9, 121, 484, 676, 10201, 12321, 14641, 40804, 44944, 69696]
    assert sequences.get_palindrome_squares(300) == test


def test_parentheses_validator():
    assert sequences.are_parentheses_balanced("<[{(()[{}<>{}]())}]>") is True
    assert sequences.are_parentheses_balanced("") is True
    assert sequences.are_parentheses_balanced("[<}{>]") is False
    assert sequences.are_parentheses_balanced("[]]") is False
    assert sequences.are_parentheses_balanced("(()") is False
    assert sequences.are_parentheses_balanced("(some <text>)") is True


# noinspection SpellCheckingInspection
def test_get_longest_uniq_sequence_length():
    assert sequences.get_longest_uniq_length("abcdefg") == 7
    assert sequences.get_longest_uniq_length("abcacba") == 3
    assert sequences.get_longest_uniq_length("hwccjayhiszbmomlqkem") == 11


def test_add_space():
    assert sequences.add_spaces("") == ""
    assert sequences.add_spaces("test_test") == "test_test"
    assert sequences.add_spaces("JohnDoe") == "John Doe"
    assert sequences.add_spaces("John Doe") == "John Doe"
