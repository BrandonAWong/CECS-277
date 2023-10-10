from abc import ABC, abstractmethod


class Entity(ABC):
    def __init__(self, name: str, max_hp: int):
        self._name: str = name
        self._hp = self._max_hp = max_hp

    @property
    def name(self):
        return self._name
    
    @property
    def hp(self):
        return self._hp

    def take_damage(self, dmg: int) -> None:
        self._hp = max(self.hp - dmg, 0)
    
    def __str__(self):
        return f"{self.name}: {self.hp}/{self._max_hp}"

    @abstractmethod
    def basic_attack(self, other):
        pass

    @abstractmethod
    def special_attack(self, other):
        pass