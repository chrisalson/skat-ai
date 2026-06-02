from core.enums import Rank


CARD_POINTS = {

    Rank.ACE: 11,

    Rank.TEN: 10,

    Rank.KING: 4,

    Rank.QUEEN: 3,

    Rank.JACK: 2,

    Rank.NINE: 0,

    Rank.EIGHT: 0,

    Rank.SEVEN: 0
}


def calculate_trick_points(cards):

    total = 0

    for card in cards:

        total += CARD_POINTS[
            card.rank
        ]

    return total