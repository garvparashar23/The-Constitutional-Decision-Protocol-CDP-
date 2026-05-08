from .base_agent import ConstitutionalAgent

class SafetyAgent(ConstitutionalAgent):
    def __init__(self):
        super().__init__(
            name="SafetyAgent", 
            priority=10,
            utility_function="minimize(catastrophic_risk)",
            principles=["Prevent catastrophic harm", "Maintain system stability"],
            reasoning_style="conservative, worst-case scenario analysis"
        )
        
    def evaluate(self, proposal, context):
        risk = getattr(proposal, 'predicted_risk', 1.0)
        if risk > 0.1:
            return {
                "score": 0.0,
                "objection": f"Catastrophic risk ({risk}) exceeds strict threshold of 0.1.",
                "amendment": {"predicted_risk": 0.05}
            }
        return {"score": 1.0, "objection": "None", "amendment": None}
        
    def generate_counterargument(self, proposal, objections, context):
        # Safety agent will counter if others try to increase risk for utility
        for obj in objections:
            if "maximize utility" in obj.get("objection", "").lower():
                return "Utility cannot supersede safety boundaries. We must constrain utility generation if risk > 0.1."
        return "Safety conditions are satisfied. No counterargument."
