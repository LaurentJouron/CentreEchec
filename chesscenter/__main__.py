from utils.presentations import (
    welcome,
    instruction,
    select_number,
    reception,
    value_error,
    exiting_program
)
from utils.functions import display_menu
from utils.constants import CONFIRMATION_MENU, CHESS_MENU
from player.menus import PlayerManager


def main():
    player_manager = PlayerManager()
    welcome()
    instruction()
    chesscenter = True
    while chesscenter:
        display_menu(CHESS_MENU)

        choice_menu = select_number()
        if choice_menu in CHESS_MENU:
            if choice_menu == "1":
                player_manager.menu()
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


main()
