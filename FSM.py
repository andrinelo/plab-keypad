#Finite State Machine

#An FSM object should house a pointer back to the agent, since it will make many requests to the agent (KPC) object.
import KPC
from FSMRule import FSMRule

p1 = 1
p2 = 2
p3 = 3
p4 = 4
p5 = 5
p6 = 6

class FSM:

    '''Valid states  = S-INIT, S-READ, S-VERIFY, S-ACTIVE
    (S0, S1, S2, S3)
    Kan evt endre disse til å ha en int-verdi? Se hva som er mest praktisk'''


    def __init__(self):
        self.state = "S-INIT"
        self.rules = []
        self.CP = "0000" # password
        self.CUMP = "" #Cumulative password
        self.signal = None
        self.DP = ""

    def set_password(self, password):
        if self.state == "S-ACTIVE":
            self.CP = password

    @staticmethod
    def signal_is_digit(sign):
        return 48 <= ord(sign) <= 57

    def add_rule(self, s1, s2, trigger, action):
        self.rules.append(FSMRule(s1, s2, trigger, action))


    def get_next_signal(self, signal):
        self.signal = signal
        #query the agent for the next signal.

    def run_rules(self):
        for rule in self.rules:
            if self.apply_rule(rule):
                break
        print("Ingen av reglene matchet") # skal man her sette self.state til state init?
        #go through the rule set, in order, applying each rule until one of the rules is fired.


    def apply_rule(self, rule):
        if self.state == rule.s1 and  rule.trigger_is_true(self.signal):
            self.fire_rule(rule)
            return True
        return False
        #check whether the conditions of a rule are met


    def fire_rule(self, rule):
            self.state = rule.s2
            rule.action()


            '''if isinstance(rule.trigger, self.validate_cump):
                if self.validate_cump(self.signal):
                    self.CUMP += self.signal
                else:
                    self.CUMP = ""'''


            #???? denne linjen må være input til agent så agent gjør action??? i think?
        # use the consequent of a rule to a) set the next state of the FSM, and b) call the appropriate agent action method.

    def activate_is_true(self):
        if self.signal:
            return True
        return False

    def validate_cump(self, sign):
        index = len(self.CUMP)
        if self.CP[index] == sign:
            return True
        return False

    def validate_entire(self, sign):
        if not len(self.CUMP) == len(self.CP):
            return False
        return self.validate_cump(sign)


    def validate_cump_pr(self, sign):
        index = len(self.CUMP)
        if self.DP[index] == sign:
            return True
        return False

    def validate_entire_pr(self, sign):
        if not len(self.CUMP) == len(self.DP):
            return False
        return self.validate_cump(sign)

    def read_to_active(self):
        KPC.twinkle_leds()
        self.reset_cump()


    def reset_cump(self):
        self.CUMP = ""

    def add_to_cump(self):
        self.CUMP += self.signal

    def read_wrong_nr(self):
        KPC.flash_leds()
        self.reset_cump()

    def power_down(self):
        KPC.light_one_led(p2)
        KPC.light_one_led(p4)
        KPC.light_one_led(p6)

    def flash_change_state(self):
        KPC.light_one_led(p1)
        KPC.light_one_led(p2)


    def add_to_dp(self):
        self.DP += self.signal

    def reset_dp(self):
        self.DP = ""

    def reset_dp_cump(self):
        self.reset_cump()
        self.reset_dp()

    def pr2_to_active(self):
        self.reset_dp_cump()
        KPC.flash_leds()

    def verify_to_active(self):
        KPC.twinkle_leds()
        self.CP = self.DP
        self.reset_dp_cump()

def main_loop():

    #begin in the FSMs default initial state and then repeatedly call get next signal and run rules until the FSM enters its default final state.
    return 0




'''
Regler vi må ha med i første del: 
S-INIT, S-READ, activate_is_true, KPC.light_one_led(p1)

S-READ, S-ACTIVE, validate_entire, read_to_active()
S-READ, S-READ, validate_cump, add_to_cump()
S-READ, S-READ, !validate_cump, read_wrong_nr()
S-READ, S-INIT, #, power_down()

S-ACTIVE, S-INIT, #, power_down()

Regler vi må ha med i sette passord og flashe lys: 

S-ACTIVE, S-ACTIVE, x=[1,6], KPC.light_one_led(x)
S-ACTIVE, S-ACTIVE, 0 eller[7,9],  ingenting skjer
S-ACTIVE, S-PR1, *, flash_change_state()
S-PR1, S-PR1, [0,9], add_to_dp()
S-PR1, S-ACTIVE, #, reset_dp()
S-PR1, S-PR2, *, flash_change_state()
S-PR2, S-ACTIVE, #, reset_dp_cump()
S-PR2, S-PRVERIFY, validate_entire_pr, flash_change_state()
S-PR2, S-PR2, validate_cump_PR, add_to_cump()
S-PR2, S-ACTIVE, !validate_cump_PR, pr2_to_active()
S-PRVERIFY, S-ACTIVE, *,  verify_to_active()

S-ACTIVE, S-INIT, #, power_down()








'''
