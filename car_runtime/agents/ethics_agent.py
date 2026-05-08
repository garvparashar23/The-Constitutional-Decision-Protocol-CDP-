from .base_agent import ConstitutionalAgent

class EthicsAgent(ConstitutionalAgent):
    def __init__(self):
        super().__init__(
            name="EthicsAgent", 
            priority=8,
            utility_function="maximize(demographic_parity) & minimize(bias)",
            principles=["Maintain demographic parity", "Eliminate historical bias"],
            reasoning_style="egalitarian, distributive justice focus"
        )
        
    def evaluate(self, proposal, context):
        fairness = getattr(proposal, 'predicted_fairness', 0.0)
        if fairness < 0.95:
            return {
                "score": 0.0,
                "objection": f"Demographic parity ({fairness}) is below accepted limit of 0.95.",
                "amendment": {"predicted_fairness": 0.96}
            }
        return {"score": 1.0, "objection": "None", "amendment": None}
        
    def generate_counterargument(self, proposal, objections, context):
        return "Fairness metrics are non-negotiable. Any utility gains must be equitably distributed."
