from ..views.match_views import MatchView
from ..models.match_models import Match
from ..controllers.tournament_controllers import TournamentMatch as TM
from ..controllers import home_controllers as home
from ..utils.bases.controllers import BaseController


view = MatchView()


class MatchController(BaseController):
    def __init__(self):
        self.model = Match

    def run(self):
        view.display_reception()
        while True:
            choice = view.display_menu(view.match_menu)
            if choice == "1":
                return MatchFirstMatch()

            elif choice == "5":
                return home.HomeController()


class MatchFirstMatch(MatchController):
    def __init__(self):
        self.tournament = TM()

    def run(self):
        matches = self.tournament.get_first_round()
        score0 = 0
        score1 = 0
        for match in matches:
            player0 = match["player_code"][0]
            player1 = match["player_code"][1]
            print(player0, player1, score0, score1)
