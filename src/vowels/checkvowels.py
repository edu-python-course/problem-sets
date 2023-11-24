def is_character_vowel(char):
    vowels = "aeiouAEIOU"
    return char in vowels

def main():
    user_input = input("Enter a character: ")

    if len(user_input) == 1 and user_input.isalpha():
        if is_character_vowel(user_input):
            print(f"The character '{user_input}' is a vowel.")
        else:
            print(f"The character '{user_input}' is not a vowel.")
    else:
        print("Please enter a single alphabetic character.")

if __name__ == "__main__":
    main()
