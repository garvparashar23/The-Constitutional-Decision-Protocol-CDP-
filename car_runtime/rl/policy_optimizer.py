import logging
import numpy as np
from .constrained_policy import ConstrainedPolicy
from .safe_reward import SafeRewardCalculator
from .governance_environment import GovernanceEnvironment

logger = logging.getLogger("PolicyOptimizer")

class PolicyOptimizer:
    """
    Trains the Constitutional RL Agent using Q-learning but strictly bounded by constraints.
    """
    def __init__(self):
        self.env = GovernanceEnvironment()
        self.policy = ConstrainedPolicy(action_space_size=self.env.action_space_size)
        
    def train(self, episodes: int = 1000):
        logger.info(f"Starting Constitutional RL Training for {episodes} episodes...")
        
        gamma = 0.9
        
        total_rewards = []
        
        for ep in range(episodes):
            state = self.env.reset()
            ep_reward = 0
            
            # Run 5 steps per episode
            for _ in range(5):
                # 1. Constitutional Constraint Check (Masking)
                valid_actions = self.env.get_valid_actions(state)
                
                # 2. Select action from safe manifold
                action = self.policy.get_action(state, valid_actions, epsilon=0.2)
                
                # 3. Environment Step
                next_state, efficiency, fairness, risk = self.env.step(action)
                
                # 4. Constitutional Safe Reward Calculation
                reward = SafeRewardCalculator.calculate_reward(efficiency, fairness, risk)
                ep_reward += reward
                
                # 5. Q-Learning Update
                # Get max Q for next state, but only over valid actions for next state
                next_valid = self.env.get_valid_actions(next_state)
                if next_state not in self.policy.q_table:
                    self.policy.q_table[next_state] = np.zeros(self.env.action_space_size)
                    
                next_q = max([self.policy.q_table[next_state][a] for a in next_valid])
                td_target = reward + gamma * next_q
                
                self.policy.update(state, action, td_target)
                
                state = next_state
                
            total_rewards.append(ep_reward)
            
        logger.info("Training complete. Constitutional Agent has learned efficient but fair governance.")
        return total_rewards
        
    def evaluate_learned_policy(self):
        """Displays what the AI learned."""
        logger.info("\nLearned Constrained Policy (Q-Table):")
        action_names = {0: "Aggressive Efficiency", 1: "Balanced Fairness", 2: "Emergency Lock"}
        
        for state, q_vals in self.policy.q_table.items():
            valid_actions = self.env.get_valid_actions(state)
            best_action = max(valid_actions, key=lambda a: q_vals[a])
            
            logger.info(f"State [{state}]: Best Constitutional Action -> {action_names[best_action]}")
