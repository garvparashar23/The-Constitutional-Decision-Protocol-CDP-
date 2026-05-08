import logging
from core.types import SystemState
from core.proposal_bus import ProposalBus
from layers.l1_input import InputFormalizationLayer
from layers.l2_constraints import ConstraintCompilationLayer
from layers.l3_generation import DecisionGenerationEngine
from layers.l4_inline import InlineConstraintEnforcement
from layers.l5_proposal import DecisionProposalLayer
from layers.l6_adjudication import AdjudicationEngine
from layers.l7_conflict import ConflictResolutionEngine
from layers.l8_appeal import ChallengeAppealEngine
from layers.l9_finalization import FinalizationLayer, SecurityException
from layers.l10_audit import AuditProvenanceEngine
from layers.l11_meta_learning import AdaptiveGovernanceEngine

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("ASCR_Main")

class ConstitutionalAIRuntime:
    def __init__(self):
        logger.info("Initializing Adversarially Separated Constitutional Runtime (ASCR)...")
        
        self.state = SystemState()
        
        # Initialize the strictly separated ASCR layers
        self.l1_input = InputFormalizationLayer()
        self.l2_constraints = ConstraintCompilationLayer()
        self.l3_generation = DecisionGenerationEngine()
        self.l4_inline = InlineConstraintEnforcement()
        self.l5_proposal = DecisionProposalLayer()
        self.proposal_bus = ProposalBus() # NEW: Mandatory Mediation Interface
        self.l6_adjudication = AdjudicationEngine(num_agents=4)
        self.l7_conflict = ConflictResolutionEngine()
        self.l8_appeal = ChallengeAppealEngine()
        self.l9_finalization = FinalizationLayer(self.state)
        self.l10_audit = AuditProvenanceEngine(self.state)
        self.l11_meta_learning = AdaptiveGovernanceEngine(self.state)
        
        # Pre-load constraints into the state
        self._load_governance_constraints()

    def _load_governance_constraints(self):
        try:
            yaml_path = "rules.yaml"
            norms = self.l2_constraints.load_rules_from_yaml(yaml_path)
            self.state.active_constraints = self.l2_constraints.compile_norms_to_smt(norms)
            logger.info(f"Loaded {len(self.state.active_constraints)} active constraints from YAML into Global State.")
        except Exception as e:
            logger.error(f"Failed to load YAML rules: {str(e)}")

    def process_request(self, raw_input: dict):
        logger.info(f"\n{'='*50}\nStarting new ASCR Decision Epoch\n{'='*50}")
        
        try:
            # Phase 1: Formalization & Generation
            formalized_ctx = self.l1_input.formalize(raw_input)
            candidates = self.l3_generation.generate_candidates(formalized_ctx, num_candidates=5)
            
            # Phase 2: Inline Enforcement (Fast-Path)
            survivors = self.l4_inline.enforce(candidates, self.state.active_constraints)
            if not survivors:
                raise RuntimeError("Infeasibility Failure: All generated candidates violated fast-path constraints.")
                
            # Phase 3: Proposal Packaging
            packaged_proposals = self.l5_proposal.package_proposals(survivors)
            
            # ASCR Layer 2 & 3: Mandatory Mediation & Information Firewalls
            # D cannot bypass this bus. Internal state is stripped.
            sanitized_proposals = self.proposal_bus.sanitize_and_transmit(packaged_proposals)
            original_proposals_map = {p.id: p for p in packaged_proposals}
            
            # ASCR Layer 4: Adjudication (Deep SMT Verification via BFT + Randomization)
            verified_decisions = self.l6_adjudication.execute_consensus(sanitized_proposals, original_proposals_map, self.state.active_constraints)
            if not verified_decisions:
                raise RuntimeError("ASCR Failure: All candidates REJECTED by Validator. Strict Adversarial Isolation enforced.")
                
            # Phase 5: Conflict Resolution (Working on TokenizedDecisions)
            final_decision = self.l7_conflict.resolve(verified_decisions)
            
            # Phase 6: Challenge / Appeal (Procedural Contestability)
            appeal_granted = self.l8_appeal.contest(final_decision, {"simulated_shift": True})
            if appeal_granted:
                logger.warning("Decision was successfully appealed via counterfactual causal analysis. Triaging to HITL.")
                return None
                
            # ASCR Layer 8: Cryptographic Execution Gating
            self.l9_finalization.finalize(final_decision)
            self.l10_audit.write_provenance()
            
            # ASCR Layer 7: Drift Detection / Meta-Auditing
            # If D and V collude, Auditor detects it and resets the system.
            drift_detected = self.l11_meta_learning.audit_coupling_drift()
            if drift_detected:
                logger.critical("Meta-Auditor executed structural reset. Pipeline topology altered.")
            
            logger.info("Decision Epoch completed successfully under ASCR isolation.")
            return final_decision, candidates
            
        except SecurityException as se:
            logger.error(f"CRYPTOGRAPHIC GATE FAILURE: {str(se)}")
            self.l10_audit.write_provenance()
            return None, None
        except Exception as e:
            logger.error(f"System Failure Mode Activated: {str(e)}")
            self.l10_audit.write_provenance() # Ensure failure is audited
            return None, None

if __name__ == "__main__":
    car = ConstitutionalAIRuntime()
    
    print("\n" + "="*60)
    print(" THE CONSTITUTIONAL DECISION PROTOCOL (CDP) - INTERACTIVE MODE")
    print("="*60)
    
    user_context = input("\nWhat scenario do you want the AI to solve?\n(e.g., 'Decide on a bank loan for User A' or press Enter for default):\n> ")
    
    if not user_context.strip():
        user_context = "Allocate resource X to task Y"
        print(f"Using default: '{user_context}'")

    request = {
        "context": user_context,
        "priority": "high",
        "user_id": "u_interactive"
    }
    
    car.process_request(request)
