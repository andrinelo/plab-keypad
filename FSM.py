#Finite State Machine

#An FSM object should house a pointer back to the agent, since it will make many requests to the agent (KPC) object.
class FSM:

    '''Valid states  = S-INIT, S-READ, S-VERIFY, S-ACTIVE
    (S0, S1, S2, S3)
    Kan evt endre disse til å ha en int-verdi? Se hva som er mest praktisk'''


    def __init__(self):
        self.state = "S-INIT"
        self.CP = "" #Current password
        self.CUMP = "" #Cumulative password

    def set_password(self, password):
        if self.state == "S-ACTIVE":
            self.CP = password

    def signal_is_digit(self, s):
        return 48 <= ord(s) <= 57

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
