from ..utils.constants import DATABASE_NAME
from datetime import datetime
from .match_models import Match
from datetime import datetime
from tinydb import TinyDB


class Round:
    db = TinyDB(DATABASE_NAME, indent=4)
    data = db.table("round")

    def __init__(self, round_number, rounds):
        self.round_number = round_number
        self.rounds = rounds
        self._timestamp_begin = datetime.now()
        self._timestamp_end = None
        self.round_closed = False

    def __str__(self):
        return (
            f"Round {self.round_number}: \n"
            f"Start: {self.timestamp_begin} - End: {self.timestamp_end}"
        )

    def save(self):
        round_data = {
            "round_number": self.round_number,
            "rounds": self.rounds,
            "_timestamp_begin": str(self._timestamp_begin),
            "_timestamp_end": str(self._timestamp_end),
            "round_closed": self.round_closed,
        }
        self.data.insert(round_data)

    @property
    def timestamp_begin(self):
        return self._timestamp_begin.strftime("%d/%m/%Y-%H:%M")

    @property
    def timestamp_end(self):
        if self._timestamp_end:
            return self._timestamp_end.strftime("%d/%m/%Y-%H:%M")
        return ""

    def add_match(self, player0, player1, score0, score1):
        if not (0 <= score0 <= 1) or not (0 <= score1 <= 1):
            raise ValueError("Scores must be between 0 et 1")
        self.matches.append(Match(player0, player1, score0, score1))

    def close_round(self):
        self._timestamp_end = datetime.now()
        self.round_closed = True

    @property
    def closed(self):
        return self.round_closed

    @property
    def len_matches_list(self):
        return len(self.rounds)
