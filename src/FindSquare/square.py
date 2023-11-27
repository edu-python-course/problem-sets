def calculate_square(number):
    """
    Calculate the square value of a given number.

    Parameters:
    - number (float): The input number for which the square value is calculated.

    Returns:
    - float: The square value of the input number.
    """
    return number ** 2

def main():
    """
    The main function of the program. It takes user input, calculates the square value,
    and prints the result.

    Usage:
    - Run this script to input a number and get its square value.
    """
    # Ask the user for a number
    user_input = input("Enter a number: ")

    try:
        # To cast the input to a numeric type
        number = float(user_input)

        # Calculate the square value
        square_value = calculate_square(number)

        # Print out the result
        print(f"The square value of {number} is: {square_value}")

    except ValueError:
        # Handle the case where the input cannot be cast to a numeric type
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
