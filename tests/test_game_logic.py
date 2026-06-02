from core.game_factory import create_game
from core.game_logic import play_card

from rules.game_type import GameType


def test_play_card():

    state = create_game(
        GameType.CLUB
    )

    card = state.players_hands[0][0]

    hand_size = len(
        state.players_hands[0]
    )

    play_card(
        state,
        0,
        card
    )

    assert (
        len(state.players_hands[0])
        ==
        hand_size - 1
    )

    assert len(
        state.current_trick
    ) == 1