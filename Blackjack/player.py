class Player:
    '''
    Representation of a person playing Blackjack
    '''
    def __init__(self, deck):
        self._hand = sorted([deck.draw_card(), deck.draw_card()])
        self._deck = deck

    def hit(self):
        '''
        Add a card from the top of the deck list to the player's hand
        '''
        self._hand.append(self._deck.draw_card())
        self._hand.sort()

    def score(self) -> int:
        '''
        Returns the sum of all the cards in the player's hand
        '''
        sum = 0
        for card in self._hand:
            if card.rank == "Ace":
                if sum <= 10:
                    sum += 11
                else:
                    sum += 1
            else:
                try:
                    sum += int(card.rank)
                except ValueError:
                    sum += 10
        return sum

    def __str__(self):
        return '\n'.join(str(card) for card in self._hand) + f"\nScore: {self.score()}"