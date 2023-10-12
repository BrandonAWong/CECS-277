from abc import ABC, abstractmethod


class Entity(ABC):
    """
    A class representing Entity
  
    Attributes:
  
    name(str): name of the entity
    max_hp(int): The amount of hp a entity has left
    
    """
    def __init__(self, name: str, max_hp: int):
      """
      The constructor for entity class

      Parameters:
      
      name(str): name of the entity
      max_hp(int): The amount of hp a entity has left
      """
      self._name: str = name
      self._hp = self._max_hp = max_hp

    @property
    def name(self):
      """Getter function that returns name of entity"""
      return self._name
    
    @property
    def hp(self):
      """Getter function that returns entity hp"""
      return self._hp

    def take_damage(self, dmg: int):
      """Function that equates entity hp to max of hp minus damge taken"""
      self._hp = max(self.hp - dmg, 0)
    
    def __str__(self):
      """Funtion that returns a string of name of entity and its hp/max hp"""
      return f"{self.name}: {self.hp}/{self._max_hp}"

    @abstractmethod
    def basic_attack(self, other):
      """Function that is a abstractmethod for basic attack"""
      pass

    @abstractmethod
    def special_attack(self, other):
      """Function that is a abstractmethod for special attack"""
      pass