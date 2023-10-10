from utils.bases import BaseView, MenuBaseView


class HomeView(MenuBaseView, BaseView):
    def display_menu(self, menu_dict):
        self.welcome_game()
        self.game_instruction()
        self._display_menu(menu_dict=menu_dict)
        return self._response_menu(menu_dict=menu_dict)

    # Presentation
    def welcome_game(self):
        return self._space_presentation(
            " Welcome to the << CHESS-CENTER >> application "
        )

    def game_instruction(self):
        return self._space_presentation("Please follow the instructions below")

    def exit_game(self):
        return self._space_presentation(" EXIT CHESS CENTER ")

    def exiting_game(self):
        return self._star_presentation(" Exiting the program ")

    def good_by(self):
        return self._space_presentation("Good day and see you soon")
