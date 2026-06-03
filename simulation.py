from core.game_factory import create_game
from core.game_logic import play_trick

from agents.greedy_agent import GreedyAgent
from agents.random_agent import RandomAgent
from agents.trump_agent import TrumpAgent

from rules.game_type import GameType


NUM_GAMES = 1000


def run_simulation():

    total_scores = [0, 0, 0]
    total_tricks = [0, 0, 0]

    for _ in range(NUM_GAMES):

        state = create_game(
            GameType.HEART
        )

        agents = [
            TrumpAgent(2),
            RandomAgent(),
            RandomAgent()
        ]

        for _ in range(10):

            play_trick(
                state,
                agents
            )

        for player in range(3):

            total_scores[player] += (
                state.scores[player]
            )

            total_tricks[player] += (
                state.tricks_won[player]
            )

    print("\n=== Ergebnisse ===\n")

    for player in range(3):

        average_score = (
            total_scores[player]
            / NUM_GAMES
        )

        average_tricks = (
            total_tricks[player]
            / NUM_GAMES
        )

        print(
            f"Spieler {player}: "
            f"{average_score:.2f} Augen | "
            f"{average_tricks:.2f} Stiche"
        )

if __name__ == "__main__":
    run_simulation()