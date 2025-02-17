import random

from src.papayoo.card import Card

class Player:
    def __init__(self, name: str):
        self.__name = name
        self.__hand: list[Card] | None = None

    def set_hand(self, cards: list[Card]):
        self.__hand = cards

    def get_hand(self) -> list[Card]:
        return self.__hand

    def give_card(self, nb_to_give: int) -> list[Card]:
        cards = random.choices(self.__hand, k=nb_to_give)
        self.set_hand(cards=[card for card in self.__hand if card not in cards])
        return cards

    def receive_card(self, cards: list[Card]):
        self.set_hand(cards=self.__hand + cards)

    def __repr__(self) -> str:
        return f"Player({self.__name})"

    def __str__(self) -> str:
        return f"Player({self.__name})"