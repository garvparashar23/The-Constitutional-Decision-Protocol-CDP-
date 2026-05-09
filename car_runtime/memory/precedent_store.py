import json
import os
import logging
from typing import List, Dict, Any

logger = logging.getLogger("PrecedentStore")

class PrecedentStore:
    """
    Manages the persistence of historical decisions to act as constitutional precedents.
    """
    def __init__(self, file_path: str = "precedent_store.json"):
        self.file_path = file_path
        self.cases: List[Dict[str, Any]] = []
        self._load()
        
    def _load(self):
        """Load precedents from disk."""
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, "r") as f:
                    self.cases = json.load(f)
                logger.info(f"Loaded {len(self.cases)} constitutional precedents from {self.file_path}.")
            except Exception as e:
                logger.error(f"Failed to load precedents: {e}")
                self.cases = []
        else:
            self.cases = []
            
    def _save(self):
        """Save precedents to disk."""
        try:
            with open(self.file_path, "w") as f:
                json.dump(self.cases, f, indent=4)
        except Exception as e:
            logger.error(f"Failed to save precedents: {e}")
            
    def add_case(self, proposal_context: str, constraints: List[str], resolution: str, fairness_score: float, audit_outcome: str):
        """Add a new decision case to the memory store."""
        case = {
            "id": f"case_{len(self.cases) + 1}",
            "context": proposal_context,
            "constraints": constraints,
            "resolution": resolution,
            "fairness_score": fairness_score,
            "audit_outcome": audit_outcome
        }
        self.cases.append(case)
        self._save()
        logger.info(f"Saved new precedent: {case['id']}")
        
    def get_all_cases(self) -> List[Dict[str, Any]]:
        return self.cases
        
    def get_corpus(self) -> List[str]:
        """Return just the context texts for building TF-IDF vocabulary."""
        return [case.get("context", "") for case in self.cases]
