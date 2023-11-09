from abc import ABC, abstractmethod


class EnemyFactory(ABC):
    @abstractmethod
    def create_random_enemy(self):
        '''Create a random enemy for player to encounter'''
        pass