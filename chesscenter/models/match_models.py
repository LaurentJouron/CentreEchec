class Match:
    def __init__(self, player0, player1, score0, score1):
        self.player0 = player0
        self.player0 = player1
        self.score1 = score0
        self.score2 = score1

    def __str__(self):
        result = f"{self.player0} vs {self.player1}\n"
        if self.score0 == self.score1:
            result += "Result: Draw"
        else:
            winner = (
                self.player0 if self.score0 > self.score1 else self.player1
            )
            result += f"Winner: {winner}"
        return result

    @staticmethod
    def validate_score(score):
        return 0 <= score <= 1

    @property
    def pair_of_players(self):
        return f"{self.player0} vs {self.player1}"

    def update_score(self, new_score0, new_score1):
        if self.validate_score(new_score0) and self.validate_score(new_score1):
            self.score0 = new_score0
            self.score1 = new_score1
        else:
            raise ValueError("Invalid score")

    def serialize(self):
        return {
            "player0": self.player0,
            "player1": self.player1,
            "score0": self.score0,
            "score1": self.score1,
        }

    @classmethod
    def deserialize(cls, data):
        return cls(
            data["player0"], data["player1"], data["score0"], data["score1"]
        )
