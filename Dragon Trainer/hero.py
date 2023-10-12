from entity import Entity
import random as rand


class Hero(Entity):
    """
    A class representing a Hero's basic attack and special attack
    Inherits from entity
  
    """
    def basic_attack(self, other) -> str:
        """Function that performs damage of basic
        and applies it to other entity"""
        damage_output = rand.randrange(1,7) + rand.randrange(1,7)
        other.take_damage(damage_output)    
        return f"You slash the {other.name} with your sword for {damage_output} damage!"

    def special_attack(self, other) -> str:
        """Function that performs damage of special attack
        and applies it to other entity"""
        damage_output = rand.randrange(1,13)
        other.take_damage(damage_output)
        return f"You hit the {other.name} with an arrow for {damage_output} damage!"