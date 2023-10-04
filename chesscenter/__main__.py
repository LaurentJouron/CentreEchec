from utils.presentations import welcome, instruction
from utils.functions import display_menu
from player.menu import PlayerManager


class ChessCenter:
    
    def manage_menu():
        start_menu = {
            '1': 'Player',
            '2': 'Tournament',
            '3': 'Match',
            '4': 'Tour',
            '5': 'Quit'
            }
        welcome()
        instruction()
        display_menu(start_menu)

        PlayerManager.player_menu()


ChessCenter.manage_menu()
