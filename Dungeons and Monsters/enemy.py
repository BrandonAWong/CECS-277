from entity import Entity
from random import choice, randint


class Enemy(Entity):
    def __init__(self):
        super().__init__(choice(("Goblin", "Vampire","Ghoul", "Skeleton", "Zombie")), randint(4, 8))
    
    def attack(self, entity: Entity) -> str:
        dmg: int = randint(1, 4)
        entity.take_damage(dmg)
        return f"{self.name} attacks a {entity.name} for {dmg} damage."