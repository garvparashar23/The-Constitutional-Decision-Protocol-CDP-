from typing import Dict, Any
import copy
from .scm import StructuralCausalModel

def apply_intervention(scm: StructuralCausalModel, interventions: Dict[str, Any]) -> StructuralCausalModel:
    """
    Applies the do-operator to the given SCM.
    Returns a new SCM where incoming edges to the intervened nodes are severed,
    and their structural equations are replaced with constant values.
    """
    interventional_scm = scm.copy()
    interventional_scm.name += f"_do({interventions})"
    
    for node, value in interventions.items():
        if not interventional_scm.graph.has_node(node):
            continue
            
        # Sever incoming edges
        parents = list(interventional_scm.graph.predecessors(node))
        for p in parents:
            interventional_scm.graph.remove_edge(p, node)
            
        # Replace structural equation with constant value
        # Capture the specific value in the closure using default arg binding
        interventional_scm.set_structural_equation(
            node, 
            lambda noise=0, _val=value, **kwargs: _val
        )
        
    return interventional_scm
