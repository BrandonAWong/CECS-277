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
    for i in range(2):
        print(f"Player #{i+1} = {player_points[i]}")
    if player_points[0] == player_points[1]:
        print("It's a tie!")
    elif player_points[0] > player_points[1]:
        print("Player #1 won!")
    else:
        print("Player #2 won!")

def main():
    print("- Ship, Captain, and Crew! -")
    players_points: list[int] = []
    for i in range(2):
        print(f"Player #{i+1}'s Turn")
        keep: list[int] = []
        for _ in range(3):
            roll: list[int] = [None] * (5 - len(keep))
            roll_dice(roll)
            display_dice("Roll", roll)
            # add to keep

            print(f"Keep = {keep}")
        players_points.append(roll[0] + roll[1])
    find_winner(players_points)



main()