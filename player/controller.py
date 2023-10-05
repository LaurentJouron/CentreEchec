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
        player = self.model(**player_data)
        player.save()
        presentations.register(
            f"{player_data['first_name']} {player_data['last_name']}"
            )
        return player


class PlayerModifyController:
    ...


class PlayerGetAllController:
    def __init__(self):
        self.model = PlayerModel

    def get_all(self):
        return self.model.get_all()


class PlayerGetOneController:
    ...


class PlayerDeleteController:
    ...
