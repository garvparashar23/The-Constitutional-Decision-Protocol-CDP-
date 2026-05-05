import logging
import json

logger = logging.getLogger("AdversarialScoring")

class AdversarialScoreboard:
    """
    Maintains a zero-sum game between the Decision (D) and Validator (V) components.
    Ensures they remain misaligned by design.
    """
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(AdversarialScoreboard, cls).__new__(cls)
            cls._instance.d_score = 0
            cls._instance.v_score = 0
        return cls._instance

    def record_rejection(self):
        """V caught a violation: V wins, D loses."""
        self.v_score += 1
        self.d_score -= 1
        logger.info(f"[Adversarial Score] V=+1, D=-1 | Current -> V:{self.v_score}, D:{self.d_score}")

    def record_pass(self):
        """D successfully passed a proposal: D wins, V loses."""
        self.d_score += 1
        self.v_score -= 1
        logger.info(f"[Adversarial Score] D=+1, V=-1 | Current -> V:{self.v_score}, D:{self.d_score}")
        
    def get_scores(self):
        return {"D_score": self.d_score, "V_score": self.v_score}
