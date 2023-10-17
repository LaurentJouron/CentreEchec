from utils.bases.menus import BaseMenu
from utils.bases.date import BaseDate

from utils.constants import NUMBER_OF_ROUND, CONFIRMATION_MENU


class TournamentView(BaseMenu, BaseDate):
    tournament_menu: dict = {
        "1": "Creation",
        "2": "",
        "3": "",
        "4": "",
        "5": "",
    }

    def get_tournament_data(self):
        # name = self._get_string("Enter the tournament name: ")
        # place = self._get_string("Place of the tournament: ")
        # start = self._get_valid_date("Enter start date: ", future_date=True)
        # start_date = self.convert(start)
        self.display_number_of_rounds()
        nbr_tour = self.valid_int_value("Defaut number of round: ", NUMBER_OF_ROUND)
        print(nbr_tour)
        # end = self._get_valid_date(
        #     "Enter end date: ", start_date=start, future_date=False
        # )
        # end_date = self.convert(end)
        # current_round = self._get_string("current_round: ")
        # comment = self._get_string("Enter a comment if needed: ")
        # return {
        #     "name": name.capitalize(),
        #     "place": place.capitalize(),
        #     "start_date": start_date,
        #     "nbr_tour": nbr_tour,
        #     "end_date": end_date,
        #     "current_round": current_round,
        #     "comment": comment,
        # }

    def display_menu(self, menu_dict):
        self._display_menu(menu_dict=menu_dict)
        return self._response_menu(menu_dict=menu_dict)

    def valid_int_value(self, sentence, value):
        self.display_value_and_sentence(sentence=sentence, value=value)
        self.display_made_your_choice
        print(f"Confirm {value} select 1 | Change select 2")
        choice = self.display_menu(CONFIRMATION_MENU)
        while True:
            if choice == "1":
                continue
            elif choice == "2":
                answer = self._get_string("Enter new value: ")
                return answer
            else:
                self._message_error(choice)

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

    def display_number_of_rounds(self):
        self._star_presentation(" NUMBER ROUNDS ")
