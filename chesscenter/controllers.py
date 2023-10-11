from utils.bases import BaseController
from utils.constants import CONFIRMATION_MENU
from player.menus import PlayerController

from .views import HomeView


class HomeController(BaseController, HomeView):
    def run(self):
        """
        Main function to handle the home menu.

        Displays the welcome and game instructions, then processes user
        choices.
        Returns the appropriate controller based on the user's choice.
        """
        self.welcome_game()
        self.game_instruction()
        while True:
            choice = self.display_menu(self.home_menu)
            if choice == "1":
                return PlayerController()

            elif choice == "2":
                print("tournament menu")

            elif choice == "3":
                print("tour menu")

            elif choice == "4":
                print("match menu")

            elif choice == "5":
                return ExitController()


class ExitController(BaseController, HomeView):
    def run(self):
        """
        Main function to handle the exit menu.

        Displays the exit message and asks for user confirmation.
        Returns the appropriate controller based on the user's choice.
        """
        self.exit_game()
        choice = self.display_menu(CONFIRMATION_MENU)
        if choice == "1":
            return None
        else:
            return HomeController()
