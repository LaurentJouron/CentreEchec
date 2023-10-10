from utils.bases import BaseView, MenuBaseView


class HomeView(MenuBaseView, BaseView):
    CHESS_MENU: dict = {
        "1": "Player",
        "2": "Tournament",
        "3": "Match",
        "4": "Tour",
        "5": "Quit",
    }

    def display_menu(self, menu_dict):
        self.welcome_game()
        self.game_instruction()
        self._display_menu(menu_dict=menu_dict)
        return self._response_menu(menu_dict=menu_dict)

    # Presentation
    def welcome_game(self):
        return self._space_presentation(" Welcome on << CHESS-CENTER >> ")

    def game_instruction(self):
        return self._space_presentation("Please follow the instructions below")

    def exit_game(self):
        return self._space_presentation(" EXIT CHESS CENTER ")

    def good_by(self):
        return self._space_presentation("Good day and see you soon...\n")

    def exiting_game(self):
        return self._star_presentation(" Exiting the program ")
