import re
from utils.presentations import select_number


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


def _get_date(var):
    """
    Collect a date input from the user.

    Args:
        prompt (str): The input prompt.
        validator (function, optional): A validation function.
        Defaults to None.

    Returns:
        str: The user's input as a date.
    """
    pattern = r"^\d{8}$"
    if re.match(pattern, var):
        return True
    else:
        return False


class BaseView:
    string_validator = _get_string
    integer_validator = _get_int
    date_validator = _get_date

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

    def _get_date(self, prompt, validator=None):
        """
        Collect a date input from the user.

        Args:
            prompt (str): The input prompt.
            validator (function, optional): A validation function.
            Defaults to None.

        Returns:
            str: The user's input as a date.
        """
        validator = validator or type(self).date_validator
        while True:
            answer = input(prompt).strip()
            if validator(answer):
                return answer

    def _space_presentation(self, prompt):
        """
        Display a presentation message with spaces.

        Args:
            prompt (str): The presentation message.

        Returns:
            None
        """
        print(f"\n{prompt.center(106, ' ')}")

    def _star_presentation(self, prompt):
        """
        Display a presentation message with stars.

        Args:
            prompt (str): The presentation message.

        Returns:
            None
        """
        print(f"\n{prompt.center(106, '*')}")

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


class MenuBaseView(BaseView):
    def _display_menu(self, menu_dict):
        """
        Display a menu and return the user's choice.

        Args:
            menu_dict (dict): A dictionary of menu options.

        Returns:
            None
        """
        menu_options = " | ".join(
            [f" {keys}. {value} " for keys, value in menu_dict.items()]
        )
        return self._star_presentation(menu_options)

    def _response_menu(self, menu_dict):
        """
        Collect and validate the user's choice from the menu.

        Args:
            menu_dict (dict): A dictionary of menu options.

        Returns:
            str: The user's choice.
        """
        choice = select_number()
        if choice in menu_dict:
            return choice
        return self._message_error(choice)


class BaseController:
    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def action(self):
        """
        Define the action for the controller.

        Raises:
            NotImplementedError: This method should be implemented in
            subclasses.

        Returns:
            None
        """
        raise NotImplementedError

    def run(self):
        """
        Run the controller's action.

        Returns:
            None
        """
        return self.action()
