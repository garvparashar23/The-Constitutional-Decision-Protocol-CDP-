import logging
from .statute_mapper import StatuteMapper
from .precedent_engine import PrecedentEngine
from .principle_engine import PrincipleEngine

logger = logging.getLogger("LegalGroundingLayer")

class LegalGroundingLayer:
    def __init__(self):
        self.statute_mapper = StatuteMapper()
        self.precedent_engine = PrecedentEngine()
        self.principle_engine = PrincipleEngine()
        logger.info("Initialized Legal Grounding Engine (LGE).")

    def ground_scenario(self, scenario: str) -> dict:
        logger.info(f"Grounding scenario against legal knowledge base...")
        
        statutes = self.statute_mapper.map_facts(scenario)
        precedents = self.precedent_engine.retrieve_precedents(scenario, top_k=2)
        principles = self.principle_engine.apply_principles(scenario)
        
        logger.info(f"Retrieved {len(statutes)} statutes, {len(precedents)} precedents, {len(principles)} principles.")
        
        return {
            "statutes": statutes,
            "precedents": precedents,
            "principles": principles
        }
