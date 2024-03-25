from chesscenter.views.player_views import PlayerView
from chesscenter.models.player_models import Player
from chesscenter.controllers import home_controllers as home
from chesscenter.utils.bases.controllers import BaseController
from chesscenter.utils.constants import NUMBER_OF_PLAYERS

view = PlayerView()


class PlayerController(BaseController):
    def __init__(self):
        self.model = Player

    def run(self):
        view.display_reception()
        while True:
            choice = view.display_menu(view.player_menu)
            if choice == "1":
                return PlayerCreationController()

            elif choice == "2":
                return PlayerReadController()

            elif choice == "3":
                return PlayerRemoveController()

            elif choice == "4":
                return PlayerGetOneController()

            elif choice == "5":
                return home.HomeController()


class PlayerCreationController(PlayerController):
    def __init__(self) -> None:
        self.model = Player

    def run(self):
        view.display_creation()
        view.enter_information()
        player_data = view.get_data()
        player = self.model(**player_data)
        player.save()
        view.display_player_register(
            f"{player_data['first_name']} {player_data['last_name']}"
        )
        return PlayerController()


class PlayerReadController(PlayerController):
    def __init__(self) -> None:
        self.model = Player

    def run(self):
        view.display_list()
        print(self.model.get_all())
        return PlayerController()


class PlayerGetOneController(PlayerController):
    def __init__(self):
        self.model = Player

    def run(self):
        view.display_details()
        player_code = view.get_player_code()
        while True:
            if player := self.model.get_one_by_code(player_code=player_code):
                view.display_player(player=player)
            else:
                view._message_error(var=player_code)
                return PlayerGetOneController()
            return PlayerController()


class PlayerRemoveController(PlayerController):
    def __init__(self):
        self.model = Player

    def run(self):
        view.display_remove()
        player_code = view.get_player_code()
        if self.model.remove_by_code(player_code=player_code):
            view.success_message(player=player_code)
        else:
            view._message_error(player_code)
        return PlayerController()


class PlayerTournament:
    def __init__(self) -> None:
        self.model = Player

    def player_for_tournament(self):
        players = []
        while len(players) < NUMBER_OF_PLAYERS:
            view.display_code()
            player_code = view.get_player_code()
            if player := self.model.get_one_by_code(player_code=player_code):
                new_player = {
                    "player_code": player.player_code,
                    "first_name": player.first_name,
                    "last_name": player.last_name,
                    "birthday": player.birthday,
                    "gender": player.gender,
                    "rank": 0,
                }
                players.append(new_player)
                print(f"\nThere are {len(players)} players in the list.")
            print("The player list is complete.")
        return players
