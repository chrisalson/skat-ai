from core.card import Card
from core.enums import Suit, Rank

from rules.game_type import GameType
from rules.legal_moves import legal_moves

def test_follow_suit():

    hand = [
        Card(Suit.SPADES, Rank.TEN),
        Card(Suit.HEARTS, Rank.KING)
    ]

    lead = Card(Suit.SPADES, Rank.ACE)

    moves = legal_moves(
        hand,
        lead,
        GameType.CLUB
    )

    assert len(moves) == 1
    assert moves[0].suit == Suit.SPADES

def test_can_play_anything_if_no_suit():

    hand = [
        Card(Suit.HEARTS, Rank.KING),
        Card(Suit.DIAMONDS, Rank.NINE)
    ]

    lead = Card(Suit.SPADES, Rank.ACE)

    moves = legal_moves(
        hand,
        lead,
        GameType.CLUB
    )

    assert len(moves) == 2

def test_follow_trump():

    hand = [
        Card(Suit.CLUBS, Rank.JACK),
        Card(Suit.SPADES, Rank.ACE)
    ]

    lead = Card(Suit.HEARTS, Rank.ACE)

    moves = legal_moves(
        hand,
        lead,
        GameType.HEART
    )

    assert len(moves) == 1
    assert moves[0].rank == Rank.JACK

