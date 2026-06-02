from core.game_factory import create_game
from core.game_logic import play_card

from rules.game_type import GameType


def test_trick_tracks_player_and_card():

    state = create_game(
        GameType.CLUB
    )

    card = state.players_hands[0][0]

    play_card(
        state,
        0,
        card
    )

    player, played_card = state.current_trick[0]

    assert player == 0

    assert played_card == card