from chesscenter.utils.bases.menus import BaseMenu


class MatchView(BaseMenu):
    match_menu: dict = {
        "1": "first match",
        "2": "",
        "3": "",
        "4": "",
        "5": "",
    }

    def display_menu(self, menu_dict):
        self._display_menu(menu_dict=menu_dict)
        return self._response_menu(menu_dict=menu_dict)

    def get_name(self):
        return self._get_string("Enter the tournament name: ").capitalize()

    def display_reception(self):
        self._space_presentation(" MATCH RECEPTION ")
