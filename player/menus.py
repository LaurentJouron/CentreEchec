from utils.presentations import select_number
from utils.constants import PLAYER_MENU
from utils.bases import BaseView
from .controllers import (
    PlayerCreationController,
    PlayerGetAllController,
    PlayerDeleteController,
    PlayerGetOneController,
)
from .views import PlayerView

views = PlayerView()


class PlayerMenu(BaseView):
    def menu(self):
        players = True
        while players:
            views.player_reception()
            views.display_menu(PLAYER_MENU)
            choice_menu = select_number()
            if choice_menu in PLAYER_MENU:
                if choice_menu == "1":
                    views.player_creation()
                    player = PlayerCreationController()
                    player.create()

                elif choice_menu == "2":
                    views.player_list_all()
                    player = PlayerGetAllController()
                    player.get_all()

                elif choice_menu == "3":
                    views.player_remove()
                    player = PlayerDeleteController()
                    player.remove()

                elif choice_menu == "4":
                    player = PlayerGetOneController()
                    player.get_one_by_code()

                elif choice_menu == "5":
                    players = False
            else:
                views.message_error()


# from utils.bases import BaseController
# from chesscenter.controllers import HomeController

# class PlayerController(BaseController):
#     def action(self):
#         display_menu(PLAYER_MENU)
#         choice_menu = select_number()
#         if choice_menu in PLAYER_MENU:
#             if choice_menu == "1":
#                 return PlayerCreationController()

#             elif choice_menu == "2":
#                 return PlayerGetAllController()

#             elif choice_menu == "3":
#                 return PlayerDeleteController()

#             elif choice_menu == "4":
#                 return PlayerGetOneController()

#             elif choice_menu == "5":
#                 return HomeController()
