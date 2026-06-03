from core.card import Card
from core.enums import Suit, Rank

from rules.trick_rules import (
    determine_trick_winner
)
from rules.game_type import GameType


def test_current_winning_card():

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

    winner_index = determine_trick_winner(
        cards,
        GameType.CLUB
    )

    winning_card = cards[
        winner_index
    ]

    assert (
        winning_card.rank
        ==
        Rank.ACE
    )