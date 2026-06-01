from core.enums import Rank, Suit
from rules.game_type import GameType


def is_trump(card, game_type):

    if game_type == GameType.NULL:
        return False

    if card.rank == Rank.JACK:
        return True

    if game_type == GameType.GRAND:
        return False

    trump_suit_map = {
        GameType.CLUB: Suit.CLUBS,
        GameType.SPADE: Suit.SPADES,
        GameType.HEART: Suit.HEARTS,
        GameType.DIAMOND: Suit.DIAMONDS,
    }

    return card.suit == trump_suit_map[game_type]