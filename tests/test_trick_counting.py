from core.game_factory import create_game
from core.game_logic import finish_trick

from core.card import Card
from core.enums import Suit, Rank

from rules.game_type import GameType


def test_trick_count_is_updated():

    state = create_game(
        GameType.HEART
    )

    state.current_trick = [

        (
            0,
            Card(
                Suit.CLUBS,
                Rank.ACE
            )
        ),

        (
            1,
            Card(
                Suit.CLUBS,
                Rank.TEN
            )
        ),

        (
            2,
            Card(
                Suit.HEARTS,
                Rank.SEVEN
            )
        )
    ]

    finish_trick(state)

    assert state.tricks_won[2] == 1