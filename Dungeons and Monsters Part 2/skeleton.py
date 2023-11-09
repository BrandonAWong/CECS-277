from entity import Entity
from random import randint


class Skeleton(Entity):
    def __init__(self):
        super().__init__("Mutant Skeleton", randint(6, 10))

    def attack(self, entity: Entity) -> str:
        dmg: int = randint(6, 10)
        entity.take_damage(dmg)
        return f"{self.name} attacks {entity.name} for {dmg} damage."