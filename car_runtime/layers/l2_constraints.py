import logging
from typing import List, Dict, Any
from core.types import Constraint
from constitution.rule_loader import RuleLoader
from constitution.parser import ConstitutionParser
from constitution.compiler import ConstitutionCompiler

logger = logging.getLogger("L2_ConstraintCompilation")

class ConstraintCompilationLayer:
    """
    Layer 2: Constraint Compilation
    Wraps the Formal Constitution Engine to parse YAML rules and compile them into Z3 constraints.
    """
    def __init__(self):
        self.rule_loader = RuleLoader()
        self.parser = ConstitutionParser()
        self.compiler = ConstitutionCompiler()
        
    def load_rules_from_yaml(self, filepath: str) -> List[Dict[str, Any]]:
        # For backward compatibility, we ignore filepath and load all rules from the formal dir
        logger.info("Loading formal constitutional rules...")
        return self.rule_loader.load_all_rules()
        
    def compile_norms_to_smt(self, norms: List[Dict[str, Any]]) -> List[Constraint]:
        logger.info(f"Using Constitution Engine to compile {len(norms)} norms.")
        parsed_rules = self.parser.parse(norms)
        return self.compiler.compile(parsed_rules)

