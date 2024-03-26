from chesscenter.utils.bases.menus import BaseMenu
from chesscenter.utils.bases.date import BaseDate


class RoundView(BaseMenu, BaseDate):
    def display_first_rounds(self):
        self._star_presentation(" FIRST ROUNDS ")
