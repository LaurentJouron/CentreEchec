from chesscenter.controllers import HomeController
from .views import HomeView

views = HomeView()


def run_application():
    """
    Main function of the application.

    Initializes the main controller and runs the application loop.
    """
    controller = HomeController()
    while controller is not None:
        next_controller = controller.run()
        controller = next_controller
    views.good_by()


run_application()
