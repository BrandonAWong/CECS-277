from plate_decorator import PlateDecorator


class Stuffing(PlateDecorator):
    def description(self) -> str:
        if super().count():
            return f"{super().description()} and Stuffing"
        return f"{super().description()} with Stuffing"
    
    def area(self) -> int:
        return super().area() - 18
    
    def weight(self) -> int:
        return super().weight() - 7
    
    def count(self) -> int:
        return super().count() + 1