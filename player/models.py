from tinydb import TinyDB, where, table
from typing import List
import string

from utils.constants import DATABASE_NAME


class Player:
    """
    Represents a chess player.

    Attributes:
        player_code (str): A unique code for the player.
        first_name (str): The first name of the player.
        last_name (str): The last name of the player.
        birthday (str): The birthday of the player.
        gender (str): The gender of the player.
    """

    db = TinyDB(DATABASE_NAME, indent=4)
    data = db.table("players")

    def __init__(self, **kwargs):
        self.player_code = kwargs["player_code"]
        self.first_name = kwargs["first_name"]
        self.last_name = kwargs["last_name"]
        self.birthday = kwargs["birthday"]
        self.gender = kwargs["gender"]

    def __repr__(self):
        """
        Get a string representation of the player.

        Returns:
            str: A formatted string representing the player.
        """
        return f"\n\t{self.player_code}\t {self.full_name}\n"

    def __str__(self):
        """
        Get a string representation of the player.

        Returns:
            str: A formatted string representing the player.
        """
        return f"\n{self.player_code}\
            \n{self.full_name}\
            \n{self.birthday}\
            \n{self.gender}\n"

    @property
    def full_name(self):
        """
        Get the full name of the player.

        Returns:
            str: The full name of the player.
        """
        return f"{self.first_name} {self.last_name}"

    @property
    def db_instance(self) -> table.Document:
        """
        Get the database instance of the player.

        Returns:
            table.Document: The database instance of the player.
        """
        return Player.data.get(
            (where("first_name") == self.first_name)
            & (where("last_name") == self.last_name)
        )

    def save(self, validate_data: bool = False) -> int:
        """
        Save the player data to the database.

        Args:
            validate_data (bool): Whether to validate data before saving.

        Returns:
            int: The ID of the inserted data, or -1 if the player
            already exists.
        """
        if validate_data:
            self._checks()
        return -1 if self.exists() else Player.data.insert(self.__dict__)

    def _checks(self):
        self._check_names()

    def _check_names(self):
        if not self.first_name:
            raise ValueError("First and last name cannot be blank.")
        special_characters = string.punctuation + string.digits
        for character in self.first_name + self.last_name:
            if character in special_characters:
                raise ValueError(f"Value error {self.full_name}.")

    def exists(self):
        """
        Check if the player data already exists in the database.

        Returns:
            bool: True if the player exists, otherwise False.
        """
        return bool(self.db_instance)

    @classmethod
    def remove_by_code(cls, player_code):
        """
        Remove a player by their code.

        Args:
            player_code (str): The code of the player to remove.
        """
        return cls.data.remove(where("player_code") == player_code)

    @classmethod
    def get_all(cls) -> List["Player"]:
        """
        Get a list of all players.

        Returns:
            List[Player]: A list of Player objects.
        """
        return [cls(**player) for player in cls.data.all()]

    @classmethod
    def get_one_by_code(cls, player_code) -> "Player":
        """
        Get a player by their code.

        Args:
            player_code (str): The code of the player to retrieve.

        Returns:
            Player: The Player object, or None if not found.
        """
        player_data = cls.data.search(where("player_code") == player_code)
        if player_data:
            return cls(**player_data[0])
        return None
