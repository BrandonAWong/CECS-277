from entity import Entity
from random import randint


class Zombie(Entity):
    def __init__(self):
        super().__init__("Giant Zombie", randint(8, 10))

    def attack(self, entity: Entity) -> str:
        dmg: int = randint(5, 12)
        entity.take_damage(dmg)
        return f"{self.name} attacks {entity.name} for {dmg} damage."