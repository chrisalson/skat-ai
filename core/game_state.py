from dataclasses import dataclass

from core.card import Card


@dataclass
class GameState:

    players_hands: list

    current_trick: list

    played_cards: list

    game_type: str