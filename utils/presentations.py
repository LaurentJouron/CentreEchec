def welcome():
    welcome_application = " Welcome to the << CHESS-CENTER >> application "
    print(f"\n{welcome_application.center(106, ' ')}")


def reception(var):
    reception = f" {var} "
    print(f"\n {reception.center(106, ' ')}")


def instruction():
    instructions = " Please follow the instructions below "
    print(f"\n{instructions.center(106, ' ')}")


def enter_information():
    information_decoration = " Enter information "
    print(f"{information_decoration.center(106, '*')}")


def input_error(var):
    print(f"Invalid input: {var}. Please try again.")


def register(var):
    print(f" {var} is register. ")
