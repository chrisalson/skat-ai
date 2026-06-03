from agents.trump_agent import TrumpAgent

from core.card import Card
from core.enums import (
    Suit,
    Rank
)

from rules.game_type import GameType


def test_trump_agent_prefers_trump():

    agent = TrumpAgent()

    hand = [

        Card(
            Suit.SPADES,
            Rank.ACE
        ),

        Card(
            Suit.CLUBS,
            Rank.JACK
        )
    ]

    card = agent.choose_move(
        hand,
        None,
        GameType.HEART
    )

    assert (
        card.rank
        ==
        Rank.JACK
    )