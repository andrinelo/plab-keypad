#from FSM import finiteSM


class FSMRule:

    def __init__(self, s1, s2, trigger, action):
        self.s1 = s1
        self.s2 = s2
        self.trigger = trigger
        self.action = action




        # sjekke # og * --- sjekke det her? eller i FSM

    def __str__(self):
        return "State = "+ self.s1+ ". NextState = "+ self.s2