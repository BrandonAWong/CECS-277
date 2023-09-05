# Names: 
# Date: 8/24/2023
# Desc: Random number guessing game
from random import randint
from check_input import get_int_range

def main() -> None:
    target: int = randint(1, 100)
    print("- Guessing Game -")
    guess: int = get_int_range("I'm thinking of a number. Make a guess (1-100): ", 1, 100)
    attempts: int = 1
    while target != guess:
        if guess < target:
            print("Too low! ", end='')
        else:
            print("Too high! ", end='')
        guess = get_int_range("Guess again (1-100): ", 1, 100)
        attempts += 1
    print(f"Correct! You got it in {attempts} tries")


main()