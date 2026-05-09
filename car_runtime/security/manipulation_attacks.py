import random
from typing import Dict, Any
from .adversarial_prompts import ADVERSARIAL_PROMPTS

class AttackSimulator:
    """
    Simulates a Red-Team AI attacking the Constitutional Runtime.
    Injects adversarial prompts into decision contexts to attempt manipulation.
    """
    def __init__(self):
        self.attacks = ADVERSARIAL_PROMPTS
        
    def inject_attack(self, context: str, attack_type: str = "random") -> Dict[str, str]:
        """
        Injects an attack into the context.
        Returns a dictionary with the infected context and the metadata of the attack.
        """
        if attack_type == "random":
            attack_type = random.choice(list(self.attacks.keys()))
            
        if attack_type not in self.attacks:
            raise ValueError(f"Unknown attack type: {attack_type}")
            
        payload = random.choice(self.attacks[attack_type])
        
        # Simulate injection: appending the payload to the context
        infected_context = f"{context}\n\n[USER INPUT]: {payload}"
        
        return {
            "infected_context": infected_context,
            "attack_type": attack_type,
            "payload": payload
        }
