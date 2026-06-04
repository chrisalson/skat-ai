from core.game_factory import create_game

from rules.game_result import (
    declarer_won
)
from rules.game_type import GameType


def test_declarer_wins():

    state = create_game(
        GameType.HEART
    )

    state.scores[0] = 61

    assert declarer_won(
        state
    )