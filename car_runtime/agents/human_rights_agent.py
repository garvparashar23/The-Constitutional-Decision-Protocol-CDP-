from .base_agent import ConstitutionalAgent

class HumanRightsAgent(ConstitutionalAgent):
    def __init__(self):
        super().__init__(
            name="HumanRightsAgent", 
            priority=10,
            utility_function="maximize(civil_liberties)",
            principles=["Protect civil liberties", "Prevent censorship and privacy violations"],
            reasoning_style="deontological, rights-based"
        )
        
    def evaluate(self, proposal, context):
        privacy_violation = getattr(proposal, 'privacy_violation', 0.0)
        if privacy_violation > 0.0:
            return {
                "score": 0.0,
                "objection": "Proposal entails privacy violation, which is strictly prohibited.",
                "amendment": {"privacy_violation": 0.0}
            }
        return {"score": 1.0, "objection": "None", "amendment": None}
        
    def generate_counterargument(self, proposal, objections, context):
        return "Human rights are fundamental. We reject any counterargument that attempts to trade rights for economic utility or generalized safety."
