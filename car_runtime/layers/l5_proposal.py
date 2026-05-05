import networkx as nx
from typing import List
import logging
from core.types import DecisionProposal

logger = logging.getLogger("L5_ProposalLayer")

class DecisionProposalLayer:
    """
    Layer 5: Decision Proposal Layer
    Packages valid candidates with their provenance, causal graphs, 
    and uncertainty estimates before deep Adjudication.
    """
    def package_proposals(self, candidates: List[DecisionProposal]) -> List[DecisionProposal]:
        logger.info("Packaging proposals with Structural Causal Models (SCMs).")
        
        for cand in candidates:
            # Generate a minimal SCM / Causal Graph for contestability later
            scm = nx.DiGraph()
            scm.add_node("Context")
            scm.add_node("Action", value=cand.content["action"])
            scm.add_node("Outcome", utility=cand.content["dro_utility"])
            
            scm.add_edge("Context", "Action")
            scm.add_edge("Action", "Outcome")
            
            # Attach a DOT formatted graph for DoWhy Causal Inference
            cand.causal_graph = scm
            cand.causal_dot = "digraph {Context -> Action; Action -> Outcome; Context -> Outcome;}"
            
            # Recalculate deep uncertainty
            cand.uncertainty_score += 0.05
            
        return candidates
