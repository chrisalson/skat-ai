from rules.trump import is_trump


def legal_moves(hand, lead_card, game_type):

    if lead_card is None:
        return hand

    lead_is_trump = is_trump(
        lead_card,
        game_type
    )

    matching_cards = []

    for card in hand:

        if lead_is_trump:

            if is_trump(card, game_type):
                matching_cards.append(card)

        else:

            if (
                not is_trump(card, game_type)
                and card.suit == lead_card.suit
            ):
                matching_cards.append(card)

    if matching_cards:
        return matching_cards

    return hand
