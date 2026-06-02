from core.deck import Deck


def deal_cards(deck: Deck):

    deck.shuffle()

    hands = [
        [],
        [],
        []
    ]

    # 3 Karten

    for player in range(3):
        for _ in range(3):
            hands[player].append(
                deck.draw()
            )

    # Skat

    skat = [
        deck.draw(),
        deck.draw()
    ]

    # 4 Karten

    for player in range(3):
        for _ in range(4):
            hands[player].append(
                deck.draw()
            )

    # 3 Karten

    for player in range(3):
        for _ in range(3):
            hands[player].append(
                deck.draw()
            )

    return hands, skat