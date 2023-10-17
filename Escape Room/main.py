# Name: Brandon Wong
# Date: 10/17/2023
# Desc: CLI game where you are given 3 random doors and you must open them to escape.


from random import choice
from check_input import get_int_range
from basic_door import BasicDoor
from locked_door import LockedDoor
from deadbolt_door import DeadboltDoor
from combo_door import ComboDoor
from code_door import CodeDoor


def open_door(door) -> None:
    """
    Opens the door and displays information about it.
    Asks the user what to do in order to open the door.
    """
    print(door.examine_door())
    while not door.is_unlocked():
        choice = get_int_range(door.menu_options(), 1, door.get_menu_max())
        print(door.attempt(choice))
        if not door.is_unlocked():
            print(door.clue())
    print(door.success())


def main():
    print("Welcome to the Escape Room. You must unlock 3 doors to escape...\n")
    door_options = (BasicDoor(), LockedDoor(), DeadboltDoor(), ComboDoor(), CodeDoor())
    doors = [choice(door_options) for _ in range(3)]
    for d in doors:
        open_door(d)
    print("Congratulations! You escaped... this time.")

main()