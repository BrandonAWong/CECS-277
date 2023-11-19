from plate_decorator import PlateDecorator


class GreenBeans(PlateDecorator):
    def description(self) -> str:
        if super().count():
            return f"{super().description()} and Green Beans"
        return f"{super().description()} with Green Beans"
    
    def area(self) -> int:
        return super().area() - 20
    
    def weight(self) -> int:
        return super().weight() - 3
    
    def count(self) -> int:
        return super().count() + 1