from rules.legal_moves import legal_moves
from rules.scoring import CARD_POINTS


class GreedyAgent:

    def choose_move(
        self,
        hand,
        lead_card,
        game_type
    ):

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