class ConstitutionalAgent:
    def __init__(self, name, priority, utility_function, principles, reasoning_style):
        self.name = name
        self.priority = priority
        self.utility_function = utility_function
        self.principles = principles
        self.reasoning_style = reasoning_style
        
    def evaluate(self, proposal, context):
        """Generates objections, scores compliance, and proposes modifications."""
        raise NotImplementedError
        
    def generate_counterargument(self, proposal, objections, context):
        """Generates counterarguments based on other agents' criticisms."""
        return "No counterargument provided."
