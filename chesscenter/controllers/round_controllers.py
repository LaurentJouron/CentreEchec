from ..views.round_views import RoundView
from ..models.round_models import Round
from ..controllers import home_controllers as home
from ..controllers.tournament_controllers import TournamentRound
from ..utils.bases.controllers import BaseController

view = RoundView()


class RoundController(BaseController):
    def __init__(self):
        self.model = Round

    def run(self):
        view.display_reception()
        while True:
            choice = view.display_menu(view.round_menu)
            if choice == "1":
                return RoundFirstRoundController()
            elif choice == "5":
                return home.HomeController()


class RoundFirstRoundController(RoundController):
    def __init__(self):
        self.model = Round
        self.tournament = TournamentRound()

    def run(self):
        print(self.tournament.get_first_round())
