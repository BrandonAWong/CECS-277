# Names: 


from hero import Hero
from enemy import Enemy
from map import Map
from check_input import get_int_range
from random import choice


def main():
    player: Hero = Hero(input("What is your name, traveler? "))
    dungeon: Map = Map()
    while player.hp:
        dungeon.reveal(player.loc)
        print(f"{player}\n{dungeon.show_map(player.loc)}\n"
              "\n1. Go North\n2. Go South\n3. Go East\n4. Go West\n5. Quit")
        p_choice: int = get_int_range("Enter choice: ", 1, 5)

        if p_choice == 1:
            tile: chr = player.go_north()
        elif p_choice == 2:
            tile: chr = player.go_south()
        elif p_choice == 3:
            tile: chr = player.go_east()
        elif p_choice == 4:
            tile: chr = player.go_west()
        elif p_choice == 5:
            break

        if tile == "m":
            monster: Enemy = Enemy()
            print(f"You encounter a {monster}")
            while monster.hp and player.hp:
                print(f"1. Attack {monster.name}\n2. Run Away")
                battle_choice: int = get_int_range("Enter choice: ", 1, 2)
                if battle_choice == 1:
                    print(player.attack(monster))
                    if monster.hp:
                        print(monster.attack(player))
                elif battle_choice == 2:
                    dungeon.reveal(player.loc)
                    print("You ran away!\n")
                    while choice([player.go_north, player.go_south, player.go_east, player.go_west])() == "o":
                        continue
                    break
            if not monster.hp:
                dungeon.remove_at_loc(player.loc)
                print(f"You have slain a {monster.name}\n")
        elif tile == "i":
            if player.hp < 25:
                player.heal()
                dungeon.remove_at_loc(player.loc)
                print("You found a Health Potion! You drink it to restore your health.\n")
            else:
                print("You found a Health Potion! You are at full health. You decide to save the potion for later.\n")
        elif tile == "n":
            print("There is nothing here...\n")
        elif tile == "s":
            print("You headed back to the start of the dungeon.\n")
        elif tile == "o":
            print("You cannot go that way...\n")
        elif tile == "f":
            print("Congratulations! You fond the exit.")
            break

    if not player.hp:
        print("You died.")
    print("Game Over")


main()