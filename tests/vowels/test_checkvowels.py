
from checkvowels import is_character_vowel

def test_is_character_vowel():
    assert is_character_vowel('a') == True
    assert is_character_vowel('b') == False
    assert is_character_vowel('A') == True
    assert is_character_vowel('1') == False
    assert is_character_vowel('@') == False


