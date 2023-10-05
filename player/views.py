from datetime import datetime

from utils import presentations
from utils.base import BaseView


class PlayerView(BaseView):
    def generate_player_code(self, first_name, last_name, birthday):
        initials = first_name[0].upper() + last_name[0].upper()
        date_parts = datetime.strptime(birthday, "%d%m%Y").strftime("%d%m%Y")[0:5]
        year_last_digit = date_parts[-1]
        player_code = initials + date_parts + year_last_digit
        return player_code

    def get_player_data(self):
        first_name = self._get_string("Please enter the player’s first name: ")
        last_name = self._get_string("Enter the last name: ")
        birthday = self._get_date(
            "Enter date of birth (ddmmaaaa): ")
        player_code = self.generate_player_code(
            first_name,
            last_name,
            birthday
            )
        return {
            "player_code": player_code,
            "first_name": first_name,
            "last_name": last_name,
            "birthday": birthday,
        }

    def get_birthday(self) -> str:
        validator = self.validate_birthday
        while True:
            birthday = input("Enter date of birth (ddmmaaaa): ")
            if validator(birthday):
                formatted_birthday = datetime.strptime(birthday, "%d%m%Y").strftime(
                    "%A %d %B %Y"
                )
                return formatted_birthday
            else:
                presentations.input_error(birthday)
