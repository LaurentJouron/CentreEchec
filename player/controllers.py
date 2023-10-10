from utils import presentations
from .views import PlayerView
from .models import Player


class PlayerCreationController(PlayerView):
    def __init__(self):
        self.model = Player

    def create(self):
        self.display_creation()
        presentations.enter_information()
        player_data = self.get_player_data()
        player = self.model(**player_data)
        player.save()
        presentations.register(
            f"{player_data['first_name']} {player_data['last_name']}"
        )
        return player


class PlayerGetAllController(PlayerView):
    def __init__(self):
        self.model = Player

    def get_all(self):
        self.display_list_all()
        print(self.model.get_all())


class PlayerGetOneController(PlayerView):
    def __init__(self):
        self.model = Player

    def get_one_by_code(self):
        self.display_get_one()
        player_code = self.get_player_code()
        player = self.model.get_one_by_code(player_code)
        if player:
            presentations.display_player(player)
        else:
            self.message_error(player_code)


class PlayerRemoveController(PlayerView):
    def __init__(self):
        self.model = Player

    def remove(self):
        self.display_remove()
        player_code = self.get_player_code()
        removed_players = self.model.remove_by_code(player_code)
        if removed_players:
            presentations.success_message("Player removed successfully.")
        else:
            self.message_error(player_code)
