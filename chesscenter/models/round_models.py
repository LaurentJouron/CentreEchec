from datetime import datetime
from .match_models import Match


class Round:
    def __init__(self, round_number):
        self.round_number = round_number
        self.matches = []
        self._timestamp_begin = datetime.now()
        self._timestamp_end = None
        self.round_closed = False

    def __str__(self):
        return (
            f"Round {self.round_number}: \n"
            f"Start: {self.timestamp_begin} - End: {self.timestamp_end}"
        )

    @property
    def timestamp_begin(self):
        return self._timestamp_begin.strftime("%d/%m/%Y-%H:%M")

    @property
    def timestamp_end(self):
        if self._timestamp_end:
            return self._timestamp_end.strftime("%d/%m/%Y-%H:%M")
        return ""

    def add_match(self, player1, player2, score1, score2):
        if not (0 <= score1 <= 1) or not (0 <= score2 <= 1):
            raise ValueError("Scores must be between 0 et 1")
        self.matches.append(Match(player1, player2, score1, score2))

    def close_round(self):
        self._timestamp_end = datetime.now()
        self.round_closed = True

    @property
    def closed(self):
        return self.round_closed

    @property
    def len_matches_list(self):
        return len(self.matches)

    def serialize_round(self):
        serialized_matches = [match.serialize() for match in self.matches]
        return {
            "round_number": self.round_number,
            "matches": serialized_matches,
            "timestamp_begin": self.timestamp_begin,
            "timestamp_end": self.timestamp_end,
            "round_closed": self.round_closed,
        }

    @classmethod
    def deserialize_round(cls, serialized_round):
        round_instance = cls(serialized_round["round_number"])
        round_instance._timestamp_begin = datetime.strptime(
            serialized_round["timestamp_begin"], "%d/%m/%Y-%H:%M"
        )
        round_instance._timestamp_end = (
            datetime.strptime(
                serialized_round["timestamp_end"], "%d/%m/%Y-%H:%M"
            )
            if serialized_round["timestamp_end"]
            else None
        )
        round_instance.round_closed = serialized_round["round_closed"]
        round_instance.matches = [
            Match.deserialize(match_data)
            for match_data in serialized_round["matches"]
        ]
        return round_instance
