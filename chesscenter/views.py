from utils.bases import BaseView
from utils.constants import CHESS_MENU


class ChessCenterViews(BaseView):
    def welcome_game(self):
        return self._space_presentation(
            " Welcome to the << CHESS-CENTER >> application "
        )

    def game_instruction(self):
        return self._space_presentation("Please follow the instructions below")

    def display_menu(self):
        return self._display_menu(CHESS_MENU)
