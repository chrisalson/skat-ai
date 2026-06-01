from core.card import Card
from core.enums import Suit, Rank

from rules.game_type import GameType
from rules.trump import is_trump


def test_jack_is_always_trump():

    card = Card(Suit.CLUBS, Rank.JACK)

    assert is_trump(card, GameType.HEART)


def test_heart_is_trump_in_heart_game():

    card = Card(Suit.HEARTS, Rank.ACE)

    assert is_trump(card, GameType.HEART)


def test_spade_is_not_trump_in_heart_game():

    card = Card(Suit.SPADES, Rank.ACE)

    assert not is_trump(card, GameType.HEART)


def test_no_trump_in_null():

    card = Card(Suit.HEARTS, Rank.ACE)

    assert not is_trump(card, GameType.NULL)