from plate import Plate


class LargePlate(Plate):
    def description(self) -> str:
        return "Flimsy 12 inch paper plate"
    
    def area(self) -> int:
        return 113
    
    def weight(self) -> int:
        return 24
    
    def count(self) -> int:
        return 0