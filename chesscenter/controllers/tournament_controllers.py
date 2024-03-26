from chesscenter.utils.bases.controllers import BaseController
from chesscenter.controllers import home_controllers as home

from chesscenter.views.tournament_views import TournamentView
from chesscenter.models.tournament_models import Tournament
from chesscenter.controllers.player_controllers import (
    PlayerTournament,
    PlayerController,
)
from chesscenter.controllers.round_controllers import RoundFirstController


view = TournamentView()


class TournamentController(BaseController):
    def run(self):
        view.display_reception()
        while True:
            choice = view.display_menu(view.tournament_menu)
            if choice == "1":
                return TournamentCreationController()

            elif choice == "2":
                return TournamentReadController()

            elif choice == "3":
                return TournamentRemoveController()

            elif choice == "4":
                return TournamentGetOneController()

            elif choice == "5":
                return home.HomeController()

    def get_tournament_in_tournaments(self, tournaments):
        for tournament in tournaments:
            name = tournament.name
            place = tournament.place
            start_date = tournament.start_date
            end_date = tournament.end_date
            nbr_round = tournament.nbr_round
            current_round = tournament.current_round
            comment = tournament.comment
            players = self.players.get_player_in_players(tournament.players)
            print(
                name,
                place,
                start_date,
                end_date,
                nbr_round,
                current_round,
                comment,
                players,
            )


class TournamentCreationController(TournamentController):
    def __init__(self) -> None:
        self.model = Tournament
        self.player = PlayerTournament()

    def run(self):
        view.display_creation()
        tournament_data = view.tournament_data()
        tournament_data["players"] = self.player.player_for_tournament()
        RoundFirstController(tournament_data["players"])
        tournament = self.model(**tournament_data)
        tournament.save()
        view.display_tournament_register(tournament_data["name"])
        return TournamentController()


class TournamentReadController(TournamentController):
    def __init__(self) -> None:
        self.model = Tournament
        self.players = PlayerController()

    def run(self):
        view.display_list()
        tournaments = self.model.get_all()
        self.get_tournament_in_tournaments(tournaments)
        return TournamentController()


class TournamentGetOneController(TournamentController):
    def __init__(self):
        self.model = Tournament

    def run(self):
        view.display_details()
        tournament_name = view.get_name()
        while True:
            if tournament := self.model.get_by_name(tournament_name):
                view.display_tournament(tournament)
            else:
                view._message_error(tournament_name)
                return TournamentGetOneController()
            return TournamentController()


class TournamentRemoveController(TournamentController):
    def __init__(self):
        self.model = Tournament

    def run(self):
        view.display_remove()
        tournament_name = view.get_name()
        if self.model.remove_by_name(name=tournament_name):
            view.success_message(tournament_name)
        else:
            view._message_error(tournament_name)
        return TournamentController()
