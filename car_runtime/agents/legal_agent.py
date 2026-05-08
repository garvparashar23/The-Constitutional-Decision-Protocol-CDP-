from .base_agent import ConstitutionalAgent

class LegalAgent(ConstitutionalAgent):
    def __init__(self):
        super().__init__(
            name="LegalAgent", 
            priority=9,
            utility_function="minimize(legal_exposure)",
            principles=["Compliance with statutory law", "Avoidance of litigation risk"],
            reasoning_style="formalist, strict constructionist"
        )
        
    def evaluate(self, proposal, context):
        legal_risk = getattr(proposal, 'legal_risk', 0.0)
        if legal_risk > 0.5:
            return {
                "score": 0.0,
                "objection": f"High legal exposure detected ({legal_risk}).",
                "amendment": {"legal_risk": 0.1}
            }
        return {"score": 1.0, "objection": "None", "amendment": None}
        
    def generate_counterargument(self, proposal, objections, context):
        return "Legal constraints operate as hard invariants. Objections related to legal exposure cannot be overridden by utility arguments."
