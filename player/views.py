from datetime import datetime

from utils.bases.menus import BaseMenu
from utils.bases.date import BaseDate


class PlayerView(BaseMenu, BaseDate):
    player_menu: dict = {
        "1": "Add",
        "2": "Show all",
        "3": "Remove",
        "4": "Details",
        "5": "Quit",
    }
    gender: dict = {"1": "Male", "2": "Female"}

    def generate_player_code(self, first_name, last_name, birthday):
        """
        Generate a player code based on first name, last name, and birthday.

        Args:
            first_name (str): The player's first name.
            last_name (str): The player's last name.
            birthday (str): The player's date of birth in "ddmmaaaa" format.

        Returns:
            str: The generated player code.
        """
        initials = first_name[0].upper() + last_name[0].upper()
        day_month = datetime.strptime(birthday, "%d%m%Y").strftime("%d%m")[0:4]
        year_last_digit = birthday[-1]
        player_code = initials + day_month + year_last_digit
        return player_code

    def get_player_data(self):
        """
        Collect player data from user input.

        Returns:
            dict: Player data including player code, first name, last name,
            and formatted birthday.
        """
        first_name = self._get_string("Please enter the player’s first name: ")
        last_name = self._get_string("Enter the last name: ")
        birth = self._get_valid_date("Enter the birth date: ")
        gender = self.get_gender()
        player_code = self.generate_player_code(first_name, last_name, birth)
        birth = self.convert(birth)
        return {
            "player_code": player_code,
            "first_name": first_name.capitalize(),
            "last_name": last_name.capitalize(),
            "birthday": birth,
            "gender": gender,
        }

    def display_menu(self, menu_dict):
        """
        Display the player menu and collect user's choice.

        Args:
            menu_dict (dict): A dictionary of menu options.

        Returns:
            str: The user's choice from the menu.
        """
        self._display_menu(menu_dict=menu_dict)
        return self._response_menu(menu_dict=menu_dict)

    def get_player_code(self):
        """
        Get the player code from user input.

        Returns:
            str: The entered player code in uppercase.
        """
        player_code = self._get_string("Please enter the player code: ")
        return player_code.upper()

    def confirm_register(self, var):
        """
        Display a confirmation message for player registration.

        Args:
            var (str): The player's name.
        """
        print(f"\nPlayer {var} is registered.")

    def get_gender(self):
        while True:
            choice = self.display_menu(self.gender)
            if choice in self.gender:
                return self.gender[choice]

    # Presentation
    def display_reception(self):
        """
        Display a reception message.
        """
        self._space_presentation(" PLAYER RECEPTION ")

    def display_creation(self):
        """
        Display a message for player creation.
        """
        self._space_presentation(" PLAYER CREATION ")

    def display_list_all(self):
        """
        Display a message for listing all players.
        """
        self._space_presentation(" ALL PLAYERS ")

    def display_remove(self):
        """
        Display a message for removing a player.
        """
        self._space_presentation(" REMOVE PLAYER ")

    def display_details(self):
        """
        Display a message for getting details of a player.
        """
        self._space_presentation(" PLAYER DETAILS ")

    def enter_information(self):
        self._enter_information()

    def display_player_register(self, var):
        print(f"\n{var} is register. ")

    def display_player(self, var):
        print(var)

    def success_message(self, var):
        print(f"\nPlayer {var} removed successfully.")
