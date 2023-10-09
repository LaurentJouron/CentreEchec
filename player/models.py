from tinydb import TinyDB, where, table
import string

from utils.constants import DATABASE_NAME


class Player:
    db = TinyDB(DATABASE_NAME, indent=4)
    data = db.table("players")

    def __init__(
        self, player_code: str, first_name: str, last_name: str, birthday: str = ""
    ):
        self.player_code = player_code
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday

    def __repr__(self):
        return f"\n\t{self.player_code}\t {self.full_name}\n"

    def __str__(self):
        return f"\n{self.player_code}\n{self.full_name}\n{self.birthday}\n"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def db_instance(self) -> table.Document:
        return Player.data.get(
            (where("first_name") == self.first_name)
            & (where("last_name") == self.last_name)
        )

    def save(self, validate_data: bool = False) -> int:
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
        return bool(self.db_instance)

    @classmethod
    def remove_by_code(cls, player_code):
        return cls.data.remove(where("player_code") == player_code)

    @classmethod
    def get_all(cls):
        return [cls(**player) for player in cls.data.all()]

    @classmethod
    def get_one_by_code(cls, player_code):
        player_data = cls.data.search(where("player_code") == player_code)
        if player_data:
            return cls(**player_data[0])
        return None
