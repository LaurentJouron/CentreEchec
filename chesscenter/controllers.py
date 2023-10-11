from utils.bases.controllers import BaseController
from utils.constants import CONFIRMATION_MENU
from player.controllers import PlayerController

from .views import HomeView

view = HomeView()


class HomeController(BaseController):
    def run(self):
        """
        Main function to handle the home menu.

        Displays the welcome and game instructions, then processes user
        choices.
        Returns the appropriate controller based on the user's choice.
        """
        view.welcome_game()
        view.game_instruction()
        while True:
            choice = view.display_menu(view.home_menu)
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


class ExitController(BaseController):
    def run(self):
        """
        Main function to handle the exit menu.

        Displays the exit message and asks for user confirmation.
        Returns the appropriate controller based on the user's choice.
        """
        view.exit_game()
        choice = view.display_menu(CONFIRMATION_MENU)
        if choice == "1":
            return None
        else:
            return HomeController()
