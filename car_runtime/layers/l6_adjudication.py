import z3
import hmac
import hashlib
import random
import asyncio
import logging
from typing import List, Dict, Any
from core.types import SanitizedProposal, TokenizedDecision, Constraint
from layers.adversarial_scoring import AdversarialScoreboard

logger = logging.getLogger("L6_AdjudicationEngine")

# A secure secret key for the HMAC token generation (in prod, this is in an env var isolated from D)
VALIDATOR_SECRET = b"ASCR_VALIDATOR_STRICT_ISOLATION_KEY_99812"

class AdjudicationAgent:
    def __init__(self, agent_id: str):
        self.agent_id = agent_id
        self.solver = z3.Solver()
        # Layer 6: Randomization & Unpredictability
        # Each agent applies a slight randomized epsilon to constraints to break D's ability to perfectly predict the boundary
        self.random_epsilon = random.uniform(-0.01, 0.01)

    async def verify(self, prop: SanitizedProposal, constraints: List[Constraint]) -> bool:
        await asyncio.sleep(0.01) # Simulated network isolation delay
        self.solver.push()
        
        # Map isolated features to Z3 logic
        risk = z3.Real('predicted_risk')
        fairness = z3.Real('predicted_fairness')
        utility = z3.Real('utility')
        
        # Add system constraints
        for c in constraints:
            if c.is_hard:
                self.solver.add(c.logic_expr)
                
        # Stochastic validation boundary:
        # Instead of parsing the raw operator (which is lost after Z3 compilation),
        # we inject the epsilon into the parsed values themselves to represent noisy sensor logic.
        noisy_risk = prop.predicted_risk + self.random_epsilon
        noisy_fairness = prop.predicted_fairness + self.random_epsilon
        
        # Strictly evaluate only the SanitizedProposal with stochastic noise
        self.solver.add(risk == z3.RealVal(noisy_risk))
        self.solver.add(fairness == z3.RealVal(noisy_fairness))
        self.solver.add(utility == z3.RealVal(prop.dro_utility))
        
        result = self.solver.check()
        self.solver.pop()
        
        return (result == z3.sat)

class AdjudicationEngine:
    """
    ASCR Layer 6: Adversarial Validator & Cryptographic Token Issuer
    """
    def __init__(self, num_agents: int = 4):
        self.agents = [AdjudicationAgent(f"Validator_{i}") for i in range(num_agents)]
        self.scoreboard = AdversarialScoreboard()
        
    def _generate_approval_token(self, prop: SanitizedProposal) -> str:
        """Generates a cryptographic execution token that the finalization layer will strictly require."""
        payload = f"{prop.id}:{prop.action}:{prop.predicted_risk}".encode('utf-8')
        return hmac.new(VALIDATOR_SECRET, payload, hashlib.sha256).hexdigest()

    async def _async_verify_all(self, prop: SanitizedProposal, constraints: List[Constraint]) -> int:
        tasks = [agent.verify(prop, constraints) for agent in self.agents]
        results = await asyncio.gather(*tasks)
        return sum(results)

    def execute_consensus(self, proposals: List[SanitizedProposal], original_proposals: Dict[str, DecisionProposal], constraints: List[Constraint]) -> List[TokenizedDecision]:
        logger.info(f"Validator: Examining {len(proposals)} proposals via BFT. (D's gradients and state are completely hidden)")
        valid_decisions = []
        
        f = (len(self.agents) - 1) // 3
        required_signatures = len(self.agents) - f
        
        for prop in proposals:
            votes = asyncio.run(self._async_verify_all(prop, constraints))
            
            if votes >= required_signatures:
                # Adversarial Objective: D wins, V loses
                self.scoreboard.record_pass()
                
                # Issue cryptographic token
                token = self._generate_approval_token(prop)
                
                # Repackage into TokenizedDecision for Execution layer
                decision = TokenizedDecision(
                    original_proposal=original_proposals[prop.id],
                    approval_token=token
                )
                valid_decisions.append(decision)
                logger.info(f"Validator: Proposal {prop.id} mathematically verified. Cryptographic Approval Token issued.")
            else:
                # Adversarial Objective: V wins, D loses
                self.scoreboard.record_rejection()
                logger.warning(f"Validator: Proposal {prop.id} REJECTED. Mathematical constraints violated.")
                
        return valid_decisions
