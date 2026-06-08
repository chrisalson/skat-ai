from core.card import Card
from core.enums import Suit, Rank

from core.game_factory import create_game

from rules.game_result import (
    get_declarer_points
)

from rules.game_type import GameType


def test_declarer_points_include_skat():

    state = create_game(
        GameType.HEART
    )

    state.declarer = 0

    state.scores[0] = 40

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
        get_declarer_points(
            state
        )
        ==
        61
    )