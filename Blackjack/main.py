from deck import Deck
from player import Player
from dealer import Dealer
from check_input import get_int_range, get_yes_no

def display_winner(pScore: int, dScore:int, points: list[int]) -> None:
    if pScore > dScore and pScore < 22:
        print("Player wins.")
        points[0] += 1
    elif pScore < dScore and dScore < 22:
        print("Dealer wins.")
        points[1] += 1
    else:
        print("Tie. Nobody wins.")
    print(f"Player's points: {pScore}\nDealer's points: {dScore}")


def main():
    print("- Blackjack -")
    deck: Deck = Deck()
    deck.shuffle()

    while True:
        if len(deck) < 15:
            deck = Deck()
            deck.shuffle()
        player: Player = Player(deck)
        while player.score() > 22:
            print("\nPlayer's Cards:")
            print(player)
            choice: int = get_int_range("1. Hit\n2. Stay\nEnter choice: ")
            if choice == 2:
                break
        if player.score() >= 22:
            print("Bust!")

        dealer: Dealer = Dealer(deck)
        dealer.play()
main()