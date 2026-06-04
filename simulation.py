from core.game_factory import create_game
from core.game_logic import play_trick

from agents.greedy_agent import GreedyAgent
from agents.random_agent import RandomAgent
from agents.trump_agent import TrumpAgent
from agents.cheap_win_agent import CheapWinAgent
from agents.treasure_hunter_agent import TreasureHunterAgent
from agents.current_winner_agent import CurrentWinnerAgent
from agents.value_aware_agent import ValueAwareAgent

from rules.game_type import GameType
from rules.game_end import is_game_over


NUM_GAMES = 1000


def run_simulation():

    total_scores = [0, 0, 0]
    total_tricks = [0, 0, 0]

    for _ in range(NUM_GAMES):

        state = create_game(
            GameType.HEART
        )

        agents = [
            ValueAwareAgent(),
            RandomAgent(),
            RandomAgent()
        ]

        while not is_game_over(
        state
    ):

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