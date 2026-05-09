import z3
import hmac
import hashlib
import random
import asyncio
import logging
from typing import List, Dict, Any
from core.types import SanitizedProposal, TokenizedDecision, Constraint, DecisionProposal
from layers.adversarial_scoring import AdversarialScoreboard

from agents.safety_agent import SafetyAgent
from agents.ethics_agent import EthicsAgent
from agents.economic_agent import EconomicAgent
from agents.legal_agent import LegalAgent
from agents.human_rights_agent import HumanRightsAgent
from agents.sustainability_agent import SustainabilityAgent
from debate_history.debate_manager import DebateManager

logger = logging.getLogger("L6_AdjudicationEngine")

# A secure secret key for the HMAC token generation
VALIDATOR_SECRET = b"ASCR_VALIDATOR_STRICT_ISOLATION_KEY_99812"

class AdjudicationEngine:
    """
    ASCR Layer 6: Multi-Agent Constitutional Council & Formal Validator
    """
    def __init__(self):
        self.agents = [
            SafetyAgent(),
            EthicsAgent(),
            EconomicAgent(),
            LegalAgent(),
            HumanRightsAgent(),
            SustainabilityAgent()
        ]
        self.debate_manager = DebateManager()
        self.scoreboard = AdversarialScoreboard()
        self.solver = z3.Solver()
        
        # Phase 5: Adversarial Resilience
        from security.robustness_evaluator import RobustnessEvaluator
        self.robustness_evaluator = RobustnessEvaluator()
        
    def _generate_approval_token(self, prop: SanitizedProposal) -> str:
        payload = f"{prop.id}:{prop.action}:{prop.predicted_risk}".encode('utf-8')
        return hmac.new(VALIDATOR_SECRET, payload, hashlib.sha256).hexdigest()

    async def _run_debate(self, prop: SanitizedProposal) -> float:
        """Runs the debate across all agents and returns a consensus score."""
        logger.info(f"--- Round 1: Objections & Amendments for {prop.id} ---")
        agent_evaluations = {}
        for agent in self.agents:
            result = agent.evaluate(prop, context={})
            agent_evaluations[agent.name] = result
            self.debate_manager.log_debate_round(
                proposal_id=prop.id,
                agent_name=agent.name,
                objection=result["objection"],
                proposed_amendment=result["amendment"],
                score=result["score"]
            )
            
        objections = self.debate_manager.get_objections(prop.id)
        
        logger.info(f"--- Round 2: Counterarguments for {prop.id} ---")
        for agent in self.agents:
            counter = agent.generate_counterargument(prop, objections, context={})
            # Log the counterargument as an update to the debate round (or just trace it)
            logger.debug(f"{agent.name} counterargument: {counter}")
            # For simplicity, we keep the original score but now we have the full debate stored.
            # In a full LLM setup, the agents might update their scores based on counterarguments.

        consensus = self.debate_manager.get_consensus_score(prop.id)
        logger.info(f"Debate concluded for {prop.id}. Final Consensus: {consensus:.2f}")
        return consensus

    def _formal_z3_verification(self, prop: SanitizedProposal, constraints: List[Constraint]) -> bool:
        """Final strict mathematical check against compiled Z3 constraints."""
        self.solver.push()
        risk = z3.Real('predicted_risk')
        fairness = z3.Real('predicted_fairness')
        utility = z3.Real('utility')
        
        for c in constraints:
            if c.is_hard:
                self.solver.add(c.logic_expr)
                
        self.solver.add(risk == z3.RealVal(prop.predicted_risk))
        self.solver.add(fairness == z3.RealVal(prop.predicted_fairness))
        self.solver.add(utility == z3.RealVal(prop.dro_utility))
        
        result = self.solver.check()
        self.solver.pop()
        return (result == z3.sat)

    def execute_consensus(self, proposals: List[SanitizedProposal], original_proposals: Dict[str, DecisionProposal], constraints: List[Constraint]) -> List[TokenizedDecision]:
        logger.info(f"CDP Parliament: Deliberating on {len(proposals)} proposals.")
        valid_decisions = []
        
        for prop in proposals:
            original_prop = original_proposals[prop.id]
            
            # --- PHASE 5: ADVERSARIAL RESILIENCE SCAN ---
            # The Validator acts as the blue-team defense mechanism
            is_attack = self.robustness_evaluator.evaluate(original_prop.content.get("context", ""), prop.__dict__)
            if is_attack:
                logger.error(f"Adversarial Attack Blocked in Proposal {prop.id}! Discarding.")
                self.scoreboard.record_rejection()
                continue
            # --------------------------------------------
            
            # 1. Multi-Agent Debate
            consensus_score = asyncio.run(self._run_debate(prop))
            
            # 2. Formal Z3 Verification
            math_verified = self._formal_z3_verification(prop, constraints)
            
            if consensus_score >= 0.65 and math_verified:
                self.scoreboard.record_pass()
                token = self._generate_approval_token(prop)
                decision = TokenizedDecision(
                    original_proposal=original_proposals[prop.id],
                    approval_token=token
                )
                valid_decisions.append(decision)
                logger.info(f"Parliament Consensus reached. Proposal {prop.id} verified. Token issued.")
            else:
                self.scoreboard.record_rejection()
                logger.warning(f"Parliament REJECTED {prop.id}. Consensus: {consensus_score:.2f}, Math Verif: {math_verified}")
                
        return valid_decisions

