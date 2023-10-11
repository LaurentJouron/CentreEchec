from utils.bases import BaseController

# from chesscenter.controllers import HomeController
from .controllers import (
    PlayerCreationController,
    PlayerGetAllController,
    PlayerRemoveController,
    PlayerGetOneController,
)
from .views import PlayerView


class PlayerController(PlayerView, BaseController):
    def run(self):
        """
        Run the player controller.

        Displays the player menu, collects user choice, and returns the
        corresponding controller.

        Returns:
            BaseController: The selected controller based on the user's choice.
        """
        while True:
            choice = self.display_menu(self.player_menu)
            if choice == "1":
                return PlayerCreationController()

            elif choice == "2":
                return PlayerGetAllController()

            elif choice == "3":
                return PlayerRemoveController()

            elif choice == "4":
                return PlayerGetOneController()

            elif choice == "5":
                ...
                # return HomeController()
