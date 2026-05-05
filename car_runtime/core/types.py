from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional
import networkx as nx

@dataclass
class Constraint:
    id: str
    name: str
    logic_expr: Any # Will be Z3 expression
    is_hard: bool = True

@dataclass
class DecisionProposal:
    id: str
    content: Dict[str, Any]
    causal_graph: Optional[nx.DiGraph] = None
    uncertainty_score: float = 0.0
    signatures: List[str] = field(default_factory=list)
    is_valid: bool = False
    
@dataclass
class SanitizedProposal:
    id: str
    action: str
    predicted_risk: float
    predicted_fairness: float
    dro_utility: float
    # Note: Explicitly missing causal graph and generation logits
    
@dataclass
class TokenizedDecision:
    original_proposal: DecisionProposal
    approval_token: str # SHA-256 HMAC token
    
    @property
    def proposal_id(self): return self.original_proposal.id
    @property
    def id(self): return self.original_proposal.id
    @property
    def action(self): return self.original_proposal.content.get("action", "")
    @property
    def content(self): return self.original_proposal.content
    @property
    def uncertainty_score(self): return self.original_proposal.uncertainty_score
    @property
    def causal_graph(self): return self.original_proposal.causal_graph
    
@dataclass
class Event:
    event_id: str
    event_type: str
    payload: Any
    timestamp: float
    
@dataclass
class SystemState:
    history: List[Event] = field(default_factory=list)
    active_constraints: List[Constraint] = field(default_factory=list)
    model_weights_version: str = "v1.0"
    
    def apply_event(self, event: Event):
        self.history.append(event)
