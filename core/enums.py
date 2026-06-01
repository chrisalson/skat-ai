from enum import Enum


class Suit(Enum):
    CLUBS = "Clubs"
    SPADES = "Spades"
    HEARTS = "Hearts"
    DIAMONDS = "Diamonds"


class Rank(Enum):
    SEVEN = "7"
    EIGHT = "8"
    NINE = "9"
    JACK = "J"
    QUEEN = "Q"
    KING = "K"
    TEN = "10"
    ACE = "A"