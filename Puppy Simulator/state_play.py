from puppy_state import PuppyState
import state_asleep


class StatePlay(PuppyState):
    def play(self, puppy) -> str:
        puppy.inc_plays()
        reaction =  "You throw the ball again and the puppy excitedly chases it."
        if puppy.plays >= 3:
            reaction += "\nThe puppy played so much it feel asleep!"
            puppy.change_state(state_asleep.StateAsleep())
            puppy.reset()
        return reaction
    
    def feed(self, puppy) -> str:
        return "The puppy is too busy playing with the ball to eat right now."