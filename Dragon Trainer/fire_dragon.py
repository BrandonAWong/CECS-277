from random import randint
import dragon

class Fire_Dragon(dragon.Dragon):
  def __init__(self, name: str, max_hp: int, f_shots: int):
    super().__init__(name, max_hp)
    self.f_shots: int = f_shots
  
  def special_attack(self, other) -> str:
    if self.f_shots:
         dmg = randint(5,9)
         other.take_damage(dmg)
         return f"{self.name} engulf you in flames for {dmg} damage!"
         self.f_shots -= 1
    else:
      return f"{self.name} has no flaming shots left!" 

  def __str__(self):
   return f"{super().__str__()}Flaming Shots: {self.f_shots}"

