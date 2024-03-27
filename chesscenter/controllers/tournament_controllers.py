from ..utils.bases.controllers import BaseController
from ..utils.constants import NUMBER_OF_PLAYERS
from ..models.tournament_models import Tournament
from ..views.tournament_views import TournamentView
from ..controllers import home_controllers as home
from ..controllers.player_controllers import (
    PlayerTournament,
    PlayerController,
)
import random

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

    def first_round(self, players):
        selected_players = random.sample(players, NUMBER_OF_PLAYERS)
        matches = [
            (selected_players[i], selected_players[i + 1])
            for i in range(0, len(selected_players), 2)
        ]
        return matches


class TournamentCreationController(TournamentController):
    def __init__(self) -> None:
        self.model = Tournament
        self.player = PlayerTournament()

    def run(self):
        view.display_creation()
        tournament_data = view.tournament_data()
        tournament_data["players"] = self.player.get_for_tournament()
        first_round_matches = self.first_round(tournament_data["players"])
        tournament = self.model(**tournament_data)
        tournament.rounds.append(first_round_matches)

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


class TournamentRound:
    def __init__(self) -> None:
        self.model = Tournament

    def get_first_round(self):
        tournament_name = view.get_name()
        if tournament := self.model.get_by_name(tournament_name):
            # Parcours de chaque tour dans la liste des tours
            for round_matches in tournament.get("rounds", []):
                # Parcours de chaque match dans le tour
                for match in round_matches:
                    # Récupération des informations sur le premier joueur du match
                    player1_code = match[0]["player_code"]
                    player1_first_name = match[0]["first_name"]
                    player1_last_name = match[0]["last_name"]

                    # Récupération des informations sur le deuxième joueur du match
                    player2_code = match[1]["player_code"]
                    player2_first_name = match[1]["first_name"]
                    player2_last_name = match[1]["last_name"]

                    # Utilisation des informations récupérées
                    print(
                        f"Player 1: {player1_first_name} {player1_last_name} (Code: {player1_code})"
                    )
                    print(
                        f"Player 2: {player2_first_name} {player2_last_name} (Code: {player2_code})"
                    )
