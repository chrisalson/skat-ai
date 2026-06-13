from core.game_factory import create_game
from core.game_logic import play_trick

from agents.greedy_agent import GreedyAgent
from agents.random_agent import RandomAgent
from agents.trump_agent import TrumpAgent
from agents.cheap_win_agent import CheapWinAgent
from agents.treasure_hunter_agent import TreasureHunterAgent
from agents.current_winner_agent import CurrentWinnerAgent
from agents.value_aware_agent import ValueAwareAgent
from agents.greedy_value_agent import GreedyValueAgent

from rules.game_type import GameType
from rules.game_end import is_game_over
from rules.game_result import (
    declarer_won,
    get_declarer_points
)


NUM_GAMES = 1000


def run_simulation():

    total_tricks_played = 0

    agent_scores = {}
    agent_tricks = {}
    agent_games = {}

    declarer_wins = 0
    defender_wins = 0

    for game_number in range(NUM_GAMES):

        state = create_game(
            GameType.HEART
        )

        all_agents = [
            ValueAwareAgent(),
            GreedyValueAgent(),
            RandomAgent()
        ]

        for agent in all_agents:

            if agent.name not in agent_scores:

                agent_scores[
                    agent.name
                ] = 0

                agent_tricks[
                    agent.name
                ] = 0

                agent_games[
                    agent.name
                ] = 0

        for agent in all_agents:

            agent_games[
                agent.name
            ] += 1

        rotation = (
            game_number
            % len(all_agents)
        )

        agents = (
            all_agents[rotation:]
            +
            all_agents[:rotation]
        )

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

        total_tricks_played += (
            sum(
                state.tricks_won
            )
        )

        for player in range(3):

            agent_name = (
                agents[player].name
            )

            if player == state.declarer:

                agent_scores[
                    agent_name
                ] += (
                    get_declarer_points(
                        state
                    )
                )

            else:

                agent_scores[
                    agent_name
                ] += (
                    state.scores[player]
                )

            agent_tricks[
                agent_name
            ] += (
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

    print("\n=== Debug ===\n")

    print(
        f"Gespielte Stiche: "
        f"{total_tricks_played}"
    )

    print("\n=== Agent Games ===\n")

    for agent_name in agent_games:

        print(
            f"{agent_name}: "
            f"{agent_games[agent_name]}"
        )

    print("\n=== Agenten ===\n")

    for agent_name in agent_scores:

        average_score = (
            agent_scores[agent_name]
            / NUM_GAMES
        )

        average_tricks = (
            agent_tricks[agent_name]
            / NUM_GAMES
        )

        print(
            f"DEBUG {agent_name}: "
            f"Tricks={agent_tricks[agent_name]}"
        )

        print(
            f"{agent_name}: "
            f"{average_score:.2f} Augen | "
            f"{average_tricks:.2f} Stiche"
        )


if __name__ == "__main__":
    run_simulation()