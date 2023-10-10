from utils.bases import BaseController
from utils.constants import CONFIRMATION_MENU, CHESS_MENU
from player.menus import PlayerController

from .views import HomeView


class HomeController(BaseController, HomeView):
    def run(self):
        choice = self.display_menu(CHESS_MENU)
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
            choice = self.display_menu(CONFIRMATION_MENU)
            if choice in CONFIRMATION_MENU:
                if choice == "1":
                    return None
                elif choice == "2":
                    home = HomeController()
                    return home.run()
