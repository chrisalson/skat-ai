from core.card import Card
from core.enums import Suit, Rank

from rules.scoring import (
    calculate_trick_points
)


def test_trick_points():

    cards = [

        Card(
            Suit.CLUBS,
            Rank.ACE
        ),

        Card(
            Suit.CLUBS,
            Rank.TEN
        ),

        Card(
            Suit.CLUBS,
            Rank.KING
        )
    ]

    assert (
        calculate_trick_points(
            cards
        )
        ==
        25
    )