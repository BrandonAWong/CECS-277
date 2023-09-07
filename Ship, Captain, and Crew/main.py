# Names: Trung Ho & Brandon Wong
# Date: 9/5/2023
# Desc: Basic CLI game of Ship, Captain, and Crew! 

from random import randint

def roll_dice(dice: list[int]) -> None:
    '''
    Randomize values of each dice and sorts them in descending order.
    '''
    dice[:] = sorted([randint(1,6) for _ in dice], reverse=True)

def display_dice(name: str, dice: list[int]) -> None:
    '''
    Displays the values of the dice.
    ''' 
    print(f"{name} = {' '.join([str(die) for die in dice])}")

def find_winner(player_points: list[int]):
    '''
    Displays both players' points and displays who won. If scores are the same, display tie.
    '''
    print("Score:")
    for i in range(2):
        print(f"Player #{i+1} = {player_points[i]}")
    if player_points[0] == player_points[1]:
        print("It's a tie!")
    elif player_points[0] > player_points[1]:
        print("Player #1 won!")
    else:
        print("Player #2 won!")

def find_keep(dice: list[int], keep: list[int]) -> None:
    '''
    Finds the dice to keep and not to reroll.
    '''
    wants = [6, 5, 4]
    for i, want in enumerate(wants):
        if want in dice and len(keep) == i:
            keep.append(want)
            dice.remove(want)
            if want == 6:
                print("Yo ho ho! Ye secured a ship!")
            elif want == 5:
                print("Shiver me timbers! A Capt'n!")
            elif want == 4:
                print("Ye bribed a crew with Grog!") 

def play_again(turn: int) -> bool:
    '''
    Checks if player wants to continue rolling.
    '''
    if turn < 2:
        if input("Roll again? ").lower() != 'y':
            return False
    return True

def main() -> None:
    print("- Ship, Captain, and Crew! -\n")
    players_points: list[int] = []
    for i in range(2):
        print(f"Player #{i+1}'s Turn")
        keep: list[int] = []
        for turn in range(3):
            roll: list[int] = [None] * (5 - len(keep))
            roll_dice(roll)
            display_dice("Roll", roll)
            find_keep(roll, keep)
            display_dice("Keep", keep)
            display_dice("Cargo", roll) if len(keep) == 3 else print()
            if not play_again(turn):
                break
        if len(keep) == 3:
            players_points.append(sum(roll))
        else:
            players_points.append(0)
        print(f"Player #{i+1} points = {players_points[i]}\n")
    find_winner(players_points)


main()