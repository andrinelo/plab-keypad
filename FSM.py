#Finite State Machine

#An FSM object should house a pointer back to the agent, since it will make many requests to the agent (KPC) object.
#from KPC import KPC
from FSMRule import FSMRule
from inspect import isfunction


class FSM:


    def __init__(self, kpc):
        self.state = "S-INIT" #husk å bytte state manuelt under testing
        self.rules = []
        self.CP = "0000" # password
        self.CUMP = "" #Cumulative password
        self.signal = None #byttet her til triggersignal i rules du vil teste
        self.DP = ""
        self.kpc = kpc

    def signal_is_digit(self):
        return 48 <= ord(self.signal) <= 57


    def trigger_is_true(self, rule):
        if isfunction(rule.trigger):
            return rule.trigger()
        else: #self.signal_is_digit(self.trigger):
            return self.signal == rule.trigger

    def set_password(self, password):
        if self.state == "S-ACTIVE":
            self.CP = password


    def add_rule(self, s1, s2, trigger, action):
        self.rules.append(FSMRule(s1, s2, trigger, action))



    def run_rules(self):
        print("Signal when in run_rules = ", self.signal)
        for r in self.rules:
            print(r)
        for rule in self.rules:
            if self.apply_rule(rule):
                print("BREAK")
                break

        print("Ingen av reglene matchet")
         #skal man her sette self.state til state init?
        #go through the rule set, in order, applying each rule until one of the rules is fired.


    def apply_rule(self, rule):
        #check whether the conditions of a rule are met
        print("inne i apply rule")
        print("My state : ", self.state)
        print("Rulestate = ", rule.s1)
        print("Er min stat lik rulestate? ", self.state == rule.s1)
        print("Is trigger true? ", self.trigger_is_true(rule))
        if self.state == rule.s1 and  self.trigger_is_true(rule):
            self.fire_rule(rule)
            print("APPLY")
            return True
        return False





    def fire_rule(self, rule):
        # use the consequent of a rule to a) set the next state of the FSM, and b) call the appropriate agent action method.
        self.state = rule.s2
        rule.action()
        print("FIRE")


    def activate_is_true(self):
        if self.signal:
            return True
        return False


    def validate_cump(self):
        index = len(self.CUMP)
        if self.CP[index] == self.signal:
            return True
        return False


    def unvalidate_cump(self):
        index = len(self.CUMP)
        if self.CP[index] == self.signal:
            return False
        return True


    def validate_entire(self):
        if not len(self.CUMP) == len(self.CP):
            return False
        return self.validate_cump()


    def validate_cump_pr(self):
        index = len(self.CUMP)
        if self.DP[index] == self.signal:
            return True
        return False

    def unvalidate_cump_pr(self):
        index = len(self.CUMP)
        if self.CP[index] == self.signal:
            return False
        return True


    def validate_entire_pr(self):
        if not len(self.CUMP) == len(self.DP):
            return False
        return self.validate_cump()


    def main_loop(self):
        while True:
            self.signal = self.kpc.get_next_signal()
            self.run_rules()




    #begin in the FSMs default initial state and then repeatedly call get next signal
    #and run rules until the FSM enters its default final state.




