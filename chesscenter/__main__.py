from utils.presentations import welcome, instruction, select_number, reception, value_error, exiting_program
from utils.functions import display_menu
from utils.constants import CONFIRMATION_MENU
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
        chesscenter = True
        while chesscenter:
            display_menu(start_menu)

            choice_menu = select_number()
            if choice_menu in start_menu:
                if choice_menu == "1":
                    PlayerManager.player_menu()
                elif choice_menu == "2":
                    ...
                elif choice_menu == "3":
                    ...
                elif choice_menu == "4":
                    ...
                elif choice_menu == "5":
                    reception(" EXIT CHESS CENTER ")
                    exiting_program()
                    display_menu(CONFIRMATION_MENU)
                    confirmation = select_number()
                    if confirmation in CONFIRMATION_MENU:
                        if confirmation == "1":
                            chesscenter = False
                        elif confirmation == "2":
                            chesscenter = True
                        else:
                            value_error()
                    else:
                        value_error()
                else:
                    value_error()
            else:
                value_error()


ChessCenter.manage_menu()
