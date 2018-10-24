#from FSM import finiteSM
from inspect import isfunction

class FSMRule:

    def __init__(self, s1, s2, trigger, action):
        self.s1 = s1
        self.s2 = s2
        self.trigger = trigger
        self.action = action


    #flytta signal_is_digit hit fra FSM
    @staticmethod
    def signal_is_digit(sign):
        return 48 <= ord(sign) <= 57

    def trigger_is_true(self, sign):
        if isfunction(self.trigger):
            return self.trigger(sign)
        else: #self.signal_is_digit(self.trigger):
            return sign == self.trigger

        # sjekke # og * --- sjekke det her? eller i FSM

    def __str__(self):
        return "State = "+ self.s1+ ". NextState = "+ self.s2