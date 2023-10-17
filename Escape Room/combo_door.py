from random import randint
from door import Door


class ComboDoor(Door):
    def __init__(self):
        self._correct_value: int = randint(1, 10)
        self._input: int = None

    def examine_door(self) -> str:
        return "A door with a combination lock. You can spin the dial to a number 1-10."

    def menu_options(self) -> str:
        return "Enter # 1-10: "
    
    def get_menu_max(self) -> int:
        return 10
    
    def attempt(self, option: int) -> str:
        self._input = option
        return f"You turn the dial to... {option}"

    def is_unlocked(self) -> bool:
        return self._input == self._correct_value

    def clue(self) -> str:
        if self._input > self._correct_value:
            return "Try a lower value."
        else:
            return "Try a higher value."

    def success(self) -> str:
        return "You found the correct value and opened the door.\n"
    