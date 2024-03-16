from tinydb import TinyDB, where, table
import string

from chesscenter.utils.constants import DATABASE_NAME


class Tournament:
    db = TinyDB(DATABASE_NAME, indent=4)
    data = db.table("tournament")

    def __init__(self, **kwargs):
        self.name = kwargs["name"]
        self.place = kwargs["place"]
        self.nbr_tour = kwargs["nbr_tour"]
        self.start_date = kwargs["start_date"]
        self.end_date = kwargs["end_date"]
        self.current_round = kwargs["current_round"]
        self.comment = kwargs["comment"]

    def __repr__(self):
        return (
            f"\nName: {self.name}\n"
            f"Place: {self.place}\n"
            f"Start: {self.start_date}\n"
        )

    def __str__(self):
        return f"\n Name: {self.name}\t Place: {self.place}"

    @property
    def db_instance(self) -> table.Document:
        return Tournament.data.get(
            (where("name") == self.name)
            & (where("place") == self.place)
            & (where("start_date") == self.start_date)
        )

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
    def get_all(cls):
        return [cls(**tournament) for tournament in cls.data.all()]

    @classmethod
    def get_by_name(cls, name):
        if tournament_data := cls.data.search(where("name") == name):
            return cls(**tournament_data[0])
        return None
