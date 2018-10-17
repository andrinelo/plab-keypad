from FSM import FSM
from inspect import isfunction

class FSMRule:

    def __init__(self, s1, s2, trigger, action):
        self.s1 = s1
        self.s2 = s2
        self.trigger = trigger
        self.action = action

    def trigger_is_true(self, sign):
        if isfunction(self.trigger):
            return self.trigger(sign)
        if FSM.signal_is_digit(self.trigger):
            return sign == self.trigger
        return False

