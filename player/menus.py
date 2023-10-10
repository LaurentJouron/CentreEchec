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
        while True:
            choice = self.display_menu(self.PLAYER_MENU)
            if choice == "1":
                player = PlayerCreationController()
                return player.create()

            elif choice == "2":
                player = PlayerGetAllController()
                return player.get_all()

            elif choice == "3":
                player = PlayerRemoveController()
                return player.remove()

            elif choice == "4":
                player = PlayerGetOneController()
                return player.get_one_by_code()

            # elif choice == "5":
            # home = HomeController()
            # return home.run()
