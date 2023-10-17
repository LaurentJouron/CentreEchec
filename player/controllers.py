from utils.bases.controllers import BaseController
from chesscenter import controllers as home
from .views import PlayerView
from .models import Player

view = PlayerView()


class PlayerController(BaseController):
    def run(self):
        """
        Run the player controller.

        Displays the player menu, collects user choice, and returns the
        corresponding controller.

        Returns:
            BaseController: The selected controller based on the user's choice.
        """
        view.display_reception()
        while True:
            choice = view.display_menu(view.player_menu)
            if choice == "1":
                return PlayerCreationController()

            elif choice == "2":
                return PlayerGetAllController()

            elif choice == "3":
                return PlayerRemoveController()

            elif choice == "4":
                return PlayerGetOneController()

            elif choice == "5":
                return home.HomeController()


class PlayerCreationController:
    def __init__(self):
        self.model = Player

    def run(self):
        """
        Run the player creation controller.

        Displays the creation view, collects player information, and saves
        the player data.

        Returns:
            PlayerController: The controller for player-related actions.
        """
        view.display_creation()
        view.enter_information()
        player_data = view.get_player_data()
        player = self.model(**player_data)
        player.save()
        view.display_player_register(
            f"{player_data['first_name']} {player_data['last_name']}"
        )
        return PlayerController()


class PlayerGetAllController:
    def __init__(self):
        self.model = Player

    def run(self):
        """
        Run the player retrieval controller.

        Displays a list of all players in the database and prints their
        information.

        Returns:
            PlayerController: The controller for player-related actions.
        """
        view.display_list_all()
        print(self.model.get_all())
        return PlayerController()


class PlayerGetOneController:
    def __init__(self):
        self.model = Player

    def run(self):
        """
        Run the player retrieval controller.

        Displays the 'get one' view, prompts for a player code, retrieves
        and displays player information if found. If the player is not found,
        an error message is displayed.

        Returns:
            PlayerController: The controller for player-related actions.
        """
        view.display_details()
        player_code = view.get_player_code()
        player = self.model.get_one_by_code(player_code)
        if player:
            view.display_player(player)
        else:
            view._message_error(player_code)
        return PlayerController()


class PlayerRemoveController:
    def __init__(self):
        self.model = Player

    def run(self):
        """
        Run the player removal controller.

        Displays the 'remove' view, prompts for a player code, and removes
        the player from the database if found. If the player is not found,
        an error message is displayed.

        Returns:
            PlayerController: The controller for player-related actions.
        """
        view.display_remove()
        player_code = view.get_player_code()
        removed_players = self.model.remove_by_code(player_code)
        if removed_players:
            view.success_message(player_code)
        else:
            view._message_error(player_code)
        return PlayerController()
