import logging

logger = logging.getLogger("DebateManager")

class DebateManager:
    def __init__(self):
        self.history = []

    def log_debate_round(self, proposal_id, agent_name, objection, proposed_amendment, score, counterargument=None):
        entry = {
            "proposal_id": proposal_id,
            "agent": agent_name,
            "objection": objection,
            "counterargument": counterargument,
            "amendment": proposed_amendment,
            "score": score
        }
        self.history.append(entry)
        logger.debug(f"Debate Logged | Agent: {agent_name} | Score: {score}")
        
    def get_consensus_score(self, proposal_id):
        scores = [entry["score"] for entry in self.history if entry["proposal_id"] == proposal_id]
        if not scores:
            return 0.0
        consensus = sum(scores) / len(scores)
        logger.info(f"Consensus Evolution tracked. Current score: {consensus:.2f}")
        return consensus
    
    def get_objections(self, proposal_id):
        return [entry for entry in self.history if entry["proposal_id"] == proposal_id and entry["objection"] != "None"]
