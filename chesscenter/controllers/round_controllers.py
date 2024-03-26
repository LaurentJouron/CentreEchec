from ..views.round_views import RoundView
from ..models.round_models import Round
from ..controllers import home_controllers as home
from ..utils.bases.controllers import BaseController
from ..utils.constants import NUMBER_OF_PLAYERS
from ..models.tournament_models import Tournament
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

    def save_first_round(self, tournament_name, players):
        selected_players = random.sample(players, NUMBER_OF_PLAYERS)
        matches = [
            (selected_players[i], selected_players[i + 1])
            for i in range(0, len(selected_players), 2)
        ]
        round_data = {
            "round_number": 1,  # Assuming this is the first round
            "rounds": matches,
        }
        round_instance = self.model(**round_data)
        round_instance.save()

        if tournament := Tournament.get_by_name(tournament_name):
            tournament.rounds.append(round_instance)
            tournament.save()
        else:
            view._message_error("Tournament not found")
