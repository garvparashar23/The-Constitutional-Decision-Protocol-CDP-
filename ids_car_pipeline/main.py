import torch
import logging
from executor import IDSExecutor
from validator import IDSValidator
from challenger import IDSChallenger
from auditor import IDSAuditor
from orchestrator import CARSystem

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("IDS_CAR_Main")

def main():
    logger.info("Initializing the Adversarial Modules...")
    
    # Initialize the independent modules (stub models with uninitialized random weights)
    # They have different architectures as specified:
    # Executor: LSTM
    executor = IDSExecutor(input_dim=20, hidden_dim=64)
    # Validator: MLP
    validator = IDSValidator(input_dim=20, hidden_dim=32)
    # Challenger: FGSM generator
    challenger = IDSChallenger(epsilon=0.1)
    # Auditor: Statistical anomaly baseline
    auditor = IDSAuditor(threshold=0.3)
    
    # Initialize the Orchestrator
    car_system = CARSystem(executor, validator, challenger, auditor)
    
    # Create a simulated batch of network traffic (e.g. from CIC-IoT2023)
    # Batch size 1, Sequence Length 10, Features 20
    logger.info("Simulating incoming network traffic tensor (x)...")
    dummy_traffic_x = torch.randn(1, 10, 20)
    
    # Run the Constitutional Decision Protocol (CDP)
    final_decision = car_system.process(dummy_traffic_x)
    
    # Print the outcome
    if final_decision == -1:
        logger.warning("FINAL OUTCOME: The protocol safely REJECTED the Executor's classification due to Governance constraints.")
    elif final_decision == 1:
        logger.info("FINAL OUTCOME: Intrusion Detected and constitutionally verified.")
    else:
        logger.info("FINAL OUTCOME: Benign Traffic constitutionally verified.")

if __name__ == "__main__":
    main()
