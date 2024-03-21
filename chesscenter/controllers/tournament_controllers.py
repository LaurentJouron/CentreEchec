from chesscenter.utils.bases.controllers import BaseController
from chesscenter.controllers import home_controllers as home

from chesscenter.views.tournament_views import TournamentView
from chesscenter.models.tournament_models import Tournament
from .player_controllers import PlayerToTournamentController

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
                return TournamentManagerController()

            elif choice == "6":
                return home.HomeController()


class TournamentCreationController(TournamentController):
    def __init__(self) -> None:
        self.model = Tournament

    def run(self):
        view.display_creation()
        tournament_data = view.tournament_data()
        tournament = self.model(**tournament_data)
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


class TournamentManagerController(BaseController):
    def __init__(self):
        self.selected_tournament = None

    def run(self):
        view.display_manager()
        tournament = view.get_name()
        while True:
            choice = view.display_menu(view.tournament_manager)
            if choice == "1":
                return TournamentAddPlayerController(tournament)

            elif choice == "2":
                return ...

            elif choice == "3":
                return ...

            elif choice == "4":
                return ...

            elif choice == "5":
                return TournamentController()

    def select_tournament(self, tournament):
        self.selected_tournament = tournament


class TournamentAddPlayerController(BaseController):
    def __init__(self, tournament):
        self.model = tournament

    def run(self):
        player_controller = PlayerToTournamentController()
        new_player = player_controller.run()
        self.model.append_player(player=new_player)

        print("Player added successfully to the tournament!")
        return TournamentManagerController()
