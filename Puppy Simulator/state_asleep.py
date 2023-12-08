from puppy_state import PuppyState
import state_eat


class StateAsleep(PuppyState):
    def play(self, puppy) -> str:
        return "The puppy is asleep. It doesn't want to play right now."
        
    def feed(self, puppy) -> str:
        puppy.change_state(state_eat.StateEat())
        puppy.reset()
        puppy.inc_feed()
        return "The puppy wakes up and comes running to eat."