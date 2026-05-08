import logging

logger = logging.getLogger("TemporalVerifier")

class TemporalVerifier:
    def __init__(self):
        # Maps rule_id to its state history
        self.history = {}

    def verify(self, parsed_rules, current_state):
        """
        Verifies temporal constraints over the accumulated history.
        current_state is a dictionary of variable values.
        """
        violations = []
        for rule in parsed_rules:
            rule_id = rule["id"]
            temporal_op = rule.get("temporal", "ALWAYS")
            
            if rule_id not in self.history:
                self.history[rule_id] = []
            
            val = current_state.get(rule["variable"])
            if val is None:
                continue
                
            self.history[rule_id].append(val)
            
            if temporal_op == "ALWAYS":
                if not self._check_condition(val, rule["operator"], rule["threshold"]):
                    violations.append(f"ALWAYS constraint {rule_id} violated at current state.")
            
            elif temporal_op == "EVENTUALLY":
                has_happened = any(self._check_condition(v, rule["operator"], rule["threshold"]) for v in self.history[rule_id])
                if not has_happened:
                    logger.debug(f"EVENTUALLY constraint {rule_id} not yet satisfied.")
                    
            elif temporal_op == "UNTIL":
                condition_met = False
                if rule.get("condition"):
                    cond_var, cond_val = rule["condition"].split("==")
                    cond_val = float(cond_val.strip())
                    if current_state.get(cond_var.strip()) == cond_val:
                        condition_met = True
                
                if not condition_met:
                    if not self._check_condition(val, rule["operator"], rule["threshold"]):
                        violations.append(f"UNTIL constraint {rule_id} violated before condition met.")
                        
        return violations

    def _check_condition(self, val, op, threshold):
        if op == "<": return val < threshold
        elif op == "<=": return val <= threshold
        elif op == ">": return val > threshold
        elif op == ">=": return val >= threshold
        elif op == "==": return val == threshold
        return True
