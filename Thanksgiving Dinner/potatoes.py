from plate_decorator import PlateDecorator


class Potatoes(PlateDecorator):
    def description(self) -> str:
        if super().count():
            return f"{super().description()} and Potatoes"
        return f"{super().description()} with Potatoes"
    
    def area(self) -> int:
        return super().area() - 18
    
    def weight(self) -> int:
        return super().weight() - 6
    
    def count(self) -> int:
        return super().count() + 1