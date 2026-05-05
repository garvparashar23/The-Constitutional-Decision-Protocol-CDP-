import torch
import logging

logger = logging.getLogger("Phase5_Orchestrator")

class GovernanceEngine:
    """
    Phase 5: Governance Engine (G)
    Implements decision fusion logic to combine all adversarial scores.
    """
    def __init__(self):
        pass

    def decide(self, d_e: int, v: float, a: float, t: float) -> int:
        """
        Input: (d_e, v, a, t)
        Output: final decision (d*)
        """
        logger.info("Governance Engine evaluating the adversarial protocol constraints...")
        
        # Example rule from specification:
        # if v < 0.5 or a > 0.7: reject decision (override to benign/safe, or opposite)
        # Here we assume a "rejected" intrusion decision means we default to Benign (0) or flag an Error (-1).
        
        if v < 0.5 or a > 0.7 or t < 0.3:
            logger.warning(f"Governance OVERRIDE: Decision {d_e} REJECTED due to poor systemic metrics (v={v:.2f}, a={a:.2f}, t={t:.2f})")
            return -1 # Represents an overridden/rejected decision
        else:
            logger.info(f"Governance APPROVED: Decision {d_e} satisfies structural separation bounds.")
            return d_e


class CARSystem:
    """
    Central Orchestrator for the Constitutional AI Runtime (IDS Variant)
    Enforces the pipeline: x -> Executor -> Validator -> Challenger -> Auditor -> Governance -> Output
    """
    def __init__(self, executor, validator, challenger, auditor):
        self.executor = executor
        self.validator = validator
        self.challenger = challenger
        self.auditor = auditor
        self.governance = GovernanceEngine()
        logger.info("Initialized CARSystem: Executor -> Validator -> Challenger -> Auditor -> Governance")

    def process(self, x: torch.Tensor):
        logger.info(f"\n--- Starting CAR Protocol for input packet tensor ---")
        # 1. Execute
        d_e, c_e = self.executor.predict(x)
        
        # 2. Validate
        v = self.validator.check(x, d_e)
        
        # 3. Challenge
        x_adv, a = self.challenger.attack(x, d_e)
        
        # 4. Audit
        t, anomaly = self.auditor.evaluate(x, d_e, v, a)
        
        if anomaly:
            logger.error("AUDIT ALERT: System anomaly detected! High risk of optimization collapse.")
            
        # 5. Govern
        d_final = self.governance.decide(d_e, v, a, t)
        
        logger.info(f"--- Completed CAR Protocol. Final Decision = {d_final} ---\n")
        return d_final
