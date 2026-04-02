# risk_analysis.py

def evaluate_devices(devices):
    """
    Calculate risk score for each device.
    Risk = Failure Rate × Impact
    """
    risks = {}
    for device in devices:
        risk = device.failure_rate * device.impact
        risks[device.name] = risk
    return risks


def classify_risk(risk):
    """
    Classify risk levels.
    """
    if risk < 0.2:
        return "LOW"
    elif risk < 0.5:
        return "MEDIUM"
    else:
        return "HIGH"


def mitigation_strategy(level):
    """
    Suggest mitigation strategies.
    """
    if level == "HIGH":
        return "Immediate maintenance and security patching required"
    elif level == "MEDIUM":
        return "Monitor device and schedule maintenance"
    else:
        return "System operating normally"


def get_critical_device(risks):
    """
    Identify highest risk device.
    """
    return max(risks, key=risks.get)