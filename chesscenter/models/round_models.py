from datetime import datetime
from tinydb import TinyDB
from chesscenter.utils.constants import NUMBER_OF_ROUND
from chesscenter.utils.constants import DATABASE_NAME
from .match_models import Match


class Round:
    db = TinyDB(DATABASE_NAME, indent=4)
    data = db.table("round")

    def __init__(self, rounds):
        self.round_number = NUMBER_OF_ROUND
        self.rounds = rounds
        self._timestamp_begin = datetime.now()
        self._timestamp_end = None
        self.round_closed = False

    def __str__(self):
        return (
            f"Round {self.round_number}: \n"
            f"Start: {self.timestamp_begin} - End: {self.timestamp_end}"
        )

    def save(self) -> int:
        return Round.data.insert(self.__dict__)

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
