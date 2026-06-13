from rules.legal_moves import legal_moves
from rules.card_comparator import beats
from rules.trick_rules import (
    determine_trick_winner
)
from rules.scoring import (
    CARD_POINTS,
    calculate_trick_points
)


class GreedyValueAgent:
    
    name = "GreedyValue"

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

        if not current_trick:

            return max(
                moves,
                key=lambda card:
                CARD_POINTS[
                    card.rank
                ]
            )

        cards = [
            card
            for _, card
            in current_trick
        ]

        trick_value = (
            calculate_trick_points(
                cards
            )
        )

        winner_index = (
            determine_trick_winner(
                cards,
                game_type
            )
        )

        current_winner = cards[
            winner_index
        ]

        winning_moves = []

        for card in moves:

            if beats(
                card,
                current_winner,
                game_type
            ):
                winning_moves.append(
                    card
                )

        if winning_moves:

            return max(
                winning_moves,
                key=lambda card:
                CARD_POINTS[
                    card.rank
                ]
            )

        return max(
            moves,
            key=lambda card:
            CARD_POINTS[
                card.rank
            ]
        )