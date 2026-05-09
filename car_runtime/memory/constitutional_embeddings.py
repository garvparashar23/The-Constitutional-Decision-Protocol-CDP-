import math
import collections
import re
from typing import List, Dict

class TFIDFEmbedder:
    """
    A lightweight, pure Python TF-IDF embedding engine.
    Used to convert text (like a decision proposal context) into a numerical vector
    for similarity comparisons without needing external NLP libraries.
    """
    def __init__(self):
        self.vocab: Dict[str, int] = {}
        self.idf: Dict[str, float] = {}
        self.fitted = False
        
    def _tokenize(self, text: str) -> List[str]:
        # Simple lowercase word tokenization
        if not text:
            return []
        text = str(text).lower()
        return re.findall(r'\b[a-z0-9]+\b', text)
        
    def fit(self, corpus: List[str]):
        """Build the vocabulary and compute IDF from a corpus of texts."""
        doc_count = len(corpus)
        df = collections.defaultdict(int)
        
        for text in corpus:
            tokens = set(self._tokenize(text))
            for token in tokens:
                df[token] += 1
                
        # Build vocab mapping
        self.vocab = {word: idx for idx, word in enumerate(sorted(df.keys()))}
        
        # Compute IDF
        self.idf = {
            word: math.log((1 + doc_count) / (1 + count)) + 1
            for word, count in df.items()
        }
        self.fitted = True
        
    def transform(self, text: str) -> List[float]:
        """Convert a single string into a TF-IDF vector based on the fitted vocab."""
        if not self.fitted:
            # If not fitted, we can't transform properly, but we'll return an empty vector
            # or just build a single-doc vocab inline if forced (not ideal).
            return []
            
        tokens = self._tokenize(text)
        tf = collections.Counter(tokens)
        total_tokens = len(tokens) if tokens else 1
        
        vector = [0.0] * len(self.vocab)
        
        # Calculate TF-IDF per token
        sum_sq = 0.0
        for token, count in tf.items():
            if token in self.vocab:
                idx = self.vocab[token]
                term_frequency = count / total_tokens
                idf_weight = self.idf.get(token, 1.0)
                val = term_frequency * idf_weight
                vector[idx] = val
                sum_sq += val * val
                
        # L2 Normalization
        if sum_sq > 0:
            norm = math.sqrt(sum_sq)
            vector = [v / norm for v in vector]
            
        return vector

    def transform_corpus(self, corpus: List[str]) -> List[List[float]]:
        return [self.transform(text) for text in corpus]
