from utils.bases import BaseController
from utils.constants import CONFIRMATION_MENU
from player.menus import PlayerController

from .views import HomeView


class HomeController(BaseController, HomeView):
    def run(self):
        while True:
            choice = self.display_menu(self.CHESS_MENU)
            if choice == "1":
                player = PlayerController()
                return player.run()
            elif choice == "2":
                print("tournament menu")
            elif choice == "3":
                print("tour menu")
            elif choice == "4":
                print("match menu")
            elif choice == "5":
                exit_controller = ExitController()
                return exit_controller.run()


class ExitController(HomeView):
    def run(self):
        choice = self.display_menu(CONFIRMATION_MENU)
        if choice == "1":
            return None
        else:
            home_controller = HomeController()
            return home_controller.run()
