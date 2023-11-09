from enemy_factory import EnemyFactory
from easy_zombie import EasyZombie
from easy_skeleton import EasySkeleton
from easy_goblin import EasyGoblin
from random import choice


class BeginnerFactory(EnemyFactory):
    def create_random_enemy(self):
        return choice((EasyZombie(), EasySkeleton(), EasyGoblin()))