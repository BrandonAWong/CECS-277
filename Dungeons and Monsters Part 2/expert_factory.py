from enemy_factory import EnemyFactory
from zombie import Zombie
from skeleton import Skeleton
from goblin import Goblin
from random import choice


class ExpertFactory(EnemyFactory):
    def create_random_enemy(self):
        return choice((Zombie(), Skeleton(), Goblin()))