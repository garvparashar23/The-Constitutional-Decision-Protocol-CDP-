import networkx as nx
from typing import Dict, Callable, Any, List

class StructuralCausalModel:
    """
    A Structural Causal Model (SCM) represented as a Directed Acyclic Graph (DAG).
    Variables are nodes, causal relationships are directed edges.
    Each node has a structural equation defining its value based on its parents and exogenous noise.
    """
    def __init__(self, name: str = "SCM"):
        self.name = name
        self.graph = nx.DiGraph()
        self.structural_equations: Dict[str, Callable] = {}
        
    def add_node(self, node_name: str):
        """Add a variable to the causal model."""
        self.graph.add_node(node_name)
        
    def add_edge(self, parent: str, child: str):
        """Add a directed causal link from parent to child."""
        if not self.graph.has_node(parent):
            self.add_node(parent)
        if not self.graph.has_node(child):
            self.add_node(child)
        self.graph.add_edge(parent, child)
        
    def set_structural_equation(self, node_name: str, equation: Callable):
        """
        Set the structural equation for a node.
        The equation should accept kwargs matching the names of the parent nodes,
        plus an optional 'noise' parameter.
        """
        if not self.graph.has_node(node_name):
            self.add_node(node_name)
        self.structural_equations[node_name] = equation

    def get_parents(self, node_name: str) -> List[str]:
        return list(self.graph.predecessors(node_name))
        
    def is_dag(self) -> bool:
        return nx.is_directed_acyclic_graph(self.graph)
        
    def evaluate(self, exogenous_noise: Dict[str, Any], interventions: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Evaluate the SCM given exogenous noise (and optional interventions).
        Returns the computed values for all nodes.
        """
        if not self.is_dag():
            raise ValueError("SCM is not a DAG. Cannot evaluate with cycles.")
            
        interventions = interventions or {}
        state = {}
        
        # Traverse in topological order to ensure parents are computed before children
        for node in nx.topological_sort(self.graph):
            if node in interventions:
                state[node] = interventions[node]
            else:
                parents = self.get_parents(node)
                parent_values = {p: state[p] for p in parents}
                noise = exogenous_noise.get(node, 0.0)
                
                if node in self.structural_equations:
                    try:
                        state[node] = self.structural_equations[node](**parent_values, noise=noise)
                    except TypeError:
                        # Fallback if structural equation signature is unexpected
                        state[node] = self.structural_equations[node](parent_values, noise)
                else:
                    # If no equation is provided, assume it's purely driven by noise
                    state[node] = noise
                    
        return state
        
    def copy(self):
        """Return a deep copy of the SCM."""
        new_scm = StructuralCausalModel(self.name + "_copy")
        new_scm.graph = self.graph.copy()
        new_scm.structural_equations = self.structural_equations.copy()
        return new_scm
