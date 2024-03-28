from ..utils.bases.menus import BaseMenu
from ..utils.bases.date import BaseDate

from ..utils.constants import (
    NUMBER_OF_ROUND,
    CONFIRMATION_MENU,
    DEFAULT_VALUE,
)


class TournamentView(BaseMenu, BaseDate):
    tournament_menu: dict = {
        "1": "Create",
        "2": "Read",
        "3": "Delete",
        "4": "Details",
        "5": "Return",
    }

    def tournament_data(self):
        name = self.get_name()
        place = self._get_string("Place of the tournament: ")
        start = self._get_valid_date(
            "Enter start date (ddmmyyyy): ", future_date=True
        )
        start_date = self.convert(start)
        end = self._get_valid_date(
            "Enter end date (ddmmyyyy): ", start_date=start, future_date=False
        )
        end_date = self.convert(end)
        self.display_number_of_rounds()
        nbr_round = self.valid_int_value(DEFAULT_VALUE, f"{NUMBER_OF_ROUND}")
        comment = self._get_string("Enter a comment if needed: ")
        return {
            "name": name,
            "place": place.capitalize(),
            "start_date": start_date,
            "end_date": end_date,
            "nbr_round": int(nbr_round),
            "comment": comment,
        }

    def get_name(self):
        return self._get_string("Enter the tournament name: ").capitalize()

    def display_menu(self, menu_dict):
        self._display_menu(menu_dict=menu_dict)
        return self._response_menu(menu_dict=menu_dict)

    def valid_int_value(self, sentence, value):
        self.display_value_and_sentence(sentence=sentence, value=value)
        self.display_made_your_choice
        while True:
            choice = self.display_menu(CONFIRMATION_MENU)
            if choice == "1":
                return value
            elif choice == "2":
                return self._get_int("Enter new value: ")
            else:
                self._message_error(choice)

    # Presentation
    def display_reception(self):
        self._space_presentation(" TOURNAMENT RECEPTION ")

    def display_creation(self):
        self._space_presentation(" TOURNAMENT CREATION ")

    def display_number_of_day(self):
        self._space_presentation(" NUMBER DAYS ")

    def display_number_of_rounds(self):
        self._star_presentation(" NUMBER ROUNDS ")

    def display_list(self):
        self._space_presentation(" TOURNAMENT LIST ")

    def display_remove(self):
        self._space_presentation(" REMOVE TOURNAMENT ")

    def display_details(self):
        self._space_presentation(" TOURNAMENT DETAILS ")

    def display_tournament_register(self, var):
        print(f"\nTournament {var} is registered.")

    def success_message(self, var):
        print(f"\nTournament {var} removed successfully.")

    def display_tournament(self, var):
        print(var)
