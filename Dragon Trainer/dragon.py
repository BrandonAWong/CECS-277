from random import randint
import entity

class Dragon(entity.Entity):
    """
    Base dragon which contains a basic and special attack.
    """
    def basic_attack(self, other) -> str:
      """
      Performs a tail attack ranging from 3-7 damage.
      """
      damage = randint(3,7)
      other.take_damage(damage)
      return f"{self.name} smashes you with its tail for {damage} damage!"

    def special_attack(self, other) -> str:
      """
      Performs a claw attack ranging from 4-8 damage.
      """
      damage = randint(4,8)
      other.take_damage(damage)
      return f"{self.name} slashes you with its claws for {damage} damage!"