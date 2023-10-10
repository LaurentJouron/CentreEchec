from chesscenter.controllers import HomeController
from .views import HomeView

views = HomeView()


def main():
    controller = HomeController()
    while controller is not None:
        next_controller = controller.run()
        controller = next_controller
    views.good_by()


main()
