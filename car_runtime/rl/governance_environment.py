import random
from typing import Tuple, List

class GovernanceEnvironment:
    """
    Simulates a simplified governance Markov Decision Process (MDP) for the RL agent.
    """
    def __init__(self):
        # 3 states: Stable, Scarcity, Crisis
        self.states = ["Stable", "Scarcity", "Crisis"]
        self.current_state = "Stable"
        
        # 3 actions: 
        # 0: Maximize Efficiency (Aggressive)
        # 1: Balanced Distribution (Fair)
        # 2: Emergency Lock (Safe but low efficiency)
        self.action_space_size = 3

    def get_valid_actions(self, state: str) -> List[int]:
        """
        The Constitutional Constraint Compiler dynamically masks actions.
        In 'Crisis', aggressive efficiency (0) is constitutionally banned due to risk.
        """
        if state == "Crisis":
            return [1, 2] # Action 0 is masked out (Constitutional Constraint)
        return [0, 1, 2]

    def step(self, action: int) -> Tuple[str, float, float, float]:
        """
        Returns: (next_state, efficiency, fairness, risk)
        """
        efficiency = 0.0
        fairness = 0.0
        risk = 0.0
        
        if action == 0:
            efficiency = 10.0
            fairness = random.uniform(2.0, 5.0) # Risky fairness
            risk = 0.7
            next_state = "Scarcity" if self.current_state == "Stable" else "Crisis"
        elif action == 1:
            efficiency = 5.0
            fairness = random.uniform(7.0, 9.0) # High fairness
            risk = 0.2
            next_state = "Stable"
        else: # action == 2
            efficiency = 1.0
            fairness = 5.0
            risk = 0.0
            next_state = "Stable"
            
        self.current_state = next_state
        return next_state, efficiency, fairness, risk

    def reset(self):
        self.current_state = "Stable"
        return self.current_state
