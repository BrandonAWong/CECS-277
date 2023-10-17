from random import randint
from door import Door


class DeadboltDoor(Door):
    def __init__(self):
        # 0 is locked
        # 1 is unlocked
        self._bolt1: int = randint(0, 1)
        self._bolt2: int = randint(0, 1)

    def examine_door(self) -> str:
        return ("A door with two deadbolts. Bothe need to be unlocked to open"
                "the door, but you can't tell if each one is locked or unlocked.")

    def menu_options(self) -> str:
        return "1. Toggle bolt 1\n2. Toggle bolt 2\n"

    def get_menu_max(self) -> int:
        return 2

    def attempt(self, option: int) -> str:
        match option:
            case 1:
                self._bolt1 = 0 if self._bolt1 else 1
                return "You toggle the first bolt."
            case 2:
                self._bolt2 = 0 if self._bolt2 else 1
                return "You toggle the second bolt."
        
    def is_unlocked(self) -> bool:
        return self._bolt1 and self._bolt2
    
    def clue(self) -> str:
        if not self._bolt1 and not self._bolt2: 
            return "You jiggle the door... it's completely locked."
        else:
            return "You jiggle the door... it seems like one of the bolts is unlocked."

    def success(self) -> str:
        return "You unlocked both deadbolts and opened the door.\n"