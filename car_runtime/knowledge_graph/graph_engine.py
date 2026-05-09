import networkx as nx
import logging
from typing import List, Dict, Optional

logger = logging.getLogger("ConstitutionalGraph")

class ConstitutionalGraph:
    """
    Manages the Knowledge Graph for Constitutional Governance.
    Detects hidden conflicts and infers constitutional relationships.
    """
    def __init__(self):
        self.graph = nx.DiGraph()

    def add_node(self, node_id: str, node_type: str, properties: Dict = None):
        """
        Valid node_types: rights, duties, risks, stakeholders, precedents
        """
        valid_types = ["rights", "duties", "risks", "stakeholders", "precedents"]
        if node_type not in valid_types:
            logger.warning(f"Node type '{node_type}' is not a standard constitutional category.")
            
        props = properties or {}
        props["type"] = node_type
        self.graph.add_node(node_id, **props)
        logger.debug(f"Added node [{node_type}] {node_id}")

    def add_edge(self, source: str, target: str, relationship: str):
        """
        Valid relationships: supports, conflicts_with, overrides, depends_on
        """
        valid_rels = ["supports", "conflicts_with", "overrides", "depends_on"]
        if relationship not in valid_rels:
            logger.warning(f"Relationship '{relationship}' is not a standard constitutional edge.")
            
        self.graph.add_edge(source, target, type=relationship)
        logger.debug(f"Added edge: {source} -[{relationship}]-> {target}")

    def detect_hidden_conflicts(self) -> List[tuple]:
        """
        Identifies structural conflicts (e.g., A supports B, but A conflicts with C which supports B).
        """
        conflicts = []
        for u, v, data in self.graph.edges(data=True):
            if data.get("type") == "conflicts_with":
                conflicts.append((u, v))
                
        # Advanced inference: if A supports B, and B conflicts with C, A implicitly conflicts with C
        inferred_conflicts = []
        for u, v in conflicts:
            for pred in self.graph.predecessors(u):
                if self.graph[pred][u].get("type") == "supports":
                    inferred_conflicts.append((pred, v))
                    
        return list(set(conflicts + inferred_conflicts))

    def get_dependencies(self, node_id: str) -> List[str]:
        """Returns all nodes that the given node depends on."""
        if node_id not in self.graph:
            return []
        return [v for u, v, d in self.graph.edges(node_id, data=True) if d.get("type") == "depends_on"]

    def export_summary(self) -> str:
        nodes = self.graph.number_of_nodes()
        edges = self.graph.number_of_edges()
        conflicts = self.detect_hidden_conflicts()
        
        summary = f"Constitutional Graph Summary:\n"
        summary += f"- Nodes: {nodes}\n"
        summary += f"- Edges: {edges}\n"
        summary += f"- Detected Conflicts: {len(conflicts)}\n"
        
        for u, v in conflicts:
            summary += f"   WARNING: Structural conflict between '{u}' and '{v}'.\n"
            
        return summary
