from datetime import datetime

from utils.bases import BaseView


class PlayerView(BaseView):
    def generate_player_code(self, first_name, last_name, birthday):
        initials = first_name[0].upper() + last_name[0].upper()
        day_month = datetime.strptime(birthday, "%d%m%Y").strftime("%d%m")[0:4]
        year_last_digit = birthday[-1]
        player_code = initials + day_month + year_last_digit
        return player_code

    def get_player_data(self):
        first_name = self.get_first_name()
        last_name = self.get_last_name()
        birthday = self._get_date("Enter date of birth (ddmmaaaa): ")
        player_code = self.generate_player_code(
            first_name,
            last_name,
            birthday
            )
        birthday = datetime.strptime(birthday, "%d%m%Y").strftime("%A %d %B %Y")
        return {
            "player_code": player_code,
            "first_name": first_name,
            "last_name": last_name,
            "birthday": birthday,
        }

    def get_first_name(self) -> str:
        first_name = self._get_string("Please enter the player’s first name: ")
        return first_name.capitalize()

    def get_last_name(self) -> str:
        last_name = self._get_string("Enter the last name: ")
        return last_name.capitalize()

    def get_player_code(self):
        player_code = self._get_string("Please enter the player code: ")
        return player_code.upper()
