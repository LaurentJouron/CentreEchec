import re


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
        validator = validator or self.string_validator
        while True:
            answer = input(prompt).strip()
            if validator(answer):
                return answer

    def _get_int(self, prompt, validator=None):
        validator = validator or self.integer_validator
        while True:
            answer = input(prompt).strip()
            if validator(answer):
                return int(answer)

    def _get_date(self, prompt, validator=None):
        validator = validator or self.date_validator
        while True:
            answer = input(prompt).strip()
            if validator(answer):
                return answer


class BaseController:
    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def action(self):
        raise NotImplementedError

    def run(self):
        return self.action()
