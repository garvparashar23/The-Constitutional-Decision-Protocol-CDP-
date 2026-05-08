import z3
import logging
import sys
import os

# Add parent dir to path to find core.types
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core.types import Constraint

logger = logging.getLogger("ConstitutionCompiler")

class ConstitutionCompiler:
    """
    Compiles parsed symbolic rules into Z3 constraints.
    """
    def __init__(self):
        self.variables = {
            "predicted_risk": z3.Real('predicted_risk'),
            "predicted_fairness": z3.Real('predicted_fairness'),
            "utility": z3.Real('utility'),
            "privacy_violation": z3.Real('privacy_violation'),
            "censorship_score": z3.Real('censorship_score'),
            "historical_bias": z3.Real('historical_bias'),
            "instability_index": z3.Real('instability_index'),
            "robustness_score": z3.Real('robustness_score'),
            "crisis_resolved": z3.Real('crisis_resolved')
        }

    def compile(self, parsed_rules):
        logger.info(f"Compiling {len(parsed_rules)} symbolic rules into Z3 SMT constraints.")
        compiled_constraints = []
        
        for rule in parsed_rules:
            var = self.variables.get(rule["variable"])
            if var is None:
                self.variables[rule["variable"]] = z3.Real(rule["variable"])
                var = self.variables[rule["variable"]]
                
            threshold = rule["threshold"]
            op = rule["operator"]
            
            if op == "<": expr = var < threshold
            elif op == "<=": expr = var <= threshold
            elif op == ">": expr = var > threshold
            elif op == ">=": expr = var >= threshold
            elif op == "==": expr = var == threshold
            else: continue
            
            compiled_constraints.append(Constraint(
                id=rule["id"], 
                name=rule["name"], 
                logic_expr=expr, 
                is_hard=rule["is_hard"]
            ))
            
        return compiled_constraints
