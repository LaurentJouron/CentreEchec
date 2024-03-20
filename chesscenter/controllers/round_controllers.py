from chesscenter.views.round_views import RoundView
from chesscenter.models.round_models import Round
from chesscenter.controllers import home_controllers as home
from chesscenter.utils.bases.controllers import BaseController

view = RoundView()


class RoundController(BaseController):
    def __init__(self):
        self.model = Round

    def run(self):
        view.display_reception()
        while True:
            choice = view.display_menu(view.round_menu)
            if choice == "1":
                return ...

            elif choice == "2":
                return ...

            elif choice == "3":
                return ...

            elif choice == "4":
                return ...

            elif choice == "5":
                return home.HomeController()
