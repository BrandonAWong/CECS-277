# Names: Trung Ho, Dylan Garvey, Brandon Wong
# Date: 10/10/2023
# Desc: CLI battle between player and 3 CPU dragons. Each entity has a basic and special attack to choose from.


from hero import Hero
from dragon import Dragon
from fire_dragon import FireDragon
from flying_dragon import FlyingDragon
from check_input import get_int_range
from random import choice


def main():
    name: str = input("What is your name, challenger?\n")
    print(f"Welcome to dragon training, {name}\n"
          "You must defeat 3 dragons.")
    
    player: Hero = Hero(name, 50)
    dragons: list = [Dragon("Deadly Nadder", 10),
                     FireDragon("Gronkle", 15,3 ),
                     FlyingDragon("Timberjack", 20, 3)]
    while dragons and player.hp > 0:
        print(f"\n{player}")
        [print(f"{i+1}. {d}") for i, d in enumerate(dragons)]
        d_choice: int = get_int_range("Choose a dragon to attack: ", 1, len(dragons)) - 1
        atk_choice: int = get_int_range("\nAttack with:\n1. Sword (2 D6)\n"
                                        "2. Arrow (1 D12)\nEnter weapon: ", 1, 2)
        if atk_choice == 1:
            print(f"\n{player.basic_attack(dragons[d_choice])}")
        else:
            print(f"\n{player.special_attack(dragons[d_choice])}")
        if dragons[d_choice].hp <= 0:
            dragons.pop(d_choice)
        
        if dragons:
            d_atk = choice(dragons)
            if choice([False, True]):
                print(d_atk.basic_attack(player))
            else:
                print(d_atk.special_attack(player))
    
    if not dragons:
        print("\nCongratulations! You have defeated all 3 dragons, you have passed the trials.")
    else:
        print(f"\nYou knocked out. {len(dragons)} remain.")

main()