from rules.legal_moves import legal_moves
from rules.scoring import CARD_POINTS


class GreedyAgent:

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

        best_card = max(
            moves,
            key=lambda card:
            CARD_POINTS[
                card.rank
            ]
        )

        return best_card