from rules.card_comparator import beats


def determine_trick_winner(cards, game_type):
    """
    cards = Liste von 3 Karten
    Rückgabe = Index des Gewinners
    """

    winner_index = 0
    winning_card = cards[0]

    for i in range(1, len(cards)):

        if beats(cards[i], winning_card, game_type):
            winner_index = i
            winning_card = cards[i]

    return winner_index