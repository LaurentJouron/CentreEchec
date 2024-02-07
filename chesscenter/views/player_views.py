from datetime import datetime

from chesscenter.utils.bases.menus import BaseMenu
from chesscenter.utils.bases.date import BaseDate


class PlayerView(BaseMenu, BaseDate):
    player_menu: dict = {
        "1": "Create",
        "2": "Read",
        "3": "Delete",
        "4": "Details",
        "5": "Return",
    }
    gender: dict = {"1": "Male", "2": "Female"}

    def generate_code(self, first_name, last_name, birthday):
        initials = first_name[0].upper() + last_name[0].upper()
        day_month = datetime.strptime(birthday, "%d%m%Y").strftime("%d%m")[:4]
        year_last_digit = birthday[-1]
        return initials + day_month + year_last_digit

    def get_data(self):
        first_name = self._get_string("Please enter the player’s first name: ")
        last_name = self._get_string("Enter the last name: ")
        birth = self._get_valid_date("Enter the birth date: ")
        gender = self.get_gender()
        code = self.generate_code(first_name, last_name, birth)
        birth = self.convert(birth)
        rank = self.get_rank()
        return {
            "player_code": code,
            "first_name": first_name.capitalize(),
            "last_name": last_name.capitalize(),
            "birthday": birth,
            "gender": gender,
            "rank": rank,
        }

    def get_rank(self):
        while True:
            try:
                rank = self._get_int("Please input rank: ")
                if rank < 0:
                    raise ValueError
            except ValueError:
                print("You need input positif number!")
            else:
                break
        return rank

    def display_menu(self, menu_dict):
        self._display_menu(menu_dict=menu_dict)
        return self._response_menu(menu_dict=menu_dict)

    def get_player_code(self):
        player_code = self._get_string("Please enter the player code: ")
        return player_code.upper()

    def get_gender(self):
        while True:
            choice = self.display_menu(self.gender)
            if choice in self.gender:
                return self.gender[choice]

    # Presentation
    def display_reception(self):
        self._space_presentation(" PLAYER RECEPTION ")

    def display_creation(self):
        self._space_presentation(" PLAYER CREATION ")

    def display_list(self):
        self._space_presentation(" PLAYERS LIST ")

    def display_remove(self):
        self._space_presentation(" REMOVE PLAYER ")

    def display_details(self):
        self._space_presentation(" PLAYER DETAILS ")

    def enter_information(self):
        self._enter_information()

    def display_player_register(self, var):
        print(f"\nPlayer {var} is registered.")

    def display_player(self, var):
        print(var)

    def success_message(self, var):
        print(f"\nPlayer {var} removed successfully.")
