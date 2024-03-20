class Match:
    def __init__(self, player1, player2, score1, score2):
        self.player1 = player1
        self.player2 = player2
        self.score1 = score1
        self.score2 = score2

    def __str__(self):
        result = f"{self.player1} vs {self.player2}\n"
        if self.score1 == self.score2:
            result += "Result: Draw"
        else:
            winner = (
                self.player1 if self.score1 > self.score2 else self.player2
            )
            result += f"Winner: {winner}"
        return result

    @staticmethod
    def validate_score(score):
        return 0 <= score <= 1

    @property
    def pair_of_players(self):
        return f"{self.player1} vs {self.player2}"

    def update_score(self, new_score1, new_score2):
        if self.validate_score(new_score1) and self.validate_score(new_score2):
            self.score1 = new_score1
            self.score2 = new_score2
        else:
            raise ValueError("Invalid score")

    def serialize(self):
        return {
            "player1": self.player1,
            "player2": self.player2,
            "score1": self.score1,
            "score2": self.score2,
        }

    @classmethod
    def deserialize(cls, data):
        return cls(
            data["player1"], data["player2"], data["score1"], data["score2"]
        )
