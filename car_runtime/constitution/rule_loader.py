import os
import yaml
import glob

class RuleLoader:
    def __init__(self, rules_dir="car_runtime/constitutional_rules"):
        self.rules_dir = rules_dir

    def load_all_rules(self):
        rules = []
        yaml_files = glob.glob(os.path.join(self.rules_dir, "*.yaml"))
        for filepath in yaml_files:
            with open(filepath, 'r') as f:
                data = yaml.safe_load(f)
                if data and "principles" in data:
                    for p_obj in data["principles"]:
                        if "principle" in p_obj:
                            rules.append(p_obj["principle"])
        return rules
