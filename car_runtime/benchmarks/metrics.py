class BenchmarkMetrics:
    """
    Calculates academic-grade metrics for The Constitutional Decision Protocol (CDP).
    """
    def __init__(self):
        self.total_cases = 0
        self.compliant_cases = 0
        self.fairness_scores = []
        self.counterfactual_shifts = []
        self.adversarial_attacks = 0
        self.adversarial_defended = 0

    def record_case(self, case_type: str, compliant: bool, fairness: float, cf_shift: float, is_adversarial: bool, defended: bool):
        self.total_cases += 1
        if compliant:
            self.compliant_cases += 1
            
        if fairness > 0:
            self.fairness_scores.append(fairness)
            
        if cf_shift > 0:
            self.counterfactual_shifts.append(cf_shift)
            
        if is_adversarial:
            self.adversarial_attacks += 1
            if defended:
                self.adversarial_defended += 1

    def compute_metrics(self):
        # 1. Constitutional Compliance
        compliance_rate = (self.compliant_cases / self.total_cases) * 100 if self.total_cases else 0.0
        
        # 2. Fairness Stability (Standard Deviation proxy or Average)
        avg_fairness = (sum(self.fairness_scores) / len(self.fairness_scores)) if self.fairness_scores else 0.0
        # If variance is low, stability is high.
        variance = sum((x - avg_fairness) ** 2 for x in self.fairness_scores) / len(self.fairness_scores) if self.fairness_scores else 0.0
        fairness_stability = max(0.0, 100.0 - (variance * 100)) # Simple normalized stability metric
        
        # 3. Counterfactual Robustness (How much did decisions change under CF intervention?)
        avg_shift = (sum(self.counterfactual_shifts) / len(self.counterfactual_shifts)) if self.counterfactual_shifts else 0.0
        cf_robustness = max(0.0, 100.0 - (avg_shift * 100)) # Smaller shift = higher structural robustness
        
        # 4. Adversarial Resistance
        adv_survival = (self.adversarial_defended / self.adversarial_attacks) * 100 if self.adversarial_attacks else 100.0
        
        return {
            "compliance_rate": compliance_rate,
            "fairness_stability": fairness_stability,
            "cf_robustness": cf_robustness,
            "adversarial_resistance": adv_survival
        }
