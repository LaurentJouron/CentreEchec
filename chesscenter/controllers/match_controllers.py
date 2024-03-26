from chesscenter.views.match_views import MatchView
from chesscenter.models.match_models import Match
from chesscenter.controllers import home_controllers as home
from chesscenter.utils.bases.controllers import BaseController

view = MatchView()


class MatchController(BaseController):
    def __init__(self):
        self.model = Match

    def run(self):
        view.display_reception()
        while True:
            choice = view.display_menu(view.match_menu)
            if choice == "1":
                return ...

            elif choice == "5":
                return home.HomeController()

    def get_match_in_matches(self, matches):
        score0 = 0
        score1 = 0
        for match in matches:
            player0 = match["player_code"][0]
            player1 = match["player_code"][1]
            print(player0, player1, score0, score1)
