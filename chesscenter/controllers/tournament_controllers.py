from chesscenter.utils.bases.controllers import BaseController
from chesscenter.controllers import home_controllers as home

from chesscenter.views.tournament_views import TournamentView
from chesscenter.models.tournament_models import Tournament
from chesscenter.controllers.player_controllers import PlayerTournament


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


class TournamentCreationController(TournamentController):
    def __init__(self) -> None:
        self.model = Tournament
        self.player = PlayerTournament()

    def run(self):
        view.display_creation()
        tournament_data = view.tournament_data()
        tournament = self.model(
            name=tournament_data["name"],
            place=tournament_data["place"],
            start_date=tournament_data["start_date"],
            end_date=tournament_data["end_date"],
            nbr_round=tournament_data["nbr_round"],
            current_round=tournament_data["current_round"],
            comment=tournament_data["comment"],
            players=self.player.player_for_tournament(),
        )
        tournament.save()
        view.display_tournament_register(tournament_data["name"])
        return TournamentController()


class TournamentReadController(TournamentController):
    def __init__(self) -> None:
        self.model = Tournament

    def run(self):
        view.display_list()
        print(self.model.get_all())
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


class TournamentMatch:
    def __init__(self) -> None:
        self.model = Tournament

    def get_tournament_players(self, tournament_name):
        if tournament := self.model.get_by_name(tournament_name):
            return tournament
        view._message_error(f"Tournament '{tournament_name}' not found")
        return None
