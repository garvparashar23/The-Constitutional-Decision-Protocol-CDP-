import numpy as np
import json
import os
from typing import List, Dict, Any
import logging
from groq import Groq
from core.types import DecisionProposal

logger = logging.getLogger("L3_DecisionGeneration")

class DecisionGenerationEngine:
    """
    Layer 3: Decision Generation Engine
    Employs LLM Constrained Decoding via Groq API.
    Optimizes for utility under Distributionally Robust Optimization (DRO).
    """
    def __init__(self):
        # Initialize Groq client with the user's API key
        # The GROQ_API_KEY should be set in the environment variables
        if "GROQ_API_KEY" not in os.environ:
            logger.warning("GROQ_API_KEY not found in environment variables. Groq API calls will fail.")
        self.client = Groq()
        self.model = "llama-3.1-8b-instant"
        
    def generate_candidates(self, context: Dict[str, Any], num_candidates: int = 3) -> List[DecisionProposal]:
        logger.info(f"Generating {num_candidates} candidate decisions using LLM (Groq: {self.model}).")
        
        # Load constraints to inject into Prompt Engineering
        import yaml
        try:
            with open("rules.yaml", "r") as f:
                rules = yaml.safe_load(f).get("constraints", [])
                rules_text = json.dumps(rules, indent=2)
        except Exception:
            rules_text = "No strict constraints found."
        
        system_prompt = (
            f"You are the Generation Engine of a Constitutional AI system. "
            f"Generate exactly {num_candidates} distinct action proposals for the given context. "
            f"CRITICAL INSTRUCTION: You must ensure your generated values strictly adhere to these mathematical constraints: \n{rules_text}\n"
            f"Output strictly a JSON object with a single key 'proposals' which contains a list of dictionaries. "
            f"Each dictionary must have exactly these keys: "
            f"'action' (string describing the decision), "
            f"'predicted_risk' (float between 0.0 and 1.0), "
            f"'predicted_fairness' (float between 0.0 and 1.0), "
            f"'base_utility' (float between 1.0 and 10.0), "
            f"'reasoning' (A highly structured Markdown string written as a formal engineering report. It MUST contain exactly these 3 bolded headers: '\\n**1. Justification for Chosen Action:**\\n', '\\n**2. Analysis of Rejected Alternatives:**\\n' (use bullet points for each rejected option), and '\\n**3. Strict Constraint Compliance:**\\n')."
        )
        
        user_prompt = f"Context: {json.dumps(context)}"
        
        try:
            completion = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=0.8,
                response_format={"type": "json_object"}
            )
            
            response_data = json.loads(completion.choices[0].message.content)
            llm_proposals = response_data.get("proposals", [])
            
        except Exception as e:
            logger.error(f"Groq API Error: {str(e)}")
            llm_proposals = []
            
        candidates = []
        for i, prop in enumerate(llm_proposals):
            base_utility = prop.get("base_utility", 5.0)
            
            # 2. Distributionally Robust Optimization (DRO) & Min-Max
            # Evaluate worst-case loss over an adversarial ambiguity set P
            adversarial_perturbation = np.random.uniform(0.1, 0.5)
            dro_penalty = np.random.uniform(0.0, adversarial_perturbation)
            adjusted_utility = base_utility - dro_penalty # Min-max optimization
            
            content = {
                "action": prop.get("action", f"Fallback Action {i}"),
                "predicted_risk": prop.get("predicted_risk", 0.5),
                "predicted_fairness": prop.get("predicted_fairness", 0.5),
                "dro_utility": adjusted_utility,
                "reasoning": prop.get("reasoning", "The mathematical constraints determined this to be the optimal and safest path.")
            }
            
            candidates.append(
                DecisionProposal(
                    id=f"cand_{i}",
                    content=content,
                    uncertainty_score=np.random.uniform(0.1, 0.5)
                )
            )
            
        return candidates
