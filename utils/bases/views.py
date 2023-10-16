import re
from utils.constants import SIZE_LINE


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
    if re.match(pattern, var):
        return True
    else:
        return False


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
    if re.match(pattern, var):
        return True
    else:
        return False


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
                answer = input("Select the menu number: ")
                return answer
            except ValueError:
                self._message_error(answer)

    def _space_presentation(self, prompt):
        """
        Display a presentation message with spaces.

        Args:
            prompt (str): The presentation message.

        Returns:
            None
        """
        print(f"\n{prompt.center(SIZE_LINE, ' ')}")

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
