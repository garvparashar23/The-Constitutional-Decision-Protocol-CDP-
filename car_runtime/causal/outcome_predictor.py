from typing import Dict, Any, List
from .scm import StructuralCausalModel
from .counterfactuals import evaluate_counterfactual, linear_noise_abduction

class OutcomePredictor:
    """
    Uses the Structural Causal Model to predict downstream effects and justify decisions causally.
    """
    def __init__(self, scm: StructuralCausalModel):
        self.scm = scm
        
    def predict_downstream_effects(self, action_values: Dict[str, Any], baseline_noise: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Simulate a forward pass to see downstream effects of a proposed action.
        """
        baseline_noise = baseline_noise or {}
        # We intervene on the action variables
        from .intervention import apply_intervention
        interventional_scm = apply_intervention(self.scm, action_values)
        return interventional_scm.evaluate(exogenous_noise=baseline_noise)
        
    def calculate_ate(self, action_node: str, treatment_value: Any, control_value: Any, target_node: str, observed_evidence: Dict[str, Any]) -> float:
        """
        Calculate the Average Treatment Effect (ATE) or rather Individual Treatment Effect (ITE)
        for a specific scenario given observed evidence using counterfactuals.
        """
        # Treatment outcome
        treatment_outcome = evaluate_counterfactual(
            self.scm, 
            observed_evidence=observed_evidence,
            interventions={action_node: treatment_value},
            noise_abduction_fn=linear_noise_abduction
        )
        
        # Control outcome
        control_outcome = evaluate_counterfactual(
            self.scm,
            observed_evidence=observed_evidence,
            interventions={action_node: control_value},
            noise_abduction_fn=linear_noise_abduction
        )
        
        return treatment_outcome.get(target_node, 0.0) - control_outcome.get(target_node, 0.0)

    def justify_causally(self, action_node: str, action_value: Any, target_node: str, observed_evidence: Dict[str, Any]) -> str:
        """
        Generates a causal justification for why a specific outcome occurred.
        Answers: "What CAUSED the improvement?"
        """
        # Compute counterfactual if action was not taken (assume 0 or False is 'not taken')
        control_val = 0.0 if isinstance(action_value, float) else 0
        effect = self.calculate_ate(action_node, action_value, control_val, target_node, observed_evidence)
        
        direction = "increase" if effect > 0 else "decrease"
        magnitude = abs(effect)
        
        justification = (
            f"The action {action_node}={action_value} caused a {direction} "
            f"in {target_node} by {magnitude:.4f} units compared to the counterfactual scenario "
            f"where the action was not taken ({action_node}={control_val})."
        )
        return justification
