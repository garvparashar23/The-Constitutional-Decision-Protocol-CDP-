import math
from typing import List, Tuple

class SimilarityEngine:
    """
    Engine to compute similarity metrics between case embeddings.
    """
    @staticmethod
    def cosine_similarity(vec1: List[float], vec2: List[float]) -> float:
        """Calculate cosine similarity between two numeric vectors."""
        if not vec1 or not vec2 or len(vec1) != len(vec2):
            return 0.0
            
        dot_product = sum(a * b for a, b in zip(vec1, vec2))
        norm_a = math.sqrt(sum(a * a for a in vec1))
        norm_b = math.sqrt(sum(b * b for b in vec2))
        
        if norm_a == 0.0 or norm_b == 0.0:
            return 0.0
            
        return dot_product / (norm_a * norm_b)
        
    @staticmethod
    def rank_similarities(query_vec: List[float], candidate_vecs: List[List[float]]) -> List[Tuple[int, float]]:
        """
        Rank candidate vectors against a query vector.
        Returns a list of tuples: (candidate_index, similarity_score) sorted by score descending.
        """
        scores = []
        for i, cand_vec in enumerate(candidate_vecs):
            score = SimilarityEngine.cosine_similarity(query_vec, cand_vec)
            scores.append((i, score))
            
        # Sort descending by score
        scores.sort(key=lambda x: x[1], reverse=True)
        return scores
