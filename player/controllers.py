from utils import presentations
from .views import PlayerView
from .models import Player


class PlayerCreationController(PlayerView):
    def __init__(self):
        self.model = Player

    def run(self):
        """
        Run the player creation controller.

        Displays the creation view, collects player information, and saves
        the player data.

        Returns:
            Player: The created player.
        """
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

    def run(self):
        """
        Run the player retrieval controller.

        Displays the list of all players.
        """
        self.display_list_all()
        print(self.model.get_all())


class PlayerGetOneController(PlayerView):
    def __init__(self):
        self.model = Player

    def run(self):
        """
        Run the player retrieval controller.

        Displays the get one view, collects player code, and displays
        player information.
        """
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

    def run(self):
        """
        Run the player removal controller.

        Displays the remove view, collects player code, and removes the player.
        """
        self.display_remove()
        player_code = self.get_player_code()
        removed_players = self.model.remove_by_code(player_code)
        if removed_players:
            presentations.success_message("Player removed successfully.")
        else:
            self.message_error(player_code)
