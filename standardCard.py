class Card:

    def __init__(self, rank="Two", suit="Clubs"):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return f"Card('{self.rank}', '{self.suit}')"
        # return f"{self.rank} of {self.suit}"

    def __str__(self):
        return f"{self.rank} of {self.suit}"
