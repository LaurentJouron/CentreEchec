import re
from utils.presentations import select_number


def validate_charact(var):
    pattern = r"^[a-zA-Z -àçéëêèïîôûù]+$"
    if re.match(pattern, var):
        return True
    else:
        return False


def validate_integer(var):
    pattern = r"^\d+$"
    if re.match(pattern, var):
        return True
    else:
        return False


def validate_date(var):
    pattern = r"^\d{8}$"
    if re.match(pattern, var):
        return True
    else:
        return False


class BaseView:
    string_validator = validate_charact
    integer_validator = validate_integer
    date_validator = validate_date

    def _get_string(self, prompt, validator=None):
        validator = validator or type(self).string_validator
        while True:
            answer = input(prompt).strip()
            if validator(answer):
                return answer

    def _get_int(self, prompt, validator=None):
        validator = validator or type(self).integer_validator
        while True:
            answer = input(prompt).strip()
            if validator(answer):
                return int(answer)

    def _get_date(self, prompt, validator=None):
        validator = validator or type(self).date_validator
        while True:
            answer = input(prompt).strip()
            if validator(answer):
                return answer

    def _space_presentation(self, prompt):
        print(f"\n{prompt.center(106, ' ')}")

    def _star_presentation(self, prompt):
        print(f"\n{prompt.center(106, '*')}")

    def _message_error(self, var=""):
        if var != "":
            print(f"\n{var} is value error.")
        else:
            print("Value error.")

    def _message_success(self):
        print("Successfully.")


class MenuBaseView(BaseView):
    def _display_menu(self, menu_dict):
        menu_options = " | ".join(
            [f" {keys}. {value} " for keys, value in menu_dict.items()]
        )
        return self._star_presentation(menu_options)

    def _response_menu(self, menu_dict):
        choice = select_number()
        if choice in menu_dict:
            return choice
        return self._message_error(choice)


class BaseController:
    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def action(self):
        raise NotImplemented

    def run(self):
        return self.action()
