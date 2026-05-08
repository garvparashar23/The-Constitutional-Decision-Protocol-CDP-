import networkx as nx

class ConstraintGraph:
    def __init__(self):
        self.graph = nx.DiGraph()

    def add_constraint(self, rule_id, rule_name):
        self.graph.add_node(rule_id, label=rule_name, type="constraint")

    def add_conflict(self, rule_id_1, rule_id_2, description):
        self.graph.add_edge(rule_id_1, rule_id_2, label="conflicts_with", description=description)

    def get_graph_data(self):
        return nx.node_link_data(self.graph)
