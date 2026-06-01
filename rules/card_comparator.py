from core.enums import Rank, Suit

from rules.game_type import GameType
from rules.trump import is_trump
from rules.card_order import (
    TRUMP_ORDER,
    NORMAL_ORDER,
    NULL_ORDER
)
JACK_ORDER = {
    Suit.CLUBS: 4,
    Suit.SPADES: 3,
    Suit.HEARTS: 2,
    Suit.DIAMONDS: 1
}
def beats(card_a, card_b, game_type):

    if game_type == GameType.NULL:
        return NULL_ORDER[card_a.rank] > NULL_ORDER[card_b.rank]

    a_trump = is_trump(card_a, game_type)
    b_trump = is_trump(card_b, game_type)

    # Trumpf schlägt Nicht-Trumpf
    if a_trump and not b_trump:
        return True

    if b_trump and not a_trump:
        return False

    # Beide Trumpf
    if a_trump and b_trump:

        if (
            card_a.rank == Rank.JACK
            and card_b.rank == Rank.JACK
        ):
            return (
                JACK_ORDER[card_a.suit]
                >
                JACK_ORDER[card_b.suit]
            )

        if card_a.rank == Rank.JACK:
            return True

        if card_b.rank == Rank.JACK:
            return False

        return (
            TRUMP_ORDER[card_a.rank]
            >
            TRUMP_ORDER[card_b.rank]
        )

    # Normale Karten

    return (
        NORMAL_ORDER[card_a.rank]
        >
        NORMAL_ORDER[card_b.rank]
    )
