from random import randint
from door import Door


class BasicDoor(Door):
    def __init__(self):
        self._state: int = randint(1, 2)
        self._input: int = None

    def examine_door(self) -> str:
        return "A door that is either pushed or pulled."
    
    def menu_options(self) -> str:
        return "1. Pull\n2. Push\n"
    
    def get_menu_max(self) -> int:
        return 2
    
    def attempt(self, option: int) -> str:
        self._input = option
        match option:
            case 1:
                return "You pushed the door."
            case 2:
                return "You pulled the door."
    
    def is_unlocked(self) -> bool:
        return self._input == self._state
    
    def clue(self) -> str:
        return "Try the other way"
    
    def success(self) -> str:
        return "Congratulations you opened the door.\n"