import re
from chesscenter.utils.constants import SIZE_LINE


def _get_string(var):
    """
    Collect a string input from the user.

    Args:
        prompt (str): The input prompt.
        validator (function, optional): A validation function.
        Defaults to None.

    Returns:
        str: The user's input.
    """
    pattern = r"^[a-zA-Z -àçéëêèïîôûù]+$"
    return bool(re.match(pattern, var))


def _get_int(var):
    """
    Collect an integer input from the user.

    Args:
        prompt (str): The input prompt.
        validator (function, optional): A validation function.
        Defaults to None.

    Returns:
        int: The user's input as an integer.
    """
    pattern = r"^\d+$"
    return bool(re.match(pattern, var))


class BaseView:
    string_validator = _get_string
    integer_validator = _get_int

    def _get_string(self, prompt, validator=None):
        """
        Collect a string input from the user.

        Args:
            prompt (str): The input prompt.
            validator (function, optional): A validation function.
            Defaults to None.

        Returns:
            str: The user's input.
        """
        validator = validator or type(self).string_validator
        while True:
            answer = input(prompt).strip()
            if validator(answer):
                return answer

    def _get_int(self, prompt, validator=None):
        """
        Collect an integer input from the user.

        Args:
            prompt (str): The input prompt.
            validator (function, optional): A validation function.
            Defaults to None.

        Returns:
            int: The user's input as an integer.
        """
        validator = validator or type(self).integer_validator
        while True:
            answer = input(prompt).strip()
            if validator(answer):
                return int(answer)

    def _select_number(self):
        """
        Collect a number input from the user.

        Returns:
            str: The user's input as a string.
        """
        while True:
            try:
                return input("Select the menu number: ")
            except ValueError as e:
                self._message_error(e)

    def _space_presentation(self, prompt):
        """
        Display a presentation message with spaces.

        Args:
            prompt (str): The presentation message.

        Returns:
            None
        """
        print(f"\n{prompt.center(SIZE_LINE, ' ')}".upper())

    def _star_presentation(self, prompt):
        """
        Display a presentation message with stars.

        Args:
            prompt (str): The presentation message.

        Returns:
            None
        """
        print(f"\n{prompt.center(SIZE_LINE, '*')}")

    def _message_error(self, var=""):
        """
        Display a value error message.

        Args:
            var (str, optional): The variable causing the error.
            Defaults to "".

        Returns:
            None
        """
        if var != "":
            print(f"\n{var} is value error.")
        else:
            print("Value error.")

    def _message_success(self):
        """
        Display a success message.

        Returns:
            None
        """
        print("Successfully.")

    def _enter_information(self):
        return self._star_presentation(" Enter information ")

    def display_value_and_sentence(self, sentence, value):
        print(f"\n{sentence}: {value}")

    def display_made_your_choice(self):
        print(self._space_presentation(" MADE YOUR CHOICE "))
