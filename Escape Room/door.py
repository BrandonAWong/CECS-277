from abc import ABC, abstractmethod


class Door(ABC):
    """
    Abstract class with multiple methods for simulating a door.
    """
    @abstractmethod
    def examine_door(self) -> str:
        """
        Returns a description of the door.
        """
        ...
    
    @abstractmethod
    def menu_options(self) -> str:
        """
        Returns menu of options the user can choose from when attempting to
        unlock the door.
        """
        ...
    
    @abstractmethod
    def get_menu_max(self) -> int:
        """
        Returns how many options the user can choose from.
        """
        ...
    
    @abstractmethod
    def attempt(self, option: int) -> str:
        """
        Saves the user input.
        Return a string detailing what the user attempted to do.
        """
        ...

    @abstractmethod
    def is_unlocked(self) -> bool:
        """
        Checks to see if the door has been unlocked or not.
        Return True if it has, False otherwise.
        """
        ...

    @abstractmethod
    def clue(self) -> str:
        """
        Returns a hint if the user was unsuccesful in their attempt.
        """
        ...
    
    @abstractmethod
    def success(self) -> str:
        """
        Returns congratulatory message if user was successful in their attempt.
        """
        ...