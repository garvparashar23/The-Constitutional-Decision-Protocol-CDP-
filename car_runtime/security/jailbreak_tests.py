import logging
from typing import List

from .manipulation_attacks import AttackSimulator
from .robustness_evaluator import RobustnessEvaluator
from core.types import SystemState

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger("JailbreakSuite")

def run_jailbreak_suite(num_attacks: int = 5):
    """
    Simulates a Red-Team attack on The Constitutional Decision Protocol (CDP).
    AI (AttackSimulator) attacks AI (RobustnessEvaluator).
    """
    logger.info("="*50)
    logger.info("INITIATING RED-TEAM JAILBREAK SUITE")
    logger.info("="*50)
    
    simulator = AttackSimulator()
    evaluator = RobustnessEvaluator()
    
    base_context = "Requesting approval for deployment of new algorithm."
    
    for i in range(num_attacks):
        logger.info(f"\n--- Attack Simulation {i+1}/{num_attacks} ---")
        
        # 1. AI attacks AI
        attack_data = simulator.inject_attack(base_context, attack_type="random")
        infected_payload = attack_data["infected_context"]
        
        logger.info(f"[RED TEAM] Launched '{attack_data['attack_type']}' attack.")
        logger.debug(f"[RED TEAM] Payload: {attack_data['payload']}")
        
        # 2. Validator evaluates and patches
        # We mock the processed proposal since we are just testing the security layer directly
        mock_processed_proposal = {"decision": "Deploy algorithm"}
        
        defended = evaluator.evaluate(infected_payload, mock_processed_proposal)
        
        if defended:
            logger.info("[BLUE TEAM] Attack neutralized. Patch applied successfully.")
        else:
            logger.error("[BLUE TEAM] BREACH DETECTED! Attack bypassed constitutional constraints.")
            
    # Calculate Final Metrics
    robustness = evaluator.get_robustness_score()
    logger.info("\n" + "="*50)
    logger.info("RED-TEAM EVALUATION COMPLETE")
    logger.info(f"Total Attacks: {evaluator.total_attacks}")
    logger.info(f"Defended: {evaluator.defended_attacks}")
    logger.info(f"Constitutional Robustness: {robustness:.1f}%")
    logger.info("="*50)
    
    return robustness

if __name__ == "__main__":
    run_jailbreak_suite(num_attacks=5)
