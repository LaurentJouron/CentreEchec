from tinydb import TinyDB, where, table
from typing import List
import string

from chesscenter.utils.constants import DATABASE_NAME


class Tournament:
    db = TinyDB(DATABASE_NAME, indent=4)
    data = db.table("tournament")

    def __init__(self, **kwargs):
        self.name: str = kwargs["name"]
        self.place: str = kwargs["place"]
        self.start_date: str = kwargs["start_date"]
        self.end_date: str = kwargs["end_date"]
        self.nbr_round: int = kwargs["nbr_round"]
        self.current_round: int = kwargs["current_round"]
        self.comment: str = kwargs["comment"]
        self.players: list = kwargs["players"]

    def __repr__(self):
        return (
            f"\nName: {self.name}\n"
            f"Place: {self.place}\n"
            f"Number of round: {self.nbr_round}\n"
            f"Start: {self.start_date}\n"
            f"End: {self.end_date}\n"
            f"Current round: {self.current_round}\n"
            f"Comment: {self.comment}\n"
            f"players: {self.players}\n"
        )

    def __str__(self):
        return (
            f"\nName: {self.name}\n"
            f"Place: {self.place}\n"
            f"Number of round: {self.nbr_round}\n"
            f"Start: {self.start_date}\n"
            f"End: {self.end_date}\n"
            f"Current round: {self.current_round}\n"
            f"Comment: {self.comment}\n"
            f"players: {self.players}\n"
        )

    @property
    def db_instance(self) -> table.Document:
        return Tournament.data.get((where("name") == self.name))

    def save(self, validate_data: bool = False) -> int:
        if validate_data:
            self._checks()
        return -1 if self.exists() else Tournament.data.insert(self.__dict__)

    def _checks(self):
        self._check_names()

    def _check_names(self):
        if not self.name:
            raise ValueError("Name cannot be blank.")
        special_characters = string.punctuation
        for character in self.name + self.place:
            if character in special_characters:
                raise ValueError(f"Value error {self.name}.")

    def exists(self):
        return bool(self.db_instance)

    @classmethod
    def remove_by_name(cls, name):
        return cls.data.remove(where("name") == name)

    @classmethod
    def get_all(cls) -> List["Tournament"]:
        return [cls(**tournament) for tournament in cls.data.all()]

    @classmethod
    def get_by_name(cls, name):
        if tournament_data := cls.data.search(where("name") == name):
            return cls(**tournament_data[0])
        return None

    def serialize_tournament(self):
        return {
            "name": Tournament.name,
            "place": Tournament.place,
            "nbr_round": Tournament.nbr_round,
            "start_date": Tournament.start_date,
            "end_date": Tournament.end_date,
            "current_round": Tournament.current_round,
            "comment": Tournament.comment,
            "players": Tournament.players,
        }

    def deserialize_tournament(self, serialized_tournament):
        name = serialized_tournament["name"]
        place = serialized_tournament["place"]
        nbr_round = serialized_tournament["nbr_round"]
        start_date = serialized_tournament["start_date"]
        end_date = serialized_tournament["end_date"]
        current_round = serialized_tournament["current_round"]
        comment = serialized_tournament["comment"]
        players = serialized_tournament["players"]
        return Tournament(
            name,
            place,
            nbr_round,
            start_date,
            end_date,
            current_round,
            comment,
            players,
        )

    def get_players_list(self):
        return self.players[:]

    def remove_player(self, player):
        self.players.remove(player)
