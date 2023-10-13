from utils.bases.menus import BaseMenu
from datetime import datetime, timedelta, date
from utils import constants


class TournamentView(BaseMenu):
    tournament_menu: dict = {
        "1": "Creation",
        "2": "",
        "3": "",
        "4": "",
        "5": "",
    }

    def tournament_data(self):
        name = self._get_string("Enter the tournament name: ")
        place = self._get_string("Place of the tournament: ")
        start = self.start_date()

        print(name, place, start)

    def start_date(self):
        """
        Generate the date the tournament begins.
        Returns:
            date: start
        """
        start = date.today()
        start_date = start.strftime("%A %d %B %Y")
        print(f"\nThe beginning of the tournament is the {start_date}")

        choice = self.display_menu(constants.CONFIRMATION_MENU)
        while True:
            if choice == "1":
                return start_date

            elif choice == "2":
                new_date = self._get_date("Enter start date (ddmmaaaa): ")
                print(new_date, start)
                # if int(new_date) < start:
                #     print("It is not possible to schedule a date less than today.")
                # else:
                #     new_date = new_date.strftime("%A %d %B %Y")
                # return new_date
            else:
                return self.start_date()

    def display_menu(self, menu_dict):
        self.display_reception()
        self._display_menu(menu_dict=menu_dict)
        return self._response_menu(menu_dict=menu_dict)

    def end_date(self):
        self.display_number_of_day()
        choice = self.select_choice()
        self.number_of_the_day(constants.NUMBER_OF_DAY + 1)

    # Presentation
    def display_reception(self):
        """
        Display a reception message.
        """
        self._space_presentation(" TOURNAMENT RECEPTION ")

    def display_creation(self):
        """
        Display a message for tournament creation.
        """
        self._space_presentation(" TOURNAMENT CREATION ")

    def display_number_of_day(self):
        self._space_presentation(" NUMBER DAYS ")
