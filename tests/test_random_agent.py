from agents.random_agent import RandomAgent

from core.card import Card
from core.enums import Suit, Rank

from rules.game_type import GameType


def test_random_agent_returns_card():

    agent = RandomAgent()

    hand = [
        Card(Suit.CLUBS, Rank.ACE),
        Card(Suit.SPADES, Rank.TEN)
    ]

    card = agent.choose_move(
        hand,
        None,
        GameType.CLUB
    )

    assert card in hand