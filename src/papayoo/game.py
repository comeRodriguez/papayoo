import itertools
import random

from src.papayoo.card import Payoo, ColorCard
from src.papayoo.player import Player

NUMBER_OF_CARDS_PER_PLAYER = {
    3: 20,
    4: 15,
    5: 12,
    6: 10,
}

class Game:
    def __init__(self, n_players: int):
        self.__n_players = n_players
        self.players = [Player(name=f"Player {i}") for i in range(1, n_players + 1)]
        self.cards = [
            ColorCard(ct, v) for ct, v in itertools.product(
                ["clubs", "spades", "diamonds", "hearts"], [i for i in range(1, 11)]
            )
        ] + [Payoo(i) for i in range(1, 21)]
        self.player_neighbors = {}

    def init_hands(self):
        remaining_cards = self.cards.copy()
        for player in self.players:
            cards = random.choices(remaining_cards, k=NUMBER_OF_CARDS_PER_PLAYER[self.__n_players])
            player.set_hand(cards=cards)
            remaining_cards = [card for card in remaining_cards if card not in cards]
