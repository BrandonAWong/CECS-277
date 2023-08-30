from random import randint

def get_users_bet(money: int) -> int:
    print(f'You have ${money}.')
    return get_input_range("How much you wana bet? ", 1, money)

def get_users_choice() -> int:
    print_cards(1, 2, 3)
    return get_input_range("Find the queen: ", 1, 3)

def display_queen_loc(queen_loc: int) -> None:
    a, b, c = ['K' if i != queen_loc else 'Q' for i in range(3)]
    print_cards(a, b, c)

def get_input_range(prompt: str, low: int, high: int) -> int:
    while True:
        try:
            n: int = int(input(prompt))
            if low <= n <= high:
                return n
            else:
                print(f"Invalid input - should be within range {low}-{high}")
        except ValueError:
            print("Invalid input - shuould be an integer.")

def print_cards(a: str | int, b: str | int, c: str | int):
    midline: str = f"|  {a}  | |  {b}  | |  {c}  |\n"
    print(
         "+-----+ +-----+ +-----+\n"
         "|     | |     | |     |\n" 
                + midline + 
         "|     | |     | |     |\n"
         "+-----+ +-----+ +-----+"
    )

def main() -> None:
    print("-Three card Monte-\n"
          "Find the queen to double your bet!\n")
    money: int = 100
    while money > 0:
        bet: int = get_users_bet(money)
        money -= bet
        guess: int = get_users_choice() - 1
        loc: int = randint(0, 2)
        display_queen_loc(loc)
        if guess == loc:
            print("You got lucky this time...")
            money += 2 * bet
        else:
            print("Sorry... you lose.")
        if money <= 0 or input("Play again? (Y/N): ").lower() != 'y':
            break

    if money <= 0:
          print("You're out of money. Beat it loser!")
    else:
        print(f"Bye 👋\nYou are leaving with ${money}.")
    
main()