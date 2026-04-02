# fault_tree.py

def system_failure(devices):
    """
    Simple OR-gate fault tree:
    System fails if any critical device fails
    """
    failure_probability = 1
    for device in devices:
        failure_probability *= (1 - device.failure_rate)
    return 1 - failure_probability