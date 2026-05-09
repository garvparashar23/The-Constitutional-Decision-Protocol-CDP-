import logging
from explainability.reasoning_visualizer import ReasoningVisualizer

logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger("ExplainabilityTest")

def test_explainability():
    logger.info("="*50)
    logger.info("TESTING PHASE 6: EXPLAINABILITY & PROOFS")
    logger.info("="*50)
    
    # 1. Test Acceptance Proof
    class MockDecision:
        def __init__(self):
            self.id = "DEC_9921"
            
    decision = MockDecision()
    acceptance_proof = ReasoningVisualizer.generate_acceptance_proof(decision)
    
    logger.info("--- Acceptance Proof Graph ---")
    logger.info(acceptance_proof)
    
    # 2. Test Rejection Proof
    debate_logs = [
        {"agent_name": "SafetyAgent", "objection": "Action causes unmitigated physical risk.", "score": 0.2},
        {"agent_name": "EthicsAgent", "objection": "Discriminates against protected class.", "score": 0.3}
    ]
    
    rejection_proof = ReasoningVisualizer.generate_rejection_proof(
        proposal_id="PROP_8834",
        debate_logs=debate_logs,
        z3_verified=False
    )
    
    logger.info("--- Rejection Proof Graph ---")
    logger.info(rejection_proof)

if __name__ == "__main__":
    test_explainability()
