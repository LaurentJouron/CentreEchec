from ..views.match_views import MatchView
from ..models.match_models import Match
from ..controllers.tournament_controllers import TournamentController
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
        self.tournament = TournamentController()
        self.model = Match

    def run(self):
        matches = self.tournament.get_matches()
        score1 = 0
        score2 = 0
        for match in matches:
            player1 = match[0]
            player2 = match[1]
            print(player1, player2, score1, score2)
