from rules.legal_moves import legal_moves
from rules.card_comparator import beats
from rules.scoring import CARD_POINTS


class TreasureHunterAgent:

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

        # Ausspiel:
        if lead_card is None:

            return min(
                moves,
                key=lambda card:
                CARD_POINTS[
                    card.rank
                ]
            )

        current_value = CARD_POINTS[
            lead_card.rank
        ]

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

        # Nur bei wertvollen Stichen kämpfen
        if (
            current_value >= 10
            and winning_moves
        ):

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