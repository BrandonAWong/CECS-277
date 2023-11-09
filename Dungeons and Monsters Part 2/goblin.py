from entity import Entity
from random import randint


class Goblin(Entity):
    '''Expert level Goblin which has more base HP and DMG'''
    def __init__(self):
        super().__init__("Greedy Goblin", randint(8, 12))

    def attack(self, entity: Entity) -> str:
        dmg: int = randint(6, 12)
        entity.take_damage(dmg)
        return f"{self.name} attacks {entity.name} for {dmg} damage."