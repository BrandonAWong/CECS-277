from card import Card
from random import shuffle

class Deck:
    def __init__(self):
        self._cards: list[Card] = [Card(suit, rank) for suit in range(4) for rank in range(13)]

    def shuffle(self) -> None:
        shuffle(self._cards)

    def draw_card(self) -> Card:
        return self._cards.pop(0)
    
    def __len__(self):
        return len(self._cards)