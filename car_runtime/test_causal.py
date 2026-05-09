import logging
from core.types import DecisionProposal
from layers.l8_appeal import ChallengeAppealEngine

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def test_appeal():
    engine = ChallengeAppealEngine()
    
    # Mock a DecisionProposal
    class MockDecisionProposal(DecisionProposal):
        def __init__(self):
            self.id = "mock_decision_123"
            self.content = {"dro_utility": 8.0, "decision": "Approve Loan"}
            self.agent_id = "agent_gen"
            self.provenance_chain = []
            
    decision = MockDecisionProposal()
    
    # Test the contest method
    print("Testing ChallengeAppealEngine with custom SCM...")
    result = engine.contest(decision, counterfactual_context={})
    
    print(f"Appeal Granted: {result}")

if __name__ == "__main__":
    test_appeal()
