#Finite State Machine

#An FSM object should house a pointer back to the agent, since it will make many requests to the agent (KPC) object.
from FSMRule import FSMRule


class FSM:

    '''Valid states  = S-INIT, S-READ, S-VERIFY, S-ACTIVE
    (S0, S1, S2, S3)
    Kan evt endre disse til å ha en int-verdi? Se hva som er mest praktisk'''


    def __init__(self):
        self.state = "S-INIT"
        self.rules = []
        self.CP = "" #Current password
        self.CUMP = "" #Cumulative password
        self.signal = None

    def set_password(self, password):
        if self.state == "S-ACTIVE":
            self.CP = password

    def signal_is_digit(self):
        return 48 <= ord(self.signal) <= 57

    def add_rule(self, s1, s2, trigger, action):
        self.rules.append(FSMRule(s1, s2, trigger, action))


    def get_next_signal(self, signal):
        self.signal = signal
        #query the agent for the next signal.
        return 0

    def run_rules(self):
        for rule in self.rules:
            if self.apply_rule(rule):
                break
        #go through the rule set, in order, applying each rule until one of the rules is fired.


    def apply_rule(self, rule):
        if self.state == rule.s1 and  self.signal == rule.trigger:
            self.fire_rule(rule)
            return True
        return False
        #check whether the conditions of a rule are met

    def fire_rule(self, rule):
            self.state = rule.s2
            rule.action() #????
        # use the consequent of a rule to a) set the next state of the FSM, and b) call the appropriate agent action method.


def main_loop():

    #begin in the FSMs default initial state and then repeatedly call get next signal and run rules until the FSM enters its default final state.
    return 0
