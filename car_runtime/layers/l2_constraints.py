import z3
from typing import List, Dict
import logging
from core.types import Constraint

import yaml

logger = logging.getLogger("L2_ConstraintCompilation")

class ConstraintCompilationLayer:
    """
    Layer 2: Constraint Compilation
    Compiles human-readable YAML norms into First-Order Logic (FOL) and Z3 SMT constraints.
    """
    def __init__(self):
        self.solver = z3.Solver()
        self.variables = {
            "predicted_risk": z3.Real('predicted_risk'),
            "predicted_fairness": z3.Real('predicted_fairness'),
            "utility": z3.Real('utility')
        }
        
    def load_rules_from_yaml(self, filepath: str) -> List[Dict[str, Any]]:
        with open(filepath, 'r') as f:
            data = yaml.safe_load(f)
        return data.get("constraints", [])
        
    def compile_norms_to_smt(self, norms: List[Dict[str, Any]]) -> List[Constraint]:
        logger.info(f"Compiling {len(norms)} YAML norms into SMT constraints.")
        compiled = []
        
        for norm in norms:
            var = self.variables.get(norm["variable"])
            if var is None:
                continue
                
            threshold = norm["threshold"]
            op = norm["operator"]
            
            if op == "<": expr = var < threshold
            elif op == "<=": expr = var <= threshold
            elif op == ">": expr = var > threshold
            elif op == ">=": expr = var >= threshold
            elif op == "==": expr = var == threshold
            else: continue
            
            compiled.append(Constraint(
                id=norm["id"], 
                name=norm["name"], 
                logic_expr=expr, 
                is_hard=norm.get("is_hard", True)
            ))
                
        return compiled
