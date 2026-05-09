import logging
from typing import List, Dict

logger = logging.getLogger("OutcomeTracker")

class OutcomeTracker:
    """
    Logs the trajectory of dynamic metrics across all epochs.
    """
    def __init__(self):
        self.history: List[Dict] = []
        
    def log_epoch(self, state_dict: Dict):
        self.history.append(state_dict)
        
    def print_report(self):
        logger.info("\n" + "="*60)
        logger.info(" CONSTITUTIONAL WORLD SIMULATOR - FINAL REPORT ")
        logger.info("="*60)
        
        for record in self.history:
            epoch = record["epoch"]
            stab = record["social_stability"]
            fair = record["fairness_evolution"]
            risk = record["risk_escalation"]
            trust = record["trust_levels"]
            econ = record["economic_impact"]
            
            # Simple ASCII bar for visual
            stab_bar = "#" * int(stab / 5)
            
            logger.info(f"Epoch {epoch:02d} | Stab:{stab:5.1f} | Fair:{fair:5.1f} | Risk:{risk:5.1f} | Trust:{trust:5.1f} | Econ:{econ:5.1f}")
            
        logger.info("="*60)
