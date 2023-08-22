# Names: Brandon W
# Date: 8/22/2023
# Desc: Random number guessing game


from random import randint
from check_input import get_int_range

def main() -> None:
    target: int = randint(1, 100)
    print("- Guessing Game -")
    guess: int = get_int_range("I'm thinking of a number. Make a guess (1-100): ", 1, 100)
    attempts: int = 1
    while target != guess:
        if not guess:
            guess = get_int_range("Guess again (1-100): ", 1, 100)
            attempts -= 1
        elif guess < target:
            guess = get_int_range("Too low! Guess again (1-100): ", 1, 100)
        elif guess > target:
            guess = get_int_range("Too high! Guess again (1-100): ", 1, 100)
        attempts += 1
            
    print(f"Correct! You got it in {attempts} tries")


main()