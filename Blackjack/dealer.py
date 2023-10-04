from player import Player

class Dealer(Player):
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