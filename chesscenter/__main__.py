from chesscenter.controllers import HomeController


def main():
    controller = HomeController()
    while controller is not None:
        next_controller = controller.run()
        controller = next_controller
    print("Good day and see you soon")


main()
