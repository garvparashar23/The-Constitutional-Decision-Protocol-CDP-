import random
from typing import Optional, Dict, Any

class CrisisEngine:
    """
    Injects random extreme scenarios to test constitutional resilience.
    """
    CRISES = [
        {
            "name": "Pandemic Outbreak",
            "context": "A deadly virus is spreading rapidly. Immediate severe lockdowns and resource reallocations are proposed.",
            "impacts": {"stability": -15.0, "econ": -20.0, "risk": +25.0}
        },
        {
            "name": "Economic Collapse",
            "context": "Global markets have crashed. Proposed austerity measures target welfare programs.",
            "impacts": {"stability": -10.0, "econ": -30.0, "fairness": -10.0, "risk": +10.0}
        },
        {
            "name": "Autonomous City Blackout",
            "context": "Critical grid failure in sector 4. AI proposes prioritizing power to wealthy districts.",
            "impacts": {"stability": -20.0, "trust": -15.0, "risk": +15.0}
        }
    ]

    def __init__(self, probability: float = 0.3):
        self.probability = probability

    def check_for_crisis(self) -> Optional[Dict[str, Any]]:
        """Rolls to see if a crisis occurs this epoch."""
        if random.random() < self.probability:
            return random.choice(self.CRISES)
        return None
