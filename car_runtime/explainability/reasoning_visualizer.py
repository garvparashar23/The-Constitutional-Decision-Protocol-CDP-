import json

class ReasoningVisualizer:
    @staticmethod
    def export_proof_tree(proof_tree, filepath):
        with open(filepath, 'w') as f:
            json.dump(proof_tree.to_dict(), f, indent=4)

    @staticmethod
    def export_constraint_graph(graph, filepath):
        with open(filepath, 'w') as f:
            json.dump(graph.get_graph_data(), f, indent=4)
