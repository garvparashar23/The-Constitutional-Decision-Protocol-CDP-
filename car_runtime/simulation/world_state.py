import logging

logger = logging.getLogger("WorldState")

class WorldState:
    """
    Tracks the dynamic macro-level metrics of the simulated world.
    All metrics are bounded between 0.0 and 100.0.
    """
    def __init__(self):
        self.social_stability = 50.0
        self.fairness_evolution = 50.0
        self.risk_escalation = 10.0
        self.trust_levels = 50.0
        self.economic_impact = 50.0
        self.epoch = 0

    def _bound(self, val: float) -> float:
        return max(0.0, min(100.0, val))

    def apply_impact(self, stability_delta: float, fairness_delta: float, risk_delta: float, trust_delta: float, econ_delta: float):
        """Applies mathematical deltas to the state metrics."""
        self.social_stability = self._bound(self.social_stability + stability_delta)
        self.fairness_evolution = self._bound(self.fairness_evolution + fairness_delta)
        self.risk_escalation = self._bound(self.risk_escalation + risk_delta)
        self.trust_levels = self._bound(self.trust_levels + trust_delta)
        self.economic_impact = self._bound(self.economic_impact + econ_delta)

    def advance_epoch(self):
        self.epoch += 1

    def to_dict(self):
        return {
            "epoch": self.epoch,
            "social_stability": round(self.social_stability, 2),
            "fairness_evolution": round(self.fairness_evolution, 2),
            "risk_escalation": round(self.risk_escalation, 2),
            "trust_levels": round(self.trust_levels, 2),
            "economic_impact": round(self.economic_impact, 2)
        }
