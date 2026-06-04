from core.game_factory import create_game

from rules.game_end import (
    is_game_over
)
from rules.game_type import GameType


def test_game_not_over():

    state = create_game(
        GameType.HEART
    )

    assert not is_game_over(
        state
    )


def test_game_over():

    state = create_game(
        GameType.HEART
    )

    state.played_cards = [None] * 30

    assert is_game_over(
        state
    )