"""
Bartender: conditions workflow demo (never-nester)

"""

MENU = ["juice", "beer"]  # available drinks list


# The function below serves the user's order.
# It takes a drink name as its argument, and checks user's age if needed.
# This one is hideous and complicated...

def bartender(drink_name: str) -> None:
    if drink_name in MENU:
        if drink_name == "beer":
            while True:
                age = input("Not so fast! How old are you?\n>>> ")
                if age.isdigit():
                    age = int(age)
                    break
                print("Please use digits only.")

            if age < 18:
                print("You're not old enough to drink!")
            elif age < 21:
                print("You can drink, but not in US!")
            else:
                print("Take your cold beer!")

        else:
            print("Here is your fresh juice!")
    else:
        print("Sorry, we do not serve this drink...")


# ... so, let's do some enhancements

def serve_an_order(drink_name: str) -> None:
    if drink_name not in MENU:
        print("Sorry, we do not serve this drink...")
        return

    if drink_name == "juice":
        print("Here is your fresh juice!")
        return

    message = check_age(get_age())
    print(message)


def get_age() -> int:
    age = ""
    while not age.isdigit():
        age = input("Not so fast! How old are you?\n>>> ")

    return int(age)


def check_age(age: int) -> str:
    if age < 18:
        return "You're not old enough to drink!"

    if age < 21:
        return "You can drink, but not in US"

    return "Here is your cold beer!"


if __name__ == "__main__":
    order = input("What do you like to drink: %s\n>>> " % " or ".join(MENU))

    bartender(order)
    serve_an_order(order)
