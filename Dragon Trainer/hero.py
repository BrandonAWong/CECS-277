from entity import Entity
from random import randint


class Hero(Entity):
    def basic_attack(self, other) -> str:
        dmg = randint(1, 6) + randint(1, 6)
        other.take_damage(dmg)
        return f"You slash the {other.name} with your sword for {dmg} damage."

    def special_attack(self, other) -> str:
        dmg = randint(1, 12)
        other.take_damage(dmg)
        return f"You hit the {other.name} with an arrow for {dmg} damage."