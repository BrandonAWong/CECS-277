from abc import ABC, abstractmethod


class PuppyState(ABC):
    @abstractmethod
    def play(self, puppy) -> str:
        """Returns a string of puppy's reaction to trying to play with it"""
        pass

    @abstractmethod
    def feed(self, puppy) -> str:
        """Returns a string of puppy's reaction to trying to feed it"""
        pass