# Names: Dylan Garvey, Trung Ho, Brandon Wong
# Date: 11/18/2023
# Desc: Thanksgiving buffet simulator! Try to get as much food on your plate 
# without the plate falling apart.


from plate import Plate
from small_plate import SmallPlate
from large_plate import LargePlate
from turkey import Turkey
from stuffing import Stuffing
from potatoes import Potatoes
from green_beans import GreenBeans
from pie import Pie
from check_input import get_int_range


def examine_plate(p: Plate) -> bool:
    """
    Prints a description of the plate and hints on how much more it can hold.
    Returns False if there's still room left on the plate, else True otherwise.
    """
    print(p.description())
    if p.weight() <= 0:
        print("Your plate snaps in half from all the weight of the food! Your food falls to your feet.")
        return True
    elif 1 <= p.weight() <= 6:
        sturdiness = "Bending"
    elif 7 <= p.weight() <= 12:
        sturdiness = "Weak"
    else:
        sturdiness = "Strong"

    if p.area() <= 0:
        print("Your plate isn't big enough for this much food! Your food spills over the edge.")
        return True
    elif 1 <= p.area() <= 20:
        space = "A tiny bit"
    elif 21 <= p.area() <= 40:
        space = "Some"
    else:
        space = "Plenty"
    print(f"Sturdiness: {sturdiness}\nSpace available: {space}")
    return False
    

def main():
    print("- Thanksgiving Dinner -\n"
          "Serve yourself as much food as you like from the buffet, but make "
          "sure that your plate will hold without spilling everywhere!")
    if get_int_range("Choose a plate:\n1. Small Sturdy Plate\n2. Large Flimsy Plate\n", 1, 2) == 1:
        plate = SmallPlate()
    else:
        plate = LargePlate()
    while True:
        user_choice = get_int_range("1. Turkey\n2. Stuffing\n3. Potatoes\n4. Green Beans\n5. Pie\n6. Quit\n", 1, 6)
        match user_choice:
            case 1:
                plate = Turkey(plate)
            case 2:
                plate = Stuffing(plate)
            case 3:
                plate = Potatoes(plate)
            case 4:
                plate = GreenBeans(plate)
            case 5:
                plate = Pie(plate)
            case 6:
                break
        if examine_plate(plate):
            break
        
    if plate.weight() > 0 and plate.area() > 0:
        print(f"Good job! You made it to the table with {plate.count()} items!\n"
            f"There was still {plate.area()} square inches left on your plate.\n"
            f"Your plate could have held {plate.weight()} more ounces of food.\n"
            "Don't worry, you can always go back for more. Happy Thanksgiving!")
main()