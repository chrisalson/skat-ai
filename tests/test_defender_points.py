from core.game_factory import create_game

from rules.game_result import (
    get_defender_points
)

from rules.game_type import GameType


def test_defender_points():

    state = create_game(
        GameType.HEART
    )

    state.declarer = 0

    state.scores = [
        40,
        10,
        20
    ]

    assert (
        get_defender_points(
            state
        )
        ==
        30
    )