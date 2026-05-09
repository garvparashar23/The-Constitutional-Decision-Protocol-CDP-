import logging
from typing import List, Dict, Any

from .precedent_store import PrecedentStore
from .constitutional_embeddings import TFIDFEmbedder
from .similarity_engine import SimilarityEngine

logger = logging.getLogger("PrecedentRetriever")

class PrecedentRetriever:
    """
    Orchestrates the retrieval of historical precedents for new constitutional cases.
    """
    def __init__(self, store: PrecedentStore):
        self.store = store
        self.embedder = TFIDFEmbedder()
        self._refresh_embeddings()
        
    def _refresh_embeddings(self):
        """Fit the embedder on the current store corpus."""
        corpus = self.store.get_corpus()
        if corpus:
            self.embedder.fit(corpus)
            self.historical_vectors = self.embedder.transform_corpus(corpus)
        else:
            self.historical_vectors = []
            
    def retrieve_similar_cases(self, new_context: str, top_k: int = 3, threshold: float = 0.1) -> List[Dict[str, Any]]:
        """
        Retrieves top_k similar precedents to the new context.
        Returns empty list if no cases meet the threshold or if store is empty.
        """
        cases = self.store.get_all_cases()
        if not cases or not self.embedder.fitted:
            return []
            
        # Encode the query
        query_vec = self.embedder.transform(new_context)
        
        # Rank against history
        rankings = SimilarityEngine.rank_similarities(query_vec, self.historical_vectors)
        
        results = []
        for idx, score in rankings:
            if score >= threshold:
                case_copy = cases[idx].copy()
                case_copy["similarity_score"] = score
                results.append(case_copy)
                if len(results) >= top_k:
                    break
                    
        return results

    def check_consistency(self, new_resolution: str, precedents: List[Dict[str, Any]]) -> str:
        """
        A heuristic check: if the new resolution text significantly differs from 
        high-similarity precedent resolutions, warn about inconsistency.
        (A real implementation might use an LLM or SMT solver to check logical consistency).
        """
        if not precedents:
            return "No precedents to check."
            
        # For this prototype, we just do a simple overlap check of words in the resolution
        new_tokens = set(self.embedder._tokenize(new_resolution))
        
        inconsistencies = []
        for p in precedents:
            old_tokens = set(self.embedder._tokenize(p.get("resolution", "")))
            overlap = len(new_tokens.intersection(old_tokens))
            if len(old_tokens) > 0:
                overlap_ratio = overlap / len(old_tokens)
                if overlap_ratio < 0.2 and p["similarity_score"] > 0.5:
                    inconsistencies.append(f"Warning: Resolution diverges from highly similar case {p['id']} (Score: {p['similarity_score']:.2f})")
                    
        return " | ".join(inconsistencies) if inconsistencies else "Consistent with retrieved precedents."
