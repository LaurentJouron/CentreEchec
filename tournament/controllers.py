from utils.bases.controllers import BaseController
from chesscenter import controllers as home

from .views import TournamentView
from .models import Tournament

view = TournamentView()


class TournamentController(BaseController):
    def run(self):
        while True:
            choice = view.display_menu(view.tournament_menu)
            if choice == "1":
                return TournamentCreationController()

            elif choice == "2":
                return ...

            elif choice == "3":
                return ...

            elif choice == "4":
                return ...

            elif choice == "5":
                return home.HomeController()


class TournamentCreationController:
    def __init__(self) -> None:
        self.model = Tournament

    def run(self):
        view.display_creation()
        get_tournament_data = view.get_tournament_data()
        tournament = self.model(**get_tournament_data)
        tournament.save()
        return TournamentController()
