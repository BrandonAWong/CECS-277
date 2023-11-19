from plate_decorator import PlateDecorator


class Turkey(PlateDecorator):
    def description(self) -> str:
        if super().count():
            return f"{super().description()} and Turkey"
        return f"{super().description()} with Turkey"
    
    def area(self) -> int:
        return super().area() - 15
    
    def weight(self) -> int:
        return super().weight() - 4
    
    def count(self) -> int:
        return super().count() + 1