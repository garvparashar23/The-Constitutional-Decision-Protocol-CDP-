from typing import List, Optional

class ProofNode:
    def __init__(self, name: str, satisfied: bool, details: Optional[str] = None):
        self.name = name
        self.satisfied = satisfied
        self.details = details or ""
        self.children: List['ProofNode'] = []

    def add_child(self, node: 'ProofNode'):
        self.children.append(node)

class ProofTree:
    def __init__(self, root_name: str, satisfied: bool):
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
        
    def render_ascii(self) -> str:
        """Renders the proof tree as a visual ASCII graph."""
        lines = []
        
        def _render_node(node: ProofNode, prefix: str, is_last: bool, is_root: bool = False):
            status = "[v]" if node.satisfied else "[x]"
            connector = "└── " if is_last else "├── "
            
            if is_root:
                lines.append(f"{status} {node.name}")
                new_prefix = ""
            else:
                lines.append(f"{prefix}{connector}{status} {node.name}")
                new_prefix = prefix + ("    " if is_last else "│   ")
                
            for i, child in enumerate(node.children):
                _render_node(child, new_prefix, i == len(node.children) - 1, is_root=False)
                
        _render_node(self.root, "", True, is_root=True)
        return "\n".join(lines)
