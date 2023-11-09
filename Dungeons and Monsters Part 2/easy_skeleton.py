from entity import Entity
from random import randint


class EasySkeleton(Entity):
    '''Beginner level Skeleton has normal amount of HP and DMG'''
    def __init__(self):
        super().__init__("Skeleton", randint(3, 4))

    def attack(self, entity: Entity) -> str:
        dmg: int = randint(1, 4)
        entity.take_damage(dmg)
        return f"{self.name} attacks {entity.name} for {dmg} damage."