from entity import Entity
from random import randint


class EasyZombie(Entity):
    '''Beginner level Zombie has normal amount of HP and DMG'''
    def __init__(self):
        super().__init__("Zombie", randint(4, 5))

    def attack(self, entity: Entity) -> str:
        dmg: int = randint(1, 5)
        entity.take_damage(dmg)
        return f"{self.name} attacks {entity.name} for {dmg} damage."