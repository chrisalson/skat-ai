from rules.legal_moves import legal_moves
from rules.trick_rules import determine_trick_winner


def play_card(
    state,
    player_index,
    card
):

    lead_card = None

    if state.current_trick:

        lead_card = (
            state.current_trick[0][1]
        )

    allowed_moves = legal_moves(
        state.players_hands[player_index],
        lead_card,
        state.game_type
    )

    if card not in allowed_moves:
        raise ValueError(
            "Illegal move"
        )

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

def play_trick(state, agents):

    lead_card = None

    start_player = state.current_player

    for offset in range(3):

        player = (
            start_player + offset
        ) % 3

        hand = state.players_hands[player]

        card = agents[player].choose_move(
            hand,
            lead_card,
            state.game_type
        )

        print(
            f"Spieler {player}: {card}"
        )

        play_card(
            state,
            player,
            card
        )

        if lead_card is None:
            lead_card = card

    finish_trick(state)

    print(
        f"Gewinner: Spieler {state.current_player}"
    )