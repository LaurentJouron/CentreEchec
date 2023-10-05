from utils.presentations import reception, select_number, value_error
from utils.functions import display_menu
from utils.constants import PLAYER_MENU
from .controllers import (
    PlayerCreationController,
    PlayerGetAllController,
    PlayerDeleteController,
    PlayerGetOneController
    )


class PlayerManager:
    def menu(self):
        players = True
        while players:
            reception(" PLAYER RECEPTION ")
            display_menu(PLAYER_MENU)
            choice_menu = select_number()
            if choice_menu in PLAYER_MENU:

                if choice_menu == "1":
                    reception(" PLAYER CREATION ")
                    player_creation = PlayerCreationController()
                    player_creation.create()

                elif choice_menu == "2":
                    reception(" ALL PLAYERS IN LIST ")
                    player_get_all = PlayerGetAllController()
                    print(player_get_all.get_all())

                elif choice_menu == "3":
                    reception(" REMOVE PLAYER ")
                    player_delete = PlayerDeleteController()
                    player_delete.remove()

                elif choice_menu =="4":
                    player_detail = PlayerGetOneController()
                    player_detail.get_by_code()
                elif choice_menu == "5":
                    players = False
            else:
                value_error()
