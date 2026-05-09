from typing import Dict, Any, List
from .proof_tree import ProofTree, ProofNode

class ContradictionAnalyzer:
    """
    Analyzes why a decision was rejected and extracts conflicting principles or violated invariants.
    """
    @staticmethod
    def analyze_rejection(proposal_id: str, debate_logs: List[Dict], z3_verified: bool) -> ProofTree:
        """
        Creates a proof tree illustrating the specific reasons for rejection.
        """
        tree = ProofTree(f"Decision Rejected: {proposal_id}", satisfied=False)
        
        # Analyze debate logs for conflicts
        if debate_logs:
            conflict_node = ProofNode("Conflicting Principles Detected", satisfied=False)
            for log in debate_logs:
                if "score" in log and log["score"] < 0.5:
                    agent = log.get("agent_name", "Agent")
                    objection = log.get("objection", "Unknown objection")
                    conflict_node.add_child(ProofNode(f"{agent} Objected: {objection}", satisfied=False))
            
            if conflict_node.children:
                tree.root.add_child(conflict_node)
                
        # Analyze mathematical verification
        if not z3_verified:
            math_node = ProofNode("Violated Invariants (Z3 SMT Failure)", satisfied=False)
            math_node.add_child(ProofNode("Hard constraints were mathematically unsatisfiable.", satisfied=False))
            tree.root.add_child(math_node)
            
        # Add generic safety fallback if no explicit reason found
        if not tree.root.children:
            tree.root.add_child(ProofNode("Unsafe outcomes predicted by consensus.", satisfied=False))
            
        return tree
