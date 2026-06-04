from core.deck import Deck
from core.dealer import deal_cards
from core.game_state import GameState


def create_game(game_type):

    deck = Deck()

    hands, skat = deal_cards(deck)

    return GameState(
        players_hands=hands,
        skat=skat,
        current_trick=[],
        played_cards=[],
        game_type=game_type,
        current_player=0,
        scores=[0, 0, 0],
        tricks_won=[0, 0, 0],
        declarer=0
    )