from utils import presentations
from player.views import PlayerView
from player.models import Player


class PlayerCreationController:
    def __init__(self):
        self.view = PlayerView()
        self.model = Player

    def create(self):
        presentations.enter_information()
        player_data = self.view.get_player_data()
        player = self.model(**player_data)
        player.save()
        presentations.register(
            f"{player_data['first_name']} {player_data['last_name']}"
        )
        return player


class PlayerGetAllController:
    def __init__(self):
        self.model = Player

    def get_all(self):
        print(self.model.get_all())


class PlayerGetOneController:
    def __init__(self):
        self.view = PlayerView()
        self.model = Player

    def get_by_code(self):
        player_code = self.view.get_player_code()
        player = self.model.get_by_code(player_code)
        if player:
            presentations.display_player(player)
        else:
            presentations.error_message("Player not found.")


class PlayerDeleteController:
    def __init__(self):
        self.view = PlayerView()
        self.model = Player

    def remove(self):
        player_code = self.view.get_player_code()
        removed_players = self.model.remove_by_code(player_code)
        if removed_players:
            presentations.success_message("Player removed successfully.")
        else:
            presentations.error_message("Player not found.")
