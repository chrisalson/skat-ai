from rules.legal_moves import legal_moves
from rules.scoring import CARD_POINTS
from rules.trump import is_trump


class TrumpAgent:

    def __init__(
        self,
        trump_bonus=15
    ):
        self.trump_bonus = (
            trump_bonus
        )

    def choose_move(
        self,
        hand,
        current_trick,
        game_type
    ):
        lead_card = None

        if current_trick:

            lead_card = (
                current_trick[0][1]
            )

        moves = legal_moves(
            hand,
            lead_card,
            game_type
        )

        def score(card):

            value = CARD_POINTS[
                card.rank
            ]

            if is_trump(
                card,
                game_type
            ):
                value += (
                    self.trump_bonus
                )

            return value

        return max(
            moves,
            key=score
        )