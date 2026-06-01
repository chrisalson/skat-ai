from core.enums import Rank


TRUMP_ORDER = {
    Rank.ACE: 7,
    Rank.TEN: 6,
    Rank.KING: 5,
    Rank.QUEEN: 4,
    Rank.NINE: 3,
    Rank.EIGHT: 2,
    Rank.SEVEN: 1
}


NORMAL_ORDER = {
    Rank.ACE: 7,
    Rank.TEN: 6,
    Rank.KING: 5,
    Rank.QUEEN: 4,
    Rank.NINE: 3,
    Rank.EIGHT: 2,
    Rank.SEVEN: 1
}


NULL_ORDER = {
    Rank.ACE: 8,
    Rank.KING: 7,
    Rank.QUEEN: 6,
    Rank.JACK: 5,
    Rank.TEN: 4,
    Rank.NINE: 3,
    Rank.EIGHT: 2,
    Rank.SEVEN: 1
}