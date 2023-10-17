from random import randint
from door import Door


class LockedDoor(Door):
    def __init__(self):
        self._key_location: int = randint(1, 3)
        self._input: int = None

    def examine_door(self) -> str:
        return "A locked door. Look around for the key."
    
    def menu_options(self) -> str:
        return ("1. Look under the mat\n"
                "2. Look under the flower pot\n"
                "3. Look under the face rock\n")
    
    def get_menu_max(self) -> int:
        return 3
    
    def attempt(self, option: int) -> str:
        self._input = option
        match option:
            case 1:
                return "You look under the mat."
            case 2:
                return "You look under the flower pot."
            case 3:
                return "You look under the face rock."

    def is_unlocked(self) -> bool:
        return self._input == self._key_location
    
    def clue(self) -> str:
        return "Look somewhere else."
    
    def success(self) -> str:
        return "You found the key and unlocked the door.\n"