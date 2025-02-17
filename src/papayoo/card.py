from abc import ABC, abstractmethod


class Card(ABC):
    def __init__(self, card_type: str, value: int):
        self.__type = card_type
        self.__value = value

    @abstractmethod
    def get_value_on_count(self) -> int:
        pass

    def __repr__(self) -> str:
        return f"Card({self.__type}, {self.__value})"

    def __str__(self) -> str:
        return f"Card({self.__type}, {self.__value})"


class Payoo(Card):
    def __init__(self, value: int):
        super().__init__(card_type="Payoo", value=value)

    def get_value_on_count(self) -> int:
        return self.__value


class ColorCard(Card):
    def __init__(self, card_type: str, value: int):
        super().__init__(card_type=card_type, value=value)
        self.__is_papayoo: bool = False

    def get_value_on_count(self) -> int:
        if self.__is_papayoo:
            return 40
        return self.__value

    def set_is_papayoo(self):
        self.__is_special = True
