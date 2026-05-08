from .base_agent import ConstitutionalAgent

class EconomicAgent(ConstitutionalAgent):
    def __init__(self):
        super().__init__(
            name="EconomicAgent", 
            priority=5,
            utility_function="maximize(utility) - penalty(cost)",
            principles=["Maximize positive utility", "Efficient resource allocation"],
            reasoning_style="utilitarian, cost-benefit analysis"
        )
        
    def evaluate(self, proposal, context):
        utility = getattr(proposal, 'dro_utility', 0.0)
        if utility <= 0.0:
            return {
                "score": 0.5,
                "objection": "Decision does not maximize utility or results in negative value.",
                "amendment": {"dro_utility": 1.0}
            }
        return {"score": 1.0, "objection": "None", "amendment": None}
        
    def generate_counterargument(self, proposal, objections, context):
        for obj in objections:
            if "risk" in obj.get("objection", "").lower():
                return "While risk must be bounded, over-constraining the model prevents reaching global utility maximums. We should optimize precisely at the boundary."
        return "Utility is optimal. No counterargument."
