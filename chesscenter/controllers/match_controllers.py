from chesscenter.views.match_views import MatchView
from chesscenter.models.match_models import Match
from chesscenter.controllers import home_controllers as home
from chesscenter.utils.bases.controllers import BaseController
from chesscenter.utils.constants import NUMBER_OF_PLAYERS
from chesscenter.controllers.tournament_controllers import TournamentMatch
import random

view = MatchView()


class MatchController(BaseController):
    def __init__(self):
        self.model = Match

    def run(self):
        view.display_reception()
        while True:
            choice = view.display_menu(view.match_menu)
            if choice == "1":
                return FirstMatch()

            elif choice == "5":
                return home.HomeController()


class FirstMatch(MatchController):
    def __init__(self):
        self.model = Match
        self.tournament = TournamentMatch()

    def run(self):
        tournament_name = view.get_name()
        if tournament := self.tournament.get_tournament_players(
            tournament_name
        ):
            players = tournament.players
            selected_players = random.sample(players, NUMBER_OF_PLAYERS)
            first_matches = []
            for i in range(0, len(selected_players), 2):
                match = Match(
                    selected_players[i], selected_players[i + 1], 0, 0
                )
                first_matches.append(match)
            return first_matches
