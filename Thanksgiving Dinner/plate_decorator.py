from plate import Plate
from abc import ABC


class PlateDecorator(Plate, ABC):
    def __init__(self, p: Plate):
        self._plate = p
    
    def description(self) -> str:
        return self._plate.description()
    
    def area(self) -> int:
        return self._plate.area()
    
    def weight(self) -> int:
        return self._plate.weight()
    
    def count(self) -> int:
        return self._plate.count()