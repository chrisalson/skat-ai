from rules.legal_moves import legal_moves
from rules.scoring import CARD_POINTS
from rules.card_comparator import beats


class CheapWinAgent:

    def choose_move(
        self,
        hand,
        current_trick,
        game_type
    ):

        moves = legal_moves(
            hand,
            lead_card,
            game_type
        )

        # Ausspiel
        if lead_card is None:

            return min(
                moves,
                key=lambda card:
                CARD_POINTS[
                    card.rank
                ]
            )

        winning_moves = []

        for card in moves:

            if beats(
                card,
                lead_card,
                game_type
            ):
                winning_moves.append(
                    card
                )

        if winning_moves:

            return min(
                winning_moves,
                key=lambda card:
                CARD_POINTS[
                    card.rank
                ]
            )

        return min(
            moves,
            key=lambda card:
            CARD_POINTS[
                card.rank
            ]
        )