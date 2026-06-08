from core.card import Card
from core.enums import Suit, Rank

from core.game_factory import create_game
from rules.game_result import (
    get_skat_points
)
from rules.game_type import GameType


def test_skat_points():

    state = create_game(
        GameType.HEART
    )

    state.skat = [

        Card(
            Suit.CLUBS,
            Rank.ACE
        ),

        Card(
            Suit.HEARTS,
            Rank.TEN
        )
    ]

    assert (
        get_skat_points(
            state
        )
        ==
        21
    )