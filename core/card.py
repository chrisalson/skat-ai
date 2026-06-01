from dataclasses import dataclass

from core.enums import Suit, Rank


@dataclass(frozen=True)
class Card:
    suit: Suit
    rank: Rank

    def __str__(self):
        return f"{self.rank.value} of {self.suit.value}"

    def __repr__(self):
        return str(self)