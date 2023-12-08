import state_asleep
import puppy_state


class Puppy:
    def __init__(self):
        self._plays = self._feeds = 0
        self._state: puppy_state.PuppyState = state_asleep.StateAsleep()

    @property
    def plays(self) -> int:
        return self._plays
    
    @property
    def feeds(self) -> int:
        return self._feeds
    
    def change_state(self, new_state) -> None:
        """Updates the puppy's state based on the argument"""
        self._state = new_state

    def throw_ball(self) -> str:
        """Calls the play method of the puppy's current state"""
        return self._state.play(self)
    
    def give_food(self) -> str:
        """Calls the feed method of the puppy's current state"""
        return self._state.feed(self)
    
    def inc_feed(self) -> None:
        """Increments how many times the puppy has been fed in a row"""
        self._feeds += 1

    def inc_plays(self) -> None:
        """Increments how many imes the pupy has played in a row"""
        self._plays += 1
    
    def reset(self) -> None:
        """Resets the counter for puppy feeds and plays attributes"""
        self._plays = self._feeds = 0