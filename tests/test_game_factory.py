from core.game_factory import create_game

from rules.game_type import GameType


def test_create_game():

    state = create_game(
        GameType.CLUB
    )

    assert len(state.players_hands) == 3

    assert len(state.players_hands[0]) == 10

    assert len(state.players_hands[1]) == 10

    assert len(state.players_hands[2]) == 10

    assert len(state.skat) == 2

    assert state.current_player == 0