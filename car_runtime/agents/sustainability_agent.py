from .base_agent import ConstitutionalAgent

class SustainabilityAgent(ConstitutionalAgent):
    def __init__(self):
        super().__init__(
            name="SustainabilityAgent", 
            priority=6,
            utility_function="minimize(environmental_impact) & maximize(long_term_viability)",
            principles=["Ensure ecological balance", "Promote sustainable resource usage"],
            reasoning_style="long-term, systems thinking"
        )
        
    def evaluate(self, proposal, context):
        carbon_footprint = getattr(proposal, 'carbon_footprint', 0.0)
        if carbon_footprint > 0.5:
            return {
                "score": 0.3,
                "objection": "Long-term sustainability threatened by high carbon footprint.",
                "amendment": {"carbon_footprint": 0.1}
            }
        return {"score": 1.0, "objection": "None", "amendment": None}
        
    def generate_counterargument(self, proposal, objections, context):
        return "Short term economic gains cited by other agents must account for negative externalities in the long-term simulation horizon."
