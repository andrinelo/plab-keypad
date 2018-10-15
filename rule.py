class Rule:

    def __init__(self, rule):
        self.rule = rule

    def check_rule(self, inp):
        return self.rule == inp
