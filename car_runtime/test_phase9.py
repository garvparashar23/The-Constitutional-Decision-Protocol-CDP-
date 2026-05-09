import logging
from knowledge_graph.graph_engine import ConstitutionalGraph
from rl.policy_optimizer import PolicyOptimizer

logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger("Phase9Test")

def test_advanced_research():
    logger.info("="*60)
    logger.info(" PHASE 9: ADVANCED RESEARCH FEATURES ")
    logger.info("="*60)
    
    # 1. Knowledge Graph Governance
    logger.info("\n--- 1. Testing Constitutional Knowledge Graph ---")
    graph = ConstitutionalGraph()
    
    # Add Nodes
    graph.add_node("Right_To_Privacy", "rights")
    graph.add_node("National_Security_Act", "duties")
    graph.add_node("Surveillance_Policy_X", "risks")
    
    # Add Edges
    graph.add_edge("National_Security_Act", "Surveillance_Policy_X", "supports")
    graph.add_edge("Right_To_Privacy", "Surveillance_Policy_X", "conflicts_with")
    
    # Export
    summary = graph.export_summary()
    logger.info(summary)
    
    # 2. Constitutional RL
    logger.info("\n--- 2. Testing Constitutional RL Agent ---")
    optimizer = PolicyOptimizer()
    optimizer.train(episodes=500)
    optimizer.evaluate_learned_policy()

if __name__ == "__main__":
    test_advanced_research()
