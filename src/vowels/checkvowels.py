def is_character_vowel(char):
    """
    Check if a given character is a vowel.

    Parameters:
    - char (str): The character to be checked.

    Returns:
    - bool: True if the character is a vowel, False otherwise.
    """
    vowels = "aeiouAEIOU"
    return char in vowels

def main():
    user_input = input("Enter a character: ")
    """
    Main function to get user input and determine if the entered character is a vowel.
    """

    if len(user_input) == 1 and user_input.isalpha():
        if is_character_vowel(user_input):
            print(f"The character '{user_input}' is a vowel.")
        else:
            print(f"The character '{user_input}' is not a vowel.")
    else:
        print("Please enter a single alphabetic character.")

if __name__ == "__main__":
    main()
