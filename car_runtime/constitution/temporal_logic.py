from enum import Enum

class TemporalOperator(Enum):
    ALWAYS = "ALWAYS"
    EVENTUALLY = "EVENTUALLY"
    UNTIL = "UNTIL"
    NEVER = "NEVER"

class TemporalConstraint:
    def __init__(self, rule_id, operator, variable, threshold, logic_op, condition=None):
        self.rule_id = rule_id
        self.operator = TemporalOperator(operator)
        self.variable = variable
        self.threshold = threshold
        self.logic_op = logic_op
        self.condition = condition
