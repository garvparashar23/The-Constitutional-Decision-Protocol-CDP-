import torch
import torch.nn as nn
import logging

logger = logging.getLogger("Phase1_Executor")

class IDSExecutor(nn.Module):
    """
    Phase 1: Executor (E)
    An LSTM/Transformer hybrid stub for Intrusion Detection.
    Objective: Maximize prediction accuracy.
    """
    def __init__(self, input_dim=20, hidden_dim=64):
        super(IDSExecutor, self).__init__()
        self.lstm = nn.LSTM(input_dim, hidden_dim, batch_first=True)
        self.fc = nn.Linear(hidden_dim, 1)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        # x shape: (batch, seq_len, features)
        out, _ = self.lstm(x)
        # Take the last sequence output
        last_out = out[:, -1, :]
        logits = self.fc(last_out)
        prob = self.sigmoid(logits)
        return prob

    def predict(self, x: torch.Tensor):
        """
        Input: data (x)
        Output: decision (d_e), confidence (c_e)
        """
        self.eval()
        with torch.no_grad():
            prob = self.forward(x).item()
            
        decision = 1 if prob >= 0.5 else 0 # 1 = Intrusion, 0 = Benign
        confidence = prob if decision == 1 else (1.0 - prob)
        
        logger.info(f"Executor Output: Decision={decision}, Confidence={confidence:.4f}")
        return decision, confidence
