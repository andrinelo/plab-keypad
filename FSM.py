#Finite State Machine

#An FSM object should house a pointer back to the agent, since it will make many requests to the agent (KPC) object.
#from KPC import KPC
from FSMRule import FSMRule


class FSM:

    '''Valid states  = S-INIT, S-READ, S-VERIFY, S-ACTIVE
    (S0, S1, S2, S3)
    Kan evt endre disse til å ha en int-verdi? Se hva som er mest praktisk'''


    def __init__(self, kpc):
        self.state = "S-INIT" #husk å bytte state manuelt under testing
        self.rules = []
        self.CP = "0000" # password
        self.CUMP = "" #Cumulative password
        self.signal = None #byttet her til triggersignal i rules du vil teste
        self.DP = ""
        self.kpc = kpc


    def set_password(self, password):
        if self.state == "S-ACTIVE":
            self.CP = password


    def add_rule(self, s1, s2, trigger, action):
        self.rules.append(FSMRule(s1, s2, trigger, action))


    def run_rules(self):
        for rule in self.rules:
            if self.apply_rule(rule):
                print("BREAK")
                break

        print("Ingen av reglene matchet")
         #skal man her sette self.state til state init?
        #go through the rule set, in order, applying each rule until one of the rules is fired.


    def apply_rule(self, rule):
        #check whether the conditions of a rule are met
        if self.state == rule.s1 and  rule.trigger_is_true(self.signal):
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

    def validate_cump(self, sign):
        index = len(self.CUMP)
        if self.CP[index] == sign:
            return True
        return False

    def unvalidate_cump(self, sign):
        index = len(self.CUMP)
        if self.CP[index] == sign:
            return False
        return True

    def validate_entire(self, sign):
        if not len(self.CUMP) == len(self.CP):
            return False
        return self.validate_cump(sign)


    def validate_cump_pr(self, sign):
        index = len(self.CUMP)
        if self.DP[index] == sign:
            return True
        return False

    def unvalidate_cump_pr(self, sign):
        index = len(self.CUMP)
        if self.CP[index] == sign:
            return False
        return True


    def validate_entire_pr(self, sign):
        if not len(self.CUMP) == len(self.DP):
            return False
        return self.validate_cump(sign)


    def main_loop(self):
        while True:
            self.signal = self.kpc.get_next_signal()
            self.run_rules()




    #begin in the FSMs default initial state and then repeatedly call get next signal and run rules until the FSM enters its default final state.




'''
Regler vi må ha med i første del: 
S-INIT, S-READ, activate_is_true, KPC.light_led_1

S-READ, S-ACTIVE, validate_entire, read_to_active
S-READ, S-READ, validate_cump, add_to_cump
S-READ, S-READ, !validate_cump, read_wrong_nr
S-READ, S-INIT, #, power_down

S-ACTIVE, S-INIT, #, power_down

Regler vi må ha med i sette passord og flashe lys: 

S-ACTIVE, S-ACTIVE, 1, KPC.light_led_1
S-ACTIVE, S-ACTIVE, 2, KPC.light_led_2
S-ACTIVE, S-ACTIVE, 3, KPC.light_led_3
S-ACTIVE, S-ACTIVE, 4, KPC.light_led_4
S-ACTIVE, S-ACTIVE, 5, KPC.light_led_5
S-ACTIVE, S-ACTIVE, 6, KPC.light_led_6



S-ACTIVE, S-ACTIVE, 0 eller[7,9],  ingenting skjer

S-ACTIVE, S-PR1, *, flash_change_state
S-PR1, S-PR1, [0,9], add_to_dp
S-PR1, S-ACTIVE, #, reset_dp
S-PR1, S-PR2, *, flash_change_state
S-PR2, S-ACTIVE, #, reset_dp_cump
S-PR2, S-PRVERIFY, validate_entire_pr, flash_change_state
S-PR2, S-PR2, validate_cump_PR, add_to_cump
S-PR2, S-ACTIVE, !validate_cump_PR, pr2_to_active
S-PRVERIFY, S-ACTIVE, *,  verify_to_active

S-ACTIVE, S-INIT, #, power_down()


'''
