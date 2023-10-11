from utils.bases import MenuBaseView


class HomeView(MenuBaseView):
    home_menu: dict = {
        "1": "Player",
        "2": "Tournament",
        "3": "Match",
        "4": "Tour",
        "5": "Quit",
    }

    def display_menu(self, menu_dict):
        """
        Display a menu and get user's choice.

        Args:
            menu_dict (dict): The menu options.

        Returns:
            str: The user's choice.
        """
        self._display_menu(menu_dict=menu_dict)
        return self._response_menu(menu_dict=menu_dict)

    # Presentation
    def welcome_game(self):
        """
        Display a welcome message.
        """
        return self._space_presentation(" Welcome on << CHESS-CENTER >> ")

    def game_instruction(self):
        """
        Display game instructions.
        """
        return self._space_presentation("Please follow the instructions below")

    def exit_game(self):
        """
        Display an exit message.
        """
        return self._space_presentation(" EXIT CHESS CENTER ")

    def good_by(self):
        """
        Display a farewell message.
        """
        return self._space_presentation("Good day and see you soon...\n")

    def exiting_game(self):
        """
        Display a message for exiting the program.
        """
        return self._star_presentation(" Exiting the program ")
