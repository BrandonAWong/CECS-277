from player import Player

class Dealer(Player):
    '''
    The CPU that the player will play against.
    This function will continuosuly run until the dealer decides to stay.
    '''
    def play(self):
        while True:
            print("\nDealer's Cards:")
            print(str(self))
            if self.score() >= 17:
                break
            print("Dealer Hits!")
            self.hit()
        if self.score() >= 22:
            print("Bust!")