import torch
import torch.nn as nn
import logging

logger = logging.getLogger("Phase2_Validator")

class IDSValidator(nn.Module):
    """
    Phase 2: Validator (V)
    A Secondary Classifier (MLP) trained with a different objective.
    Objective: Enforce consistency and structural constraints.
    """
    def __init__(self, input_dim=20, hidden_dim=32):
        super(IDSValidator, self).__init__()
        # Takes the raw input features + the executor's decision (d_e)
        self.fc1 = nn.Linear(input_dim + 1, hidden_dim)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_dim, 1)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x, d_e):
        # Flatten x if it's a sequence
        x_flat = x[:, -1, :] # Take last timestep
        
        # Concat decision
        d_e_tensor = torch.tensor([[d_e]], dtype=torch.float32)
        combined = torch.cat((x_flat, d_e_tensor), dim=1)
        
        hidden = self.relu(self.fc1(combined))
        v_logits = self.fc2(hidden)
        return self.sigmoid(v_logits)

    def check(self, x: torch.Tensor, d_e: int) -> float:
        """
        Input: (x, d_e)
        Output: validity score (v \\in [0,1])
        """
        self.eval()
        with torch.no_grad():
            v_score = self.forward(x, d_e).item()
            
        logger.info(f"Validator Output: Validity Score (v) = {v_score:.4f}")
        return v_score
