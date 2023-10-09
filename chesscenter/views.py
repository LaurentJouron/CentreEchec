from utils.bases import BaseView


class ChessCenterViews(BaseView):
    def welcome_game(self):
        return self._space_presentation(
            " Welcome to the << CHESS-CENTER >> application "
        )

    def game_instruction(self):
        return self._space_presentation("Please follow the instructions below")

    def display_menu(self, menu_dict):
        return self._display_menu(menu_dict)

    def exit_game(self):
        return self._space_presentation(" EXIT CHESS CENTER ")

    def exiting_game(self):
        return self._star_presentation(" Exiting the program ")

    def message_error(self):
        return self._message_error()
