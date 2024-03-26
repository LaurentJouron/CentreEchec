from chesscenter.views.round_views import RoundView
from chesscenter.models.round_models import Round
from chesscenter.controllers import home_controllers as home
from chesscenter.utils.bases.controllers import BaseController
from chesscenter.utils.constants import NUMBER_OF_PLAYERS
import random

view = RoundView()


class RoundController(BaseController):
    def __init__(self):
        self.model = Round

    def run(self):
        view.display_reception()
        while True:
            choice = view.display_menu(view.round_menu)
            if choice == "1":
                return ...

            elif choice == "5":
                return home.HomeController()


class RoundFirstController(RoundController):
    def __init__(self) -> None:
        self.model = Round

    def run(self, players):
        round_data = self.build_first_match(players=players)
        round_data = self.model(**round_data)
        round_data.save()

    def build_first_match(self, players):
        selected_players = random.sample(players, NUMBER_OF_PLAYERS)
        return [
            (selected_players[i], selected_players[i + 1])
            for i in range(0, len(selected_players), 2)
        ]
