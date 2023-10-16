from utils.bases.menus import BaseMenu
from utils.bases.date import BaseDate


class TournamentView(BaseMenu, BaseDate):
    tournament_menu: dict = {
        "1": "Creation",
        "2": "",
        "3": "",
        "4": "",
        "5": "",
    }

    def get_tournament_data(self):
        name = self._get_string("Enter the tournament name: ")
        place = self._get_string("Place of the tournament: ")
        start = self._get_valid_date("Enter start date: ", future_date=True)
        start_date = self.convert(start)
        nbr_tour = self._get_string("Number of tour: ")
        end = self._get_valid_date(
            "Enter end date: ", start_date=start, future_date=False
        )
        end_date = self.convert(end)
        current_round = self._get_string("current_round: ")
        comment = self._get_string("Enter a comment if needed: ")
        return {
            "name": name.capitalize(),
            "place": place.capitalize(),
            "start_date": start_date,
            "nbr_tour": nbr_tour,
            "end_date": end_date,
            "current_round": current_round,
            "comment": comment,
        }

    def display_menu(self, menu_dict):
        self.display_reception()
        self._display_menu(menu_dict=menu_dict)
        return self._response_menu(menu_dict=menu_dict)

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
