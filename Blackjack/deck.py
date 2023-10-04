from card import Card
from random import shuffle

class Deck:
    '''
    Initializes with 52 cards like a real deck
    '''
    def __init__(self):
        self._cards: list[Card] = [Card(suit, rank) for suit in range(4) for rank in range(13)]

    def shuffle(self) -> None:
        '''
        Shuffles the card list and randomizes the location of each card
        '''
        shuffle(self._cards)

    def draw_card(self) -> Card:
        '''
        Removes and returns the card on the first index of the card list
        '''
        return self._cards.pop(0)
    
    def __len__(self):
        return len(self._cards)