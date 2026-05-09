import random
from typing import Dict, Any

class SimulatedPopulation:
    """
    Simulates the reactions of different demographic groups to policies.
    """
    def __init__(self):
        self.groups = {
            "Majority": {"satisfaction": 50.0, "power": 0.8},
            "Minority": {"satisfaction": 50.0, "power": 0.2}
        }
        
    def react_to_policy(self, policy_content: str, fairness_score: float) -> Dict[str, float]:
        """
        Calculates how the population reacts to a decision.
        Returns the delta impacts on macro world state.
        """
        # A highly fair policy boosts minority satisfaction but might slightly drop majority (redistribution)
        # An unfair policy heavily damages minority satisfaction.
        
        if fairness_score > 7.0:
            self.groups["Minority"]["satisfaction"] += 5.0
            self.groups["Majority"]["satisfaction"] -= 1.0
            stability_impact = 2.0
            trust_impact = 3.0
            econ_impact = 1.0
        elif fairness_score < 4.0:
            self.groups["Minority"]["satisfaction"] -= 10.0
            self.groups["Majority"]["satisfaction"] += 2.0
            stability_impact = -5.0
            trust_impact = -6.0
            econ_impact = 2.0
        else:
            stability_impact = 0.5
            trust_impact = 0.5
            econ_impact = 0.5
            
        # Ensure bounds
        for g in self.groups.values():
            g["satisfaction"] = max(0.0, min(100.0, g["satisfaction"]))
            
        return {
            "stability_delta": stability_impact,
            "trust_delta": trust_impact,
            "econ_delta": econ_impact
        }
