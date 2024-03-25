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
