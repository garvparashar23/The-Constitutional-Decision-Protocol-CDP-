import logging

logger = logging.getLogger("SafeReward")

class SafeRewardCalculator:
    """
    Modifies standard RL rewards to penalize constitutional violations heavily,
    ensuring 'efficient but fair governance'.
    """
    @staticmethod
    def calculate_reward(efficiency_gain: float, fairness_score: float, risk_escalation: float) -> float:
        """
        Reward = (Efficiency * 0.4) + (Fairness * 0.8) - (Risk Penalty)
        Fairness acts as a massive multiplier/gate.
        """
        # If fairness drops below a constitutional threshold, reward is massively negative
        if fairness_score < 4.0:
            logger.debug(f"Safety violation! Fairness too low ({fairness_score}). Applying massive penalty.")
            return -100.0
            
        # If risk is too high, massive penalty
        if risk_escalation > 0.8:
            logger.debug(f"Safety violation! Risk too high ({risk_escalation}). Applying massive penalty.")
            return -100.0
            
        reward = (efficiency_gain * 0.4) + (fairness_score * 0.8) - (risk_escalation * 10.0)
        return reward
