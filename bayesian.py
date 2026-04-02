# bayesian.py

def bayesian_update(prior, likelihood, evidence):
    if evidence == 0:
        return 0
    return (likelihood * prior) / evidence


def combined_failure_probability(device_probs, cyber_prob):
    """
    Combines device failure with cyber attack probability
    """
    system_prob = 1
    for p in device_probs:
        system_prob *= (1 - p)

    device_failure = 1 - system_prob

    # Combine with cyber attack (OR logic)
    total_failure = 1 - ((1 - device_failure) * (1 - cyber_prob))
    return total_failure