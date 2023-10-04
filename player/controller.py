from utils import presentations
from player.views import PlayerView
from player.models import PlayerModel


class PlayerCreationController:
    def __init__(self):
        self.view = PlayerView()
        self.model = PlayerModel

    def create(self):
        presentations.enter_information()
        player_data = self.view.get_player_data()
        player = self.model(
            first_name=player_data["first_name"],
            last_name=player_data["last_name"],
            birthday=player_data["birthday"],
            code=player_data["code"],
        )
        player.save()
        self.view.register(f"{player_data['first_name']} {player_data['last_name']}")
        return player


class PlayerModifyController:
    ...


class PlayerDeleteController:
    ...
