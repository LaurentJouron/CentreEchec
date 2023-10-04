from utils.presentations import reception, select_number, value_error
from utils.functions import display_menu
from .controller import PlayerCreationController


class PlayerManager:
    def player_menu():
        player_menu = {"1": "Add", "2": "Show", "3": "Remove", "4": "Quit"}
        players = True
        while players:
            reception(" PLAYER RECEPTION ")
            display_menu(player_menu)
            choice_menu = select_number()
            if choice_menu in player_menu:
                if choice_menu == "1":
                    reception(" PLAYER CREATION ")
                    player_creation = PlayerCreationController()
                    player_creation.create()
                elif choice_menu == "2":
                    reception(" ALL PLAYERS IN LIST ")
                elif choice_menu == "3":
                    reception(" REMOVE PLAYER ")
                elif choice_menu == "4":
                    players = False
            else:
                value_error()

