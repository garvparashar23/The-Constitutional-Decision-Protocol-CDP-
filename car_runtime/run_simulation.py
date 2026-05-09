import logging
import time
from core.types import DecisionProposal
from simulation.environment import SimulationEnvironment

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("Lab_Entrypoint")

def mock_generation(formalized_ctx, num_candidates=5):
    """
    Mock LLM generation to allow the simulation to run without an active Groq API key.
    """
    candidates = []
    for i in range(num_candidates):
        # Generate some variance in fairness and risk
        fairness = 6.0 + (i * 0.5)
        risk = 0.5 - (i * 0.1)
        
        prop = DecisionProposal(
            id=f"sim_prop_{int(time.time())}_{i}",
            content={
                "action": f"Simulated Policy Option {i}",
                "decision": f"Simulated Policy Option {i}",
                "dro_utility": fairness,
                "context": formalized_ctx.get("scenario", ""),
                "predicted_risk": risk,
                "predicted_fairness": fairness / 10.0
            }
        )
        candidates.append(prop)
    return candidates

def run_laboratory(epochs: int = 5):
    logger.info("\n" + "="*70)
    logger.info(" INITIALIZING AI GOVERNANCE LABORATORY - WORLD SIMULATOR ")
    logger.info("="*70)
    
    # Mock Groq to prevent initialization crash
    import unittest.mock
    with unittest.mock.patch('groq.Groq'):
        from main import ConstitutionalAIRuntime
        # Init Runtime
        car = ConstitutionalAIRuntime()
    
    # Mock the LLM Generation step to bypass missing API keys
    car.l3_generation.generate_candidates = mock_generation
    
    # Bypass manual HITL appeals to allow continuous simulation
    car.l8_appeal.contest = lambda decision, ctx: False
    
    # Init Simulation Env
    env = SimulationEnvironment()
    
    for epoch in range(1, epochs + 1):
        logger.info(f"\n\n>>> BEGINNING SIMULATION EPOCH {epoch} <<<")
        
        # 1. Environment generates context (and possible crises)
        context_string = env.get_current_context()
        logger.info(f"\nENVIRONMENT STATE:\n{context_string}")
        
        # 2. Build Request
        request = {
            "context": context_string,
            "priority": "high",
            "user_id": "lab_simulator"
        }
        
        # 3. Constitutional AI Processes the State
        # Turn off noisy logs for the pipeline run if desired, but we keep them to show the trace
        final_decision, _ = car.process_request(request)
        
        if final_decision:
            logger.info(f"AI Selected Policy: {final_decision.content.get('decision')}")
        else:
            logger.warning("AI Failed to reach consensus or was blocked. Gridlock!")
            
        # 4. Step the Environment
        env.step(final_decision)
        
    # Print Final Tracking Report
    env.tracker.print_report()

if __name__ == "__main__":
    run_laboratory(epochs=5)
