# simulation.py

import random

def simulate_scenario(failure_function, devices, cyber_prob, iterations=1000):
    """
    Monte Carlo simulation to validate failure probability.
    """
    failures = 0

    for _ in range(iterations):
        base_prob = failure_function(devices)
        combined_prob = base_prob + cyber_prob

        if random.random() < combined_prob:
            failures += 1

    return failures / iterations