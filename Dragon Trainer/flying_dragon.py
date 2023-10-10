from dragon import Dragon
from random import randint

class FlyingDragon(Dragon):
    def __init__(self, name: str, max_hp: int, swoops: int):
        super().__init__(name, max_hp)
        self.swoops = swoops

    def special_attack(self, other) -> str:
        if self.swoops:
            dmg = randint(5, 8)
            other.take_damage(dmg)
            self.swoops -= 1
            return f"{self.name} swoops at you for {dmg} damage!"
        return f"{self.name} tries to swoop down to hit you, but failed."
    
    def __str__(self):
        return f"{super().__str__()}\nSwoop attacks remaining: {self.swoops}" 