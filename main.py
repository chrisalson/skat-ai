from core.game_factory import create_game
from core.game_logic import play_trick

from agents.random_agent import RandomAgent

from rules.game_type import GameType


def play_game():

    state = create_game(
        GameType.HEART
    )

    agents = [
        RandomAgent(),
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


if __name__ == "__main__":
    play_game()