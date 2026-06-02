from core.deck import Deck
from core.dealer import deal_cards

def test_deal_creates_three_hands():

    deck = Deck()

    hands, skat = deal_cards(deck)

    assert len(hands) == 3

def test_each_player_gets_ten_cards():

    deck = Deck()

    hands, skat = deal_cards(deck)

    for hand in hands:
        assert len(hand) == 10

def test_skat_contains_two_cards():

    deck = Deck()

    hands, skat = deal_cards(deck)

    assert len(skat) == 2

def test_all_cards_are_dealt():

    deck = Deck()

    hands, skat = deal_cards(deck)

    total_cards = (
        len(hands[0])
        + len(hands[1])
        + len(hands[2])
        + len(skat)
    )

    assert total_cards == 32

