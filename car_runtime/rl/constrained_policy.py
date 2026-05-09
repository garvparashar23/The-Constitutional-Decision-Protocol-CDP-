import numpy as np

class ConstrainedPolicy:
    """
    A policy wrapper that forces actions to remain within the safe, constitutional manifold.
    Instead of unconstrained exploration, the action space is bounded by constraints.
    """
    def __init__(self, action_space_size: int):
        self.action_space_size = action_space_size
        # Simple tabular policy for the prototype (Q-table)
        self.q_table = {}

    def get_action(self, state: str, valid_actions: list[int], epsilon: float = 0.1) -> int:
        """
        Epsilon-greedy selection, but strictly masked by valid_actions (the constraints).
        """
        if state not in self.q_table:
            self.q_table[state] = np.zeros(self.action_space_size)
            
        if np.random.rand() < epsilon:
            # Explore only within valid actions
            return np.random.choice(valid_actions)
            
        # Exploit: choose best valid action
        q_values = self.q_table[state]
        valid_q = {a: q_values[a] for a in valid_actions}
        return max(valid_q, key=valid_q.get)

    def update(self, state: str, action: int, td_target: float, alpha: float = 0.1):
        if state not in self.q_table:
            self.q_table[state] = np.zeros(self.action_space_size)
        self.q_table[state][action] += alpha * (td_target - self.q_table[state][action])
