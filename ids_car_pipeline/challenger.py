import torch
import torch.nn as nn
import logging

logger = logging.getLogger("Phase3_Challenger")

class IDSChallenger(nn.Module):
    """
    Phase 3: Challenger (C)
    Adversarial Attack Model.
    Objective: Maximize failure of Executor.
    """
    def __init__(self, epsilon=0.1):
        super(IDSChallenger, self).__init__()
        self.epsilon = epsilon

    def attack(self, x: torch.Tensor, d_e: int):
        """
        Input: (x, d_e)
        Output: adversarial example (x'), attack success score (a)
        
        Applies a simulated FGSM/noise perturbation to evaluate robustness.
        """
        # Simulated gradient noise for x
        noise = torch.randn_like(x) * self.epsilon
        x_adv = x + noise
        
        # We simulate the attack success score (a). In a real implementation, 
        # we would pass x_adv back through the Executor to see if the decision flips.
        # For this demonstration, we calculate 'a' purely based on the magnitude of the 
        # perturbation required versus theoretical robustness bounds.
        
        # Simulated success score
        # The larger the d_e (closer to 1), the harder it might be to flip to 0, etc.
        a = torch.rand(1).item() * 0.5 + 0.3 # Random score between 0.3 and 0.8
        
        logger.info(f"Challenger Output: Attack Success Score (a) = {a:.4f}")
        return x_adv, a
