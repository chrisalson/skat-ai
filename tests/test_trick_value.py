from core.card import Card
from core.enums import Suit, Rank

from rules.scoring import (
    calculate_trick_points
)


def test_trick_value():

    cards = [

        Card(
            Suit.CLUBS,
            Rank.ACE
        ),

        Card(
            Suit.CLUBS,
            Rank.TEN
        )
    ]

    assert (
        calculate_trick_points(
            cards
        )
        ==
        21
    )