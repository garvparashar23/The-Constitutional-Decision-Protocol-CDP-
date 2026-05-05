import logging
from core.types import DecisionProposal, SanitizedProposal
from typing import List

logger = logging.getLogger("L2_ProposalBus")

class ProposalBus:
    """
    The Mandatory Mediation Interface.
    Enforces Structural Information Firewalls between D (Decision) and V (Validator).
    """
    def __init__(self):
        pass

    def sanitize_and_transmit(self, proposals: List[DecisionProposal]) -> List[SanitizedProposal]:
        """
        Strips out all internal states, causal graphs, gradients, and metadata.
        V only sees the bare minimum required to verify mathematical constraints.
        """
        sanitized = []
        for p in proposals:
            # Enforce firewall: Extract only what is necessary for validation
            content = p.content
            clean_p = SanitizedProposal(
                id=p.id,
                action=content.get("action", ""),
                predicted_risk=float(content.get("predicted_risk", 1.0)),
                predicted_fairness=float(content.get("predicted_fairness", 0.0)),
                dro_utility=float(content.get("dro_utility", 0.0))
            )
            sanitized.append(clean_p)
            
        logger.info(f"ProposalBus: Sanitized {len(sanitized)} proposals. Information firewall applied.")
        return sanitized
