import json

STATUTES_DB = {
    "bail": ["CrPC Section 437", "CrPC Section 439"],
    "custody": ["CrPC Section 167"],
    "unlawful detention": ["IPC Section 340"],
    "homicide": ["IPC Section 302", "IPC Section 304"],
    "attempted murder": ["IPC Section 307"],
    "negligence": ["IPC Section 304A"],
    "evidence": ["IEA Section 27", "IEA Section 114"],
    "first offense": ["Probation of Offenders Act Section 4"],
}

class StatuteMapper:
    def map_facts(self, scenario: str) -> list:
        scenario_lower = scenario.lower()
        matched = set()
        for keyword, statutes in STATUTES_DB.items():
            if keyword in scenario_lower:
                matched.update(statutes)
        return list(matched)
