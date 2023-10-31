from abc import ABC, abstractmethod


class Entity(ABC):
    def __init__(self, name: str, max_hp: int):
        self._name: str = name
        self._hp: int = max_hp
        self._max_hp: int = max_hp

    @property
    def name(self) -> str:
        return self._name
    
    @property
    def hp(self) -> int:
        return self._hp

    def take_damage(self, dmg: int) -> None:
        '''Reduces entity's HP based on damage taken from input'''
        self._hp = max(0, self._hp - dmg)

    def heal(self):
        '''Restores entity's HP to max'''
        self._hp = self._max_hp

    def __str__(self):
        return f"{self.name}\nHP: {self.hp}/{self._max_hp}"
    
    @abstractmethod
    def attack(self, entity):
        pass
