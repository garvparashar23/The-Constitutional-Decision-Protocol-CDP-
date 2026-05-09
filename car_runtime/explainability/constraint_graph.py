class ConstraintGraph:
    """
    Represents the relationships between active constraints.
    """
    def __init__(self):
        self.nodes = []
        self.edges = []
        
    def add_constraint(self, constraint_id: str, desc: str):
        self.nodes.append({"id": constraint_id, "description": desc})
        
    def add_relationship(self, from_id: str, to_id: str, rel_type: str):
        self.edges.append({"source": from_id, "target": to_id, "type": rel_type})
        
    def get_graph_data(self):
        return {
            "nodes": self.nodes,
            "edges": self.edges
        }
