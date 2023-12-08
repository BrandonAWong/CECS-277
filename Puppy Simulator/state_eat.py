from puppy_state import PuppyState
import state_play
import state_asleep

class StateEat(PuppyState):
    def play(self, puppy) -> str:
        puppy.change_state(state_play.StatePlay())
        puppy.reset()
        puppy.inc_plays()
        return "The puppy looks up from its food and chases the ball you threw."
    
    def feed(self, puppy) -> str:
        puppy.inc_feed()
        reaction =  "The puppy continues to eat as you add another scoop of kibble to its bowl."
        if puppy.feeds >= 3:
            reaction += "\nThe puppy ate so much it feel asleep!"
            puppy.change_state(state_asleep.StateAsleep())
            puppy.reset()
        return reaction