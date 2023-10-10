from utils.presentations import select_number
from .controllers import (
    PlayerCreationController,
    PlayerGetAllController,
    PlayerDeleteController,
    PlayerGetOneController,
)
from .views import PlayerView


class PlayerMenu(PlayerView):
    def menu(self):
        players = True
        while players:
            self.display_player_reception()
            self.display_menu(self.player_menu)
            choice_menu = select_number()
            if choice_menu in self.player_menu:
                if choice_menu == "1":
                    self.player_creation()
                    player = PlayerCreationController()
                    player.create()

                elif choice_menu == "2":
                    self.player_list_all()
                    player = PlayerGetAllController()
                    player.get_all()

                elif choice_menu == "3":
                    self.player_remove()
                    player = PlayerDeleteController()
                    player.remove()

                elif choice_menu == "4":
                    player = PlayerGetOneController()
                    player.get_one_by_code()

                elif choice_menu == "5":
                    players = False
            else:
                self.message_error()


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
