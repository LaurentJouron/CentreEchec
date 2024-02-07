from chesscenter.views.home_views import HomeView
from chesscenter.utils.constants import CONFIRMATION_MENU
from chesscenter.utils.bases.controllers import BaseController
from chesscenter.controllers.player_controllers import PlayerController
from chesscenter.controllers.tournament_controllers import TournamentController

view = HomeView()


class HomeController(BaseController):
    def run(self):
        view.welcome_game()
        view.game_instruction()
        while True:
            choice = view.display_menu(view.home_menu)
            if choice == "1":
                return PlayerController()

            elif choice == "2":
                return TournamentController()

            elif choice == "3":
                print("tour menu")

            elif choice == "4":
                print("match menu")

            elif choice == "5":
                return ExitController()


class ExitController(BaseController):
    def run(self):
        view.exit_game()
        choice = view.display_menu(CONFIRMATION_MENU)
        return None if choice == "1" else HomeController()
