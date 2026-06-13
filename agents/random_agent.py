import random

from rules.legal_moves import legal_moves


class RandomAgent:

    name = "Random"

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

        return random.choice(
            moves
        )