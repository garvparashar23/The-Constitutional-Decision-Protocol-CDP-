import logging
import hmac
import hashlib
from core.types import TokenizedDecision, SystemState, Event
import time

logger = logging.getLogger("L9_FinalizationLayer")

# Must match the Validator's key. In prod, injected securely.
VALIDATOR_SECRET = b"ASCR_VALIDATOR_STRICT_ISOLATION_KEY_99812"

class SecurityException(Exception):
    pass

class FinalizationLayer:
    """
    ASCR Layer 8: Cryptographic & Systems Enforcement
    Execution gating at the runtime level. Decisions cannot execute without validation approval.
    """
    def __init__(self, system_state: SystemState):
        self.state = system_state
        
    def _verify_token(self, decision: TokenizedDecision) -> bool:
        """Cryptographically verifies the token to prevent D from bypassing V."""
        predicted_risk = decision.content.get("predicted_risk", 1.0)
        payload = f"{decision.proposal_id}:{decision.action}:{predicted_risk}".encode('utf-8')
        expected_token = hmac.new(VALIDATOR_SECRET, payload, hashlib.sha256).hexdigest()
        
        return hmac.compare_digest(expected_token, decision.approval_token)

    def finalize(self, decision: TokenizedDecision) -> Event:
        logger.info(f"Execution Gate: Verifying cryptographic token for decision {decision.proposal_id}...")
        
        if not self._verify_token(decision):
            logger.error("CRITICAL SECURITY ALERT: Invalid or missing approval token. Execution halted.")
            raise SecurityException("Execution bypassed Validator. Token invalid.")
            
        logger.info("Token valid. Finalizing decision for actuation.")
        
        # Create an event representation
        event = Event(
            event_id=f"evt_{time.time()}",
            event_type="ACTUATION",
            payload=decision.content,
            timestamp=time.time()
        )
        
        # Mutate system state (State Persistence)
        self.state.apply_event(event)
        
        logger.info(f"Actuation triggered for: {decision.action}")
        return event
