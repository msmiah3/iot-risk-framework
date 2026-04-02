# devices.py

class Device:
    def __init__(self, name, failure_rate, impact, dependencies=None):
        self.name = name
        self.failure_rate = failure_rate
        self.impact = impact
        self.dependencies = dependencies if dependencies else []

    def __repr__(self):
        return f"{self.name} (Failure Rate: {self.failure_rate})"