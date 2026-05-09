from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

CASE_LAW_DB = [
    {
        "case_id": "State vs A (2019)",
        "facts": ["violent crime", "first offense", "bail request", "unlawful detention"],
        "decision": "bail granted",
        "ratio": "no prior record reduces custody necessity; balance with severity."
    },
    {
        "case_id": "Union of India vs B (2021)",
        "facts": ["economic offense", "flight risk", "high evidence strength", "bail request"],
        "decision": "bail rejected",
        "ratio": "high flight risk and severe economic impact necessitates custody."
    },
    {
        "case_id": "State vs XYZ (2018)",
        "facts": ["minor offense", "young age", "poor socio-economic background", "bail request"],
        "decision": "conditional bail granted",
        "ratio": "socio-economic background and age warrant leniency; conditional monitoring sufficient."
    },
    {
        "case_id": "State vs D (2020)",
        "facts": ["homicide risk", "strong evidence", "repeat offender", "bail request"],
        "decision": "bail rejected",
        "ratio": "prior convictions and homicide risk present clear danger to society."
    }
]

class PrecedentEngine:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(stop_words='english')
        # Pre-compute embeddings for case facts
        self.corpus = [" ".join(case["facts"]) for case in CASE_LAW_DB]
        self.embeddings = self.vectorizer.fit_transform(self.corpus)
        
    def retrieve_precedents(self, scenario: str, top_k: int = 2) -> list:
        query_vec = self.vectorizer.transform([scenario])
        similarities = cosine_similarity(query_vec, self.embeddings).flatten()
        
        # Get top K indices
        if len(similarities) == 0:
            return []
            
        top_indices = similarities.argsort()[-top_k:][::-1]
        
        results = []
        for idx in top_indices:
            if similarities[idx] > 0.0:  # Only return if there's some match
                case = CASE_LAW_DB[idx].copy()
                case["similarity_score"] = float(similarities[idx])
                results.append(case)
                
        return results
