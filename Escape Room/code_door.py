from random import choice
from door import Door

class CodeDoor(Door):
    def __init__(self):
        randomize_code = lambda : [choice(["X", "O"]) for _ in range(3)]
        self._correct_code: list[chr] = randomize_code()
        self._input: list[chr] = randomize_code()

    def examine_door(self) -> str:
        return ("A door with a coded keypad with three characters."
                "Each key toggles a value with an 'X' or an 'O'")
    
    def menu_options(self) -> str:
        return ("1. Press Key 1\n"
                "2. Press Key 2\n"
                "3. Press Key 3\n" +
                f"Your current code: {' '.join(self._input)}\n")

    def get_menu_max(self) -> str:
        return 3
    
    def attempt(self, option: int) -> str:
        self._input[option-1] = "X" if self._input[option-1] == "O" else "O"
        match option:
            case 1:
                return f"You toggled the first key to an {self._input[option-1]}"
            case 2:
                return f"You toggled the second key to an {self._input[option-1]}"
            case 3:
                return f"You toggled the third key to an {self._input[option-1]}"

    def is_unlocked(self) -> bool:
        return self._input == self._correct_code
    
    def clue(self) -> str:
        correct = 0
        for i in range(len(self._correct_code)):
            if self._input[i] == self._correct_code[i]:
                correct += 1
        return f"There are {correct} correct characters."
    
    def success(self) -> str:
        return "Congratulations you found the correct code and opened the door.\n"