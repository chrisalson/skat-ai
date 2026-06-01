from dataclasses import dataclass

from core.card import Card


@dataclass
class Trick:

    cards: list[Card]

    def add_card(self, card):
        self.cards.append(card)

    @property
    def lead_card(self):
        return self.cards[0]