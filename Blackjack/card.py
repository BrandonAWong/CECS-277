class Card:
    '''
    Representation of a playing card
    '''
    def __init__(self, suit: int, rank: int):
        self._suit: int = suit
        self._rank: int = rank

    @property
    def rank(self):
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10',
                 "Jack", "Queen", "King", "Ace"]
        return ranks[self._rank]

    def __str__(self):
        suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        return f"{self.rank} of {suits[self._suit]}"
    
    def __lt__(self, other):
        return self._rank < other._rank