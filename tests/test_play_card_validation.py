from core.game_factory import create_game
from core.game_logic import play_card

from core.card import Card
from core.enums import Suit, Rank

from rules.game_type import GameType

import pytest


def test_illegal_move_raises_error():

    state = create_game(
        GameType.CLUB
    )

    spade_ace = Card(
        Suit.SPADES,
        Rank.ACE
    )

    heart_king = Card(
        Suit.HEARTS,
        Rank.KING
    )

    state.players_hands[0] = [
        spade_ace,
        heart_king
    ]

    state.current_trick = [
        (
            1,
            Card(
                Suit.SPADES,
                Rank.TEN
            )
        )
    ]

    with pytest.raises(
        ValueError
    ):
        play_card(
            state,
            0,
            heart_king
        )