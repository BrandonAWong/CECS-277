from entity import Entity
from map import Map
from random import randint


class Hero(Entity):
    def __init__(self, name: str):
        super().__init__(name, 25)
        self._loc: list[int] = [0, 0]

    @property
    def loc(self):
        return self._loc
    
    def attack(self, entity: Entity):
        dmg: int = randint(2, 5)
        entity.take_damage(dmg)
        return f"{self.name} attacks a {entity.name} for {dmg} damage."
    
    def go_north(self) -> chr:
        if self.loc[0] > 0:
            self.loc[0] -= 1
            return Map(self.loc)
        return "o"
    
    def go_south(self) -> chr:
        if self.loc[0] < len(Map):
            self.loc[0] += 1
            return Map(self.loc)
        return "o"
    
    def go_east(self) -> chr:
        if self.loc[1] > 0:
            self.loc[1] -= 1
            return Map(self.loc)
        return "o"
    
    def go_west(self) -> chr:
        if self.loc[1] < len(Map[self.loc[1]]):
            self.loc[1] += 1
            return Map(self.loc)
        return "o"