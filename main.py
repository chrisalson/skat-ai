from core.game_factory import create_game
from core.game_logic import play_trick
from agents.greedy_agent import GreedyAgent
from agents.random_agent import RandomAgent

from rules.game_type import GameType


def play_game():

    state = create_game(
        GameType.HEART
    )

    agents = [
        GreedyAgent(),
        RandomAgent(),
        RandomAgent()
    ]

    for trick in range(10):

        print(
            f"\n--- Stich {trick + 1} ---"
        )

        play_trick(
            state,
            agents
        )
    print("\n=== Endstand ===\n")

    print("Skat:")
    print(state.skat)
    print()

    for player in range(3):

        print(
            f"Spieler {player}: "
            f"{state.scores[player]} Augen"
        )

if __name__ == "__main__":
    play_game()