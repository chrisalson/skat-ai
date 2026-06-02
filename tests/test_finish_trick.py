from core.game_factory import create_game
from core.game_logic import finish_trick

from core.card import Card
from core.enums import Suit, Rank

from rules.game_type import GameType


def test_finish_trick():

    state = create_game(
        GameType.HEART
    )

    state.current_trick = [

        (
            0,
            Card(
                Suit.SPADES,
                Rank.ACE
            )
        ),

        (
            1,
            Card(
                Suit.SPADES,
                Rank.TEN
            )
        ),

        (
            2,
            Card(
                Suit.CLUBS,
                Rank.JACK
            )
        )
    ]

    finish_trick(state)

    assert len(
        state.current_trick
    ) == 0

    assert len(
        state.played_cards
    ) == 3

    assert (
        state.current_player
        ==
        2
    )