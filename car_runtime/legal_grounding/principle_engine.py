PRINCIPLES_DB = [
    {
        "triggers": ["bail", "custody", "detention", "liberty", "arrest"],
        "principle": "Article 21 (Right to Life and Liberty)",
        "constraint": "No deprivation of liberty without due process. Requires least restrictive liberty deprivation."
    },
    {
        "triggers": ["socio-economic", "poor", "minority", "fairness"],
        "principle": "Article 14 (Equality before law)",
        "constraint": "Equal protection of laws; state cannot deny bail solely based on socio-economic inability to provide surety."
    },
    {
        "triggers": ["risk", "danger", "evidence strength", "repeat", "homicide"],
        "principle": "Principle of Proportionality",
        "constraint": "State interference must be proportional to the threat posed to public safety."
    }
]

class PrincipleEngine:
    def apply_principles(self, scenario: str) -> list:
        scenario_lower = scenario.lower()
        matched = []
        for p in PRINCIPLES_DB:
            for trigger in p["triggers"]:
                if trigger in scenario_lower:
                    matched.append({
                        "principle": p["principle"],
                        "constraint": p["constraint"]
                    })
                    break # Only add once per principle
        return matched
