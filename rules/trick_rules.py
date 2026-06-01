from rules.trump import is_trump
from rules.card_comparator import beats


def determine_trick_winner(cards, game_type):

    winner_index = 0
    winning_card = cards[0]

    lead_card = cards[0]

    for i in range(1, len(cards)):

        current = cards[i]

        # Trumpf schlägt alles

        if (
            is_trump(current, game_type)
            and
            not is_trump(winning_card, game_type)
        ):
            winner_index = i
            winning_card = current
            continue

        # Nicht Trumpf

        if (
            not is_trump(current, game_type)
            and
            not is_trump(winning_card, game_type)
        ):

            if current.suit != lead_card.suit:
                continue

        if beats(
            current,
            winning_card,
            game_type
        ):
            winner_index = i
            winning_card = current

    return winner_index