# Names: Trung Ho, Dylan Garvey, Brandon Wong
# Date: 12/07/23
# Desc: Simulate having your own puppy. You can choose to either feed or play with them!
# Their reactions differ based on their current state.


from check_input import get_int_range
from puppy import Puppy


def main():
    print("Congratulations on your new puppy!")
    puppy = Puppy()
    while True:
        choice: int = get_int_range(
            "What would you like to do?\n1. Feed the puppy\n"
            "2. Play with the puppy\n3. Quit\nEnter choice: ", 1, 3)
        
        if choice == 1:
            print(f"\n{puppy.give_food()}")
        elif choice == 2:
            print(f"\n{puppy.throw_ball()}")
        else:
            break

main()