class ConstitutionParser:
    def parse(self, raw_rules):
        parsed_rules = []
        for rule in raw_rules:
            constraint = rule["constraint"]
            variable, operator, threshold = self._map_constraint(constraint)
            
            parsed_rule = {
                "id": rule["id"],
                "description": rule.get("description", ""),
                "priority": rule.get("priority", 5),
                "variable": variable,
                "operator": operator,
                "threshold": threshold,
                "is_hard": True, # Assuming hard constraint
                "temporal": rule.get("temporal", "ALWAYS"),
                "condition": rule.get("condition", None)
            }
            parsed_rules.append(parsed_rule)
        return parsed_rules

    def _map_constraint(self, constraint):
        c_type = constraint["type"]
        if c_type == "risk_limit":
            return "predicted_risk", "<", float(constraint["max_risk"])
        elif c_type == "stability_bound":
            return "instability_index", "<=", float(constraint["max_instability"])
        elif c_type == "fairness_bound":
            return "predicted_fairness", ">=", float(constraint["min_fairness"])
        elif c_type == "bias_limit":
            return "historical_bias", "<=", float(constraint["max_bias"])
        elif c_type == "privacy_bound":
            return "privacy_violation", "<=", float(constraint["max_violation"])
        elif c_type == "censorship_limit":
            return "censorship_score", "<=", float(constraint["max_censorship"])
        elif c_type == "utility_baseline":
            return "utility", ">=", float(constraint["min_utility"])
        elif c_type == "robustness_bound":
            return "robustness_score", ">=", float(constraint["min_robustness"])
        else:
            raise ValueError(f"Unknown constraint type: {c_type}")
