import random

from rules.legal_moves import legal_moves


class RandomAgent:

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

        return random.choice(moves)