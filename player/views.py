from datetime import datetime

from utils.bases import BaseView, MenuBaseView
from utils.constants import PLAYER_MENU


class PlayerView(MenuBaseView, BaseView):
    def __init__(self):
        self.player_menu = PLAYER_MENU

    def generate_player_code(self, first_name, last_name, birthday):
        initials = first_name[0].upper() + last_name[0].upper()
        day_month = datetime.strptime(birthday, "%d%m%Y").strftime("%d%m")[0:4]
        year_last_digit = birthday[-1]
        player_code = initials + day_month + year_last_digit
        return player_code

    def get_player_data(self):
        first_name = self._get_string("Please enter the player’s first name: ")
        last_name = self._get_string("Enter the last name: ")
        birthday = self._get_date("Enter date of birth (ddmmaaaa): ")
        player_code = self.generate_player_code(first_name, last_name, birthday)
        birthday = datetime.strptime(birthday, "%d%m%Y").strftime("%A %d %B %Y")
        return {
            "player_code": player_code,
            "first_name": first_name.capitalize(),
            "last_name": last_name.capitalize(),
            "birthday": birthday,
        }

    def display_menu(self, menu_dict):
        self.display_reception()
        self._display_menu(menu_dict=menu_dict)
        return self._response_menu(menu_dict=menu_dict)

    def get_player_code(self):
        player_code = self._get_string("Please enter the player code: ")
        return player_code.upper()

    def display_reception(self):
        return self._space_presentation(" PLAYER RECEPTION ")

    def display_creation(self):
        return self._space_presentation(" PLAYER CREATION ")

    def display_list_all(self):
        return self._space_presentation(" ALL PLAYERS IN LIST ")

    def display_remove(self):
        return self._space_presentation(" REMOVE PLAYER ")

    def display_get_one(self):
        return self._space_presentation(" GET ONE PLAYER ")

    def confirm_register(var):
        print(f"\nPlayer {var} is register. ")

    def message_error(self, var):
        return self._message_error(var)

    def message_success(self):
        return self._message_success()
