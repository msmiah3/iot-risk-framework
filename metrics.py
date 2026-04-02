# metrics.py

def availability(mtbf, mttr):
    return mtbf / (mtbf + mttr)


def reliability_over_time(failure_rate, time):
    """
    Exponential reliability function
    """
    import math
    return math.exp(-failure_rate * time)