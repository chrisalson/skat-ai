from core.game_factory import create_game

from rules.game_result import (
    defenders_won
)

from rules.game_type import GameType


def test_defenders_win():

    state = create_game(
        GameType.HEART
    )

    state.declarer = 0

    state.scores = [
        50,
        30,
        30
    ]

    assert defenders_won(
        state
    )