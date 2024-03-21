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
        self.nbr_round: int = kwargs["nbr_round"]
        self.start_date: str = kwargs["start_date"]
        self.end_date: str = kwargs["end_date"]
        self.current_round: int = kwargs["current_round"]
        self.comment: str = kwargs["comment"]
        self.players: list = []
        self.rounds: list = []

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
            f"rounds: {self.rounds}\n"
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
            f"rounds: {self.rounds}\n"
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
            "rounds": Tournament.rounds,
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
        rounds = serialized_tournament["rounds"]
        return Tournament(
            name,
            place,
            nbr_round,
            start_date,
            end_date,
            current_round,
            comment,
            players,
            rounds,
        )

    # def append_player(self, player):
    #     len_players = len(self.players)
    #     if len_players < self.nb_players:
    #         self.players.append(player)
    #         print(f"\nThere are {len_players + 1} remains place.")
    #         remains_place = self.nb_players - len_players
    #         print(f"There are {remains_place - 1} places left.")
    #     else:
    #         print("This tournament is completed")

    def append_player(self, player):
        # Vérifier si le nombre de joueurs actuels est inférieur au nombre maximal de joueurs autorisés
        if len(self.players) < self.nb_players:
            self.players.append(player)
            print(
                f"Player {player.name} has been successfully added to the tournament."
            )
            print(
                f"There are {self.nb_players - len(self.players)} places left."
            )
            self.saved()  # Sauvegarder les modifications dans la base de données
        else:
            print("This tournament is already full.")

    def saved(self):
        # Mettre à jour la base de données avec les données du tournoi
        tournament_data = {
            "name": self.name,
            "place": self.place,
            "nbr_round": self.nbr_round,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "current_round": self.current_round,
            "comment": self.comment,
            "players": [
                player.__dict__ for player in self.players
            ],  # Convertir les objets joueur en dictionnaires
        }
        # Enregistrer les données mises à jour dans la base de données
        self.data.update(tournament_data, where("name") == self.name)

    def get_players_list(self):
        return self.players[:]

    def remove_player(self, player):
        self.players.remove(player)
