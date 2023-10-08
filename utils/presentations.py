def reception(var):
    reception = f" {var} "
    print(f"\n{reception.center(106, ' ')}")


def enter_information():
    information_decoration = " Enter information "
    print(f"{information_decoration.center(106, '*')}")


def input_error(var):
    print(f"Invalid input: {var}. Please try again.")


def register(var):
    print(f"\n{var} is register. ")


def select_number():
    return input("Select the menu number : ")


def value_error():
    print("Value error.")


def exiting_program():
    information_decoration = " Exiting the program "
    print(f"{information_decoration.center(106, '*')}")


def success_message(var):
    print(var)


def error_message(var):
    print(var)


def display_player(var):
    print(var)
