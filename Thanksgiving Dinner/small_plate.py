from plate import Plate


class SmallPlate(Plate):
    def description(self) -> str:
        return "Sturdy 10 inch paper plate"
    
    def area(self) -> int:
        return 78
    
    def weight(self) -> int:
        return 32
    
    def count(self) -> int:
        return 0