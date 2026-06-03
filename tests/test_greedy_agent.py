from agents.greedy_agent import GreedyAgent

from core.card import Card
from core.enums import (
    Suit,
    Rank
)

from rules.game_type import GameType


def test_greedy_agent_plays_highest_value_card():

    agent = GreedyAgent()

    hand = [

        Card(
            Suit.CLUBS,
            Rank.SEVEN
        ),

        Card(
            Suit.CLUBS,
            Rank.TEN
        ),

        Card(
            Suit.CLUBS,
            Rank.ACE
        )
    ]

    card = agent.choose_move(
        hand,
        None,
        GameType.CLUB
    )

    assert (
        card.rank
        ==
        Rank.ACE
    )