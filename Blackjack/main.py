# Names: Brandon Wong & Trung Ho
# Date: 10/03/2023
# Desc: CLI Blackjack with player vs CPU


from deck import Deck
from player import Player
from dealer import Dealer
from check_input import get_int_range, get_yes_no

def display_winner(pScore: int, dScore:int, points: list[int]) -> None:
    '''
    Determines and prints the winner of the Blackjack game
    '''
    if pScore > dScore and pScore < 22 or dScore >= 22 and pScore < 22:
        print("\nPlayer wins.")
        points[0] += 1
    elif pScore < dScore and dScore < 22 or pScore >= 22 and dScore < 22:
        print("\nDealer wins.")
        points[1] += 1
    else:
        print("\nTie.")
    print(f"Player's points: {points[0]}\nDealer's points: {points[1]}")


def main():
    print("- Blackjack -")
    deck: Deck = Deck()
    deck.shuffle()
    points: list[int] = [0, 0]
    while True:
        if len(deck) < 15:
            deck = Deck()
            deck.shuffle()
        player: Player = Player(deck)
        while True:
            print(f"\nPlayer's Cards:\n{player}")
            if player.score() >= 22:
                print("Bust!")
                break
            choice: int = get_int_range("1. Hit\n2. Stay\nEnter choice: ", 1, 2)
            if choice == 2:
                break
            player.hit()

        dealer: Dealer = Dealer(deck)
        dealer.play()

        display_winner(player.score(), dealer.score(), points)

        if not get_yes_no("Play again? (Y/N): "):
            break

main()