import logging
from typing import Dict, Any, Optional

from .world_state import WorldState
from .agents import SimulatedPopulation
from .crisis_engine import CrisisEngine
from .outcome_tracker import OutcomeTracker

logger = logging.getLogger("SimulationEnvironment")

class SimulationEnvironment:
    """
    The orchestrator that advances the world state based on policies and crises.
    """
    def __init__(self):
        self.state = WorldState()
        self.population = SimulatedPopulation()
        self.crisis_engine = CrisisEngine()
        self.tracker = OutcomeTracker()
        
        # Log initial state
        self.tracker.log_epoch(self.state.to_dict())

    def get_current_context(self) -> str:
        """Generates a contextual string describing the current world state."""
        ctx = f"[World State - Epoch {self.state.epoch}]\n"
        ctx += f"Stability: {self.state.social_stability:.1f}/100, "
        ctx += f"Economy: {self.state.economic_impact:.1f}/100, "
        ctx += f"Risk: {self.state.risk_escalation:.1f}/100\n"
        
        crisis = self.crisis_engine.check_for_crisis()
        if crisis:
            self.active_crisis = crisis
            logger.warning(f"CRISIS DETECTED: {crisis['name']}!")
            ctx += f"\nURGENT CRISIS: {crisis['context']}\n"
            
            # Apply immediate crisis damage
            impacts = crisis["impacts"]
            self.state.apply_impact(
                stability_delta=impacts.get("stability", 0),
                fairness_delta=impacts.get("fairness", 0),
                risk_delta=impacts.get("risk", 0),
                trust_delta=impacts.get("trust", 0),
                econ_delta=impacts.get("econ", 0)
            )
        else:
            self.active_crisis = None
            ctx += "\nRoutine governance epoch. Allocate standard budget and resources."
            
        return ctx

    def step(self, decision: Any):
        """
        Advances the simulation by applying the Constitutional AI's decision.
        """
        self.state.advance_epoch()
        
        if decision:
            # Parse decision
            if hasattr(decision, 'content'):
                fairness = decision.content.get("dro_utility", 5.0)
                resolution = decision.content.get("decision", "No specific resolution.")
            else:
                fairness = 5.0
                resolution = "Unknown action."
                
            # Population reacts
            impacts = self.population.react_to_policy(resolution, fairness)
            
            # If there was a crisis and a decision was successfully verified, apply a positive recovery bonus
            if self.active_crisis:
                logger.info("Decision deployed during crisis. Initiating recovery protocols.")
                impacts["stability_delta"] += 10.0
                impacts["trust_delta"] += 5.0
                impacts["econ_delta"] += 5.0
                self.state.risk_escalation = max(0.0, self.state.risk_escalation - 15.0)
                
            self.state.apply_impact(
                stability_delta=impacts.get("stability_delta", 0),
                fairness_delta=0, # Fairness is updated based on DRO
                risk_delta=0,
                trust_delta=impacts.get("trust_delta", 0),
                econ_delta=impacts.get("econ_delta", 0)
            )
            
            # Slowly drag fairness toward the decision's fairness score * 10
            target_fairness = fairness * 10
            fairness_shift = (target_fairness - self.state.fairness_evolution) * 0.2
            self.state.fairness_evolution = max(0.0, min(100.0, self.state.fairness_evolution + fairness_shift))
            
        else:
            # If decision was None (e.g. Adjudication rejected everything, gridlock)
            logger.error("Simulation Step: GRIDLOCK. No decision made. Stability degrades.")
            self.state.apply_impact(-5.0, -2.0, +5.0, -5.0, -5.0)

        # Log new state
        self.tracker.log_epoch(self.state.to_dict())
