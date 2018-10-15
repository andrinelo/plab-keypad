#Finite State Machine

#An FSM object should house a pointer back to the agent, since it will make many requests to the agent (KPC) object.
class FSM:

    def __init__(self):
        self.state = "S-INIT"

    def add_rule():
        #add a new rule to the end of the FSMs rule list
        return 0

    def get_next_signal():
        #query the agent for the next signal.
        return 0

    def run_rules():
        #go through the rule set, in order, applying each rule until one of the rules is fired.
        return 0

    def apply_rule():
        #check whether the conditions of a rule are met
        return 0

    def fire_rule():
        # use the consequent of a rule to a) set the next state of the FSM, and b) call the appropriate agent action method.
        return 0

    def main_loop():
        #begin in the FSMs default initial state and then repeatedly call get next signal and run rules until the FSM enters its default final state.
        return 0