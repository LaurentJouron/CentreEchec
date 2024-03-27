from ..utils.bases.menus import BaseMenu
from ..utils.bases.date import BaseDate


class RoundView(BaseMenu, BaseDate):
    round_menu: dict = {
        "1": "first round",
        "2": "",
        "3": "",
        "4": "",
        "5": "Return",
    }

    def display_menu(self, menu_dict):
        self._display_menu(menu_dict=menu_dict)
        return self._response_menu(menu_dict=menu_dict)

    def display_first_rounds(self):
        self._star_presentation(" FIRST ROUNDS ")
