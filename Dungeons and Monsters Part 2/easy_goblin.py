from entity import Entity
from random import randint


class EasyGoblin(Entity):
    '''Beginner level Goblin has normal amount of HP and DMG'''
    def __init__(self):
        super().__init__("Goblin", randint(4, 6))

    def attack(self, entity: Entity) -> str:
        dmg: int = randint(2, 5)
        entity.take_damage(dmg)
        return f"{self.name} attacks {entity.name} for {dmg} damage."