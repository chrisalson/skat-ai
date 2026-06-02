from rules.trick_rules import determine_trick_winner

def play_card(
    state,
    player_index,
    card
):

    state.players_hands[player_index].remove(
        card
    )

    state.current_trick.append(
    (
        player_index,
        card
    )
)

    state.current_player = (
        state.current_player + 1
    ) % 3

def finish_trick(state):

    if len(state.current_trick) != 3:
        return

    cards = [
        card
        for _, card
        in state.current_trick
    ]

    winner_index = determine_trick_winner(
        cards,
        state.game_type
    )

    winning_player = (
        state.current_trick[winner_index][0]
    )

    for _, card in state.current_trick:
        state.played_cards.append(card)

    state.current_trick.clear()

    state.current_player = winning_player