from datetime import datetime

from .match_models import Match


class Round:
    def __init__(self, round_number):
        self.round_number = f"round {str(round_number)}"
        self.matches = []
        self.timestamp_begin = datetime.now().strftime("%d/%m/%Y-%H:%M")
        self.timestamp_end = ""
        self.round_closed = False

    def __str__(self):
        return f"{self.round_number}: début: {self.timestamp_begin} - fin: {self.timestamp_end}"

    def add_match(self, player1, player2, score1, score2):
        self.matches.append(Match(player1, player2, score1, score2))

    def close_round(self):
        self.timestamp_end = datetime.now().strftime("%d/%m/%Y-%H:%M")
        self.round_closed = True
        return self.timestamp_end

    @property
    def closed(self):
        return self.round_closed

    @property
    def len_matches_list(self):
        return len(self.matches)

    def serialized_round(self):
        serialized_match = [match.serialize_match() for match in self.matches]
        return {
            "round_name": self.round_name,
            "matches": serialized_match,
            "timestamp_begin": str(self.timestamp_begin),
            "timestampe_end": str(self.timestamp_end),
            "round_closed": self.round_closed,
        }

    def deserialized_round(self, serialized_round):
        self.round_name = serialized_round["round_name"]
        self.timestamp_begin = serialized_round["timestamp_begin"]
        self.timestamp_end = serialized_round["timestamp_end"]
        self.round_closed = serialized_round["round_closed"]
        self.matches = []
        non_empty_matches = len(serialized_round["matches"])
        for index in range(non_empty_matches):
            self.matches.append(Match("", "", "", ""))
            self.matches[index] = self.matches[index].deserialize_match(
                serialized_round["matches"][index]
            )
        return self
