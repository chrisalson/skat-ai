from core.card import Card
from core.enums import Suit, Rank

from rules.game_type import GameType
from rules.trick_rules import determine_trick_winner

def test_club_jack_wins():

    cards = [
        Card(Suit.SPADES, Rank.ACE),
        Card(Suit.CLUBS, Rank.JACK),
        Card(Suit.HEARTS, Rank.ACE)
    ]

    winner = determine_trick_winner(
        cards,
        GameType.HEART
    )

    assert winner == 1

def test_ace_beats_ten():

    cards = [
        Card(Suit.CLUBS, Rank.TEN),
        Card(Suit.CLUBS, Rank.ACE),
        Card(Suit.CLUBS, Rank.KING)
    ]

    winner = determine_trick_winner(
        cards,
        GameType.CLUB
    )

    assert winner == 1

