from core.card import Card
from core.enums import Suit, Rank
from core.deck import Deck

def test_create_card():
    card = Card(Suit.HEARTS, Rank.ACE)

    assert card.suit == Suit.HEARTS
    assert card.rank == Rank.ACE
    from core.deck import Deck


def test_deck_contains_32_cards():

    deck = Deck()

    assert deck.size() == 32

def test_draw_reduces_deck_size():

    deck = Deck()

    deck.draw()

    assert deck.size() == 31

def test_all_cards_are_unique():

    deck = Deck()

    assert len(deck.cards) == len(set(deck.cards))