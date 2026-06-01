import random

from core.card import Card
from core.enums import Suit, Rank


class Deck:

    def __init__(self):
        self.cards = [
            Card(suit, rank)
            for suit in Suit
            for rank in Rank
        ]

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()

    def size(self):
        return len(self.cards)