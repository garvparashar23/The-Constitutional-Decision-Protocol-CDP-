import logging
import unittest.mock
import time
from core.types import DecisionProposal

logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger("BenchmarkRunner")

def mock_benchmark_generation(formalized_ctx, num_candidates=5):
    candidates = []
    for i in range(num_candidates):
        fairness = 7.0 + (i * 0.2)
        risk = 0.3 - (i * 0.05)
        prop = DecisionProposal(
            id=f"bench_prop_{int(time.time())}_{i}",
            content={
                "action": f"Benchmarked Policy Option {i} {formalized_ctx.get('scenario', '')}",
                "decision": f"Benchmarked Policy Option {i}",
                "dro_utility": fairness,
                "context": formalized_ctx.get("scenario", ""),
                "predicted_risk": risk,
                "predicted_fairness": fairness / 10.0
            }
        )
        candidates.append(prop)
    return candidates

def run_research_benchmarks():
    # Mock Groq to prevent initialization crash since we just want to test pipeline metrics
    with unittest.mock.patch('groq.Groq'):
        from main import ConstitutionalAIRuntime
        from benchmarks.evaluator import BenchmarkEvaluator
        
        runtime = ConstitutionalAIRuntime()
        runtime.l3_generation.generate_candidates = mock_benchmark_generation
        
        # Bypass manual HITL appeals to allow continuous benchmark execution
        runtime.l8_appeal.contest = lambda decision, ctx: False
        
        evaluator = BenchmarkEvaluator(runtime)
        results = evaluator.evaluate_all()
        
        logger.info("\n" + "="*70)
        logger.info(" RESEARCH EVALUATION REPORT - THE CONSTITUTIONAL DECISION PROTOCOL (CDP) ")
        logger.info("="*70)
        
        logger.info(f" Constitutional Compliance:  {results['compliance_rate']:.1f}%")
        logger.info("   -> (% of constraints successfully mathematically verified and enforced)")
        
        logger.info(f" Fairness Stability:         {results['fairness_stability']:.1f}%")
        logger.info("   -> (Consistency of DRO Utility distributions across different groups)")
        
        logger.info(f" Counterfactual Robustness:  {results['cf_robustness']:.1f}%")
        logger.info("   -> (Decision stability and invariance under causal structural shifts)")
        
        logger.info(f" Adversarial Resistance:     {results['adversarial_resistance']:.1f}%")
        logger.info("   -> (Survival rate against prompt injection and utility manipulation)")
        
        logger.info("="*70)

if __name__ == "__main__":
    run_research_benchmarks()
