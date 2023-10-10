from random import randint
import entity

class Dragon(entity.Entity):

    def basic_attack(self, other) -> str:
      damage = randint(3,7)
      other.take_damage(damage)
      return f"{self.name} smashes you with its tail for {damage} damage!"

    def special_attack(self, other) -> str:
      damage = randint(4,8)
      other.take_damage(damage)
      return f"{self.name} slashes you with its claws for {damage} damage!"