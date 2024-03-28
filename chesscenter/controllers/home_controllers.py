from ..views.home_views import HomeView
from ..utils.constants import CONFIRMATION_MENU
from ..utils.bases.controllers import BaseController
from ..controllers.player_controllers import PlayerController
from ..controllers.tournament_controllers import TournamentController
from ..controllers.match_controllers import MatchController

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
                return MatchController()

            elif choice == "4":
                print("round menu")

            elif choice == "5":
                return ExitController()


class ExitController(BaseController):
    def run(self):
        view.exit_game()
        choice = view.display_menu(CONFIRMATION_MENU)
        return None if choice == "1" else HomeController()
