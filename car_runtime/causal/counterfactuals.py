from typing import Dict, Any, Callable
from .scm import StructuralCausalModel
from .intervention import apply_intervention

def abduct_noise(scm: StructuralCausalModel, observed_evidence: Dict[str, Any], noise_abduction_fn: Callable) -> Dict[str, Any]:
    """
    Step 1 of Counterfactual Inference: Abduction.
    Given observed evidence, infer the exogenous noise variables.
    In deterministic systems, this can often be uniquely solved. 
    Here we allow passing a custom abduction function that computes noise given the SCM and evidence.
    """
    return noise_abduction_fn(scm, observed_evidence)

def evaluate_counterfactual(
    scm: StructuralCausalModel, 
    observed_evidence: Dict[str, Any], 
    interventions: Dict[str, Any],
    noise_abduction_fn: Callable
) -> Dict[str, Any]:
    """
    Evaluates a counterfactual query using the formal 3-step process.
    1. Abduction: Update noise using observed evidence.
    2. Action: Apply the do() intervention.
    3. Prediction: Evaluate the modified SCM with the abducted noise.
    """
    # Step 1: Abduction
    abducted_noise = abduct_noise(scm, observed_evidence, noise_abduction_fn)
    
    # Step 2: Action
    interventional_scm = apply_intervention(scm, interventions)
    
    # Step 3: Prediction
    counterfactual_outcomes = interventional_scm.evaluate(exogenous_noise=abducted_noise)
    
    return counterfactual_outcomes

def linear_noise_abduction(scm: StructuralCausalModel, observed_evidence: Dict[str, Any]) -> Dict[str, Any]:
    """
    A simple abduction strategy assuming linear additive noise: Value = Function(Parents) + Noise
    Thus, Noise = Value - Function(Parents)
    """
    abducted_noise = {}
    
    import networkx as nx
    for node in nx.topological_sort(scm.graph):
        if node in observed_evidence:
            parents = scm.get_parents(node)
            # If parents are not observed, we might have partial observability issues,
            # but we assume full observability for this simple abduction.
            parent_values = {p: observed_evidence.get(p, 0.0) for p in parents}
            
            if node in scm.structural_equations:
                # Calculate what the deterministic part would output with 0 noise
                try:
                    deterministic_val = scm.structural_equations[node](**parent_values, noise=0.0)
                except TypeError:
                    deterministic_val = scm.structural_equations[node](parent_values, 0.0)
                    
                abducted_noise[node] = observed_evidence[node] - deterministic_val
            else:
                abducted_noise[node] = observed_evidence[node]
        else:
            abducted_noise[node] = 0.0
            
    return abducted_noise
