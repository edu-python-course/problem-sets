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


def test_parentheses_validator():
    assert sequences.are_parentheses_balanced("<[{(()[{}<>{}]())}]>") is True
    assert sequences.are_parentheses_balanced("") is True
    assert sequences.are_parentheses_balanced("[<}{>]") is False
    assert sequences.are_parentheses_balanced("[]]") is False
    assert sequences.are_parentheses_balanced("(()") is False
    assert sequences.are_parentheses_balanced("(some <text>)") is True
