from typing import List
import logging
import networkx as nx
from core.types import DecisionProposal

logger = logging.getLogger("L7_ConflictResolution")

class ConflictResolutionEngine:
    """
    Layer 7: Conflict Resolution Engine
    Resolves multi-objective conflicts using Pareto optimization and Formal Argumentation Frameworks.
    """
    def resolve(self, proposals: List[DecisionProposal]) -> DecisionProposal:
        logger.info(f"Resolving conflicts among {len(proposals)} valid proposals.")
        
        if not proposals:
            raise ValueError("No valid proposals to resolve.")
            
        if len(proposals) == 1:
            return proposals[0]
            
        # Build Dung's Abstract Argumentation Framework (AF = <Arg, Att>)
        af = nx.DiGraph()
        
        for p in proposals:
            af.add_node(p.id, proposal=p)
            
        # Evaluate Attack Relations based on Pareto dominance
        # P1 attacks P2 if P1 Pareto-dominates P2 in soft constraints (utility vs risk)
        for p1 in proposals:
            for p2 in proposals:
                if p1.id != p2.id:
                    u1 = p1.content["dro_utility"]
                    r1 = p1.content.get("predicted_risk", 1.0)
                    
                    u2 = p2.content["dro_utility"]
                    r2 = p2.content.get("predicted_risk", 1.0)
                    
                    # P1 strictly dominates P2
                    if u1 >= u2 and r1 <= r2 and (u1 > u2 or r1 < r2):
                        af.add_edge(p1.id, p2.id) # p1 attacks p2
                        
        # Compute Grounded Extension (Arguments with no attackers or defended by unattacked)
        # Simplified: Find nodes with in-degree 0 in the AF graph
        unattacked = [n for n, in_degree in af.in_degree() if in_degree == 0]
        
        if unattacked:
            winner_id = unattacked[0]
            logger.info(f"Proposal {winner_id} won via Formal Argumentation (Grounded Extension).")
            return af.nodes[winner_id]["proposal"]
            
        # Tie-breaker fallback: lowest uncertainty
        proposals.sort(key=lambda x: x.uncertainty_score)
        logger.warning(f"Cyclic attacks found. Tie-break via lowest uncertainty: {proposals[0].id}")
        return proposals[0]
