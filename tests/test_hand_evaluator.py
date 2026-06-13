from core.card import Card
from core.enums import (
    Suit,
    Rank
)

from evaluation.hand_evaluator import (
    evaluate_hand
)


def test_evaluate_hand():

    hand = [

        Card(
            Suit.CLUBS,
            Rank.ACE
        ),

        Card(
            Suit.SPADES,
            Rank.ACE
        ),

        Card(
            Suit.HEARTS,
            Rank.TEN
        ),

        Card(
            Suit.DIAMONDS,
            Rank.JACK
        ),

        Card(
            Suit.CLUBS,
            Rank.JACK
        )
    ]

    result = evaluate_hand(
        hand
    )

    assert result == {
        "aces": 2,
        "tens": 1,
        "jacks": 2,
    }