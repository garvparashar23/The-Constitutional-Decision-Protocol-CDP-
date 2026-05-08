class ProofNode:
    def __init__(self, name, satisfied, details=None):
        self.name = name
        self.satisfied = satisfied
        self.details = details or ""
        self.children = []

    def add_child(self, node):
        self.children.append(node)

class ProofTree:
    def __init__(self, root_name, satisfied):
        self.root = ProofNode(root_name, satisfied)

    def to_dict(self):
        def _node_to_dict(node):
            return {
                "name": node.name,
                "satisfied": node.satisfied,
                "details": node.details,
                "children": [_node_to_dict(c) for c in node.children]
            }
        return _node_to_dict(self.root)
