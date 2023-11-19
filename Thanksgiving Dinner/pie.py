from plate_decorator import PlateDecorator


class Pie(PlateDecorator):
    def description(self) -> str:
        if super().count():
            return f"{super().description()} and Pie"
        return f"{super().description()} with Pie"
    
    def area(self) -> int:
        return super().area() - 19
    
    def weight(self) -> int:
        return super().weight() - 8
    
    def count(self) -> int:
        return super().count() + 1