from utils.bases.views import BaseView


class MenuBaseView(BaseView):
    def _display_menu(self, menu_dict):
        """
        Display a menu and return the user's choice.

        Args:
            menu_dict (dict): A dictionary of menu options.

        Returns:
            None
        """
        menu_options = " | ".join(
            [f" {keys}. {value} " for keys, value in menu_dict.items()]
        )
        return self._star_presentation(menu_options)

    def _response_menu(self, menu_dict):
        """
        Collect and validate the user's choice from the menu.

        Args:
            menu_dict (dict): A dictionary of menu options.

        Returns:
            str: The user's choice.
        """
        choice = self._select_number()
        if choice in menu_dict:
            return choice
        return self._message_error(choice)
