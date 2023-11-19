from abc import ABC


class Plate(ABC):
    """Interface for plates"""

    def description(self) -> str:
        """Return a description of the plate and what's on it"""
        pass

    def area(self) -> int:
        """Returns the how many empty square inches are on the plate"""
        pass

    def weight(self) -> int:
        """Returns how many ounces a plate can still hold"""
        pass

    def count(self) -> int:
        """Returns how many items the plate is currently holding"""
        pass

