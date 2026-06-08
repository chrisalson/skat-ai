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
from rules.game_result import (
    declarer_won,
    get_declarer_points
)


NUM_GAMES = 1000


def run_simulation():

    total_scores = [0, 0, 0]
    total_tricks = [0, 0, 0]

    declarer_wins = 0
    defender_wins = 0

    for _ in range(NUM_GAMES):

        state = create_game(
            GameType.HEART
        )

        agents = [
            CurrentWinnerAgent(),
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

        if declarer_won(state):

            declarer_wins += 1

        else:

            defender_wins += 1

        for player in range(3):

            if player == state.declarer:

                total_scores[player] += (
                    get_declarer_points(
                        state
                    )
                )

            else:

                total_scores[player] += (
                    state.scores[player]
                )

            total_tricks[player] += (
                state.tricks_won[player]
            )

    print("\n=== Spielgewinne ===\n")

    print(
        f"Alleinspieler: "
        f"{declarer_wins} "
        f"({declarer_wins / NUM_GAMES:.1%})"
    )

    print(
        f"Gegenspieler: "
        f"{defender_wins} "
        f"({defender_wins / NUM_GAMES:.1%})"
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