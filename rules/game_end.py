def is_game_over(state):

    return (
        len(
            state.played_cards
        )
        == 30
    )