class Match:
    def __init__(self, player1, player2, score1, score2):
        self.pairs = ([player1, score1], [player2, score2])

    def __str__(self):
        return (
            f"player {self.pairs[0][0]}: vs player {self.pairs[0][0]}\n"
            f"result {self.pairs[0][1]} / {self.pairs[1][1]}"
        )

    @property
    def pair_of_players(self):
        return f"player {self.pairs[0][0]} vs player{self.pairs[1][0]}"

    def update_score(self, new_score1, new_score2):
        self.pairs[0][1] = new_score1
        self.pairs[1][1] = new_score2

    def serialized_match(self):
        return {"pairs": self.pairs}

    def deserialized_match(self, serialized_match):
        player1 = serialized_match["pairs"][0][0]
        player2 = serialized_match["pairs"][1][0]
        score1 = serialized_match["pairs"][0][1]
        score2 = serialized_match["pairs"][1][1]
        return Match(player1, player2, score1, score2)
