from core.card import Card
from core.enums import Suit, Rank

from rules.trick_rules import (
    determine_trick_winner
)
from rules.game_type import GameType


def test_winner_with_two_cards():

    cards = [

        Card(
            Suit.CLUBS,
            Rank.SEVEN
        ),

        Card(
            Suit.CLUBS,
            Rank.ACE
        )
    ]

    winner = determine_trick_winner(
        cards,
        GameType.CLUB
    )

    assert winner == 1