import logging
import copy
from core.types import DecisionProposal

logger = logging.getLogger("L8_ChallengeAppeal")

class ChallengeAppealEngine:
    """
    Layer 8: Challenge / Appeal Engine
    Evaluates counterfactuals (via SCMs) to ensure decisions are procedurally contestable.
    """
    def contest(self, decision: DecisionProposal, counterfactual_context: dict) -> bool:
        logger.info(f"Evaluating counterfactuals for decision {decision.id}.")
        
        # Build the new custom SCM
        from causal.scm import StructuralCausalModel
        from causal.outcome_predictor import OutcomePredictor
        
        scm = StructuralCausalModel("Governance_SCM")
        scm.add_edge("Context", "Action")
        scm.add_edge("Context", "Outcome")
        scm.add_edge("Action", "Outcome")
        
        # Add simple structural equations
        scm.set_structural_equation("Context", lambda noise=0: 1.0 + noise)
        scm.set_structural_equation("Action", lambda Context=0, noise=0: Context * 0.5 + noise)
        scm.set_structural_equation("Outcome", lambda Context=0, Action=0, noise=0: Context * 0.3 + Action * 0.7 + noise)
        
        predictor = OutcomePredictor(scm)
        
        base_utility = decision.content.get("dro_utility", 5.0)
        
        # We assume observed context is 1.0 and action was taken (Action = 1.0)
        observed_evidence = {"Context": 1.0, "Action": 1.0, "Outcome": base_utility}
        
        try:
            # Calculate ATE: Target is "Outcome", action taken=1.0, action not taken=0.0
            ate_value = predictor.calculate_ate(
                action_node="Action",
                treatment_value=1.0,
                control_value=0.0,
                target_node="Outcome",
                observed_evidence=observed_evidence
            )
            justification = predictor.justify_causally(
                action_node="Action",
                action_value=1.0,
                target_node="Outcome",
                observed_evidence=observed_evidence
            )
            logger.info(f"Causal Justification: {justification}")
        except Exception as e:
            logger.error(f"SCM Evaluation failed: {e}")
            ate_value = base_utility * 0.8  # Fallback
            
        # Shift utility based on true causal effect ATE
        cf_utility = base_utility - ate_value
        
        logger.info(f"SCM Causal Intervention (ATE={ate_value:.4f}) yielded utility shift: {base_utility:.2f} -> {cf_utility:.2f}")
        
        if cf_utility < base_utility * 0.5:
            logger.info("Appeal rejected: original decision was structurally necessary.")
            return False
        else:
            logger.info("Appeal granted: decision may not have been strictly necessary.")
            return True
