from core.card import Card
from core.enums import Suit, Rank

from rules.game_type import GameType
from rules.card_comparator import beats

def test_club_jack_beats_spade_jack():

    club_jack = Card(Suit.CLUBS, Rank.JACK)
    spade_jack = Card(Suit.SPADES, Rank.JACK)

    assert beats(
        club_jack,
        spade_jack,
        GameType.HEART
    )

def test_trump_beats_non_trump():

    heart_ace = Card(Suit.HEARTS, Rank.ACE)

    spade_ace = Card(Suit.SPADES, Rank.ACE)

    assert beats(
        heart_ace,
        spade_ace,
        GameType.HEART
    )

def test_ace_beats_ten():

    ace = Card(Suit.CLUBS, Rank.ACE)

    ten = Card(Suit.CLUBS, Rank.TEN)

    assert beats(
        ace,
        ten,
        GameType.CLUB
    )

def test_null_king_beats_ten():

    king = Card(Suit.CLUBS, Rank.KING)

    ten = Card(Suit.CLUBS, Rank.TEN)

    assert beats(
        king,
        ten,
        GameType.NULL
    )

