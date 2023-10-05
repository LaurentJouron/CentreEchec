from tinydb import TinyDB, where, table
import string


class PlayerModel:
    db = TinyDB(f"data/chesscenter.json", indent=4)
    players_db = db.table("players")

    def __init__(self, player_code: str, first_name: str, last_name: str, birthday: str = ""):
        self.player_code = player_code
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday

    def __repr__(self):
        return f"\nNational player code: {self.player_code} Name: {self.full_name} born: {self.birthday}\n"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def db_instance(self) -> table.Document:
        return PlayerModel.players_db.get((where("player_code") == self.player_code))

    def save(self, validate_data: bool = False) -> int:
        if validate_data:
            self._checks()
        return -1 if self.exists() else PlayerModel.players_db.insert(self.__dict__)

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

    # def remove(self) -> list[int]:
    #     if self.exists():
    #         return PlayerModel.players_db.remove(doc_ids=[self.db_instance.doc_id])
    #     return []

    @classmethod
    def get_all(cls):
        return [cls(**player) for player in cls.players_db.all()]

    # @staticmethod
    # def get_one_player(first_name, last_name):
    #     return PlayerModel.players_db.get(
    #         (where("first_name") == first_name) & (where("last_name") == last_name)
    #     )
