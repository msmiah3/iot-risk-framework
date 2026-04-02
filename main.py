# main.py
print("🚀 NEW VERSION RUNNING")
import matplotlib.pyplot as plt
from scenarios import smart_home, smart_city, industrial_iot
from risk_analysis import (
    evaluate_devices,
    classify_risk,
    mitigation_strategy,
    get_critical_device
)
from fault_tree import system_failure
from bayesian import combined_failure_probability
from simulation import simulate_scenario
from metrics import availability


# -----------------------------
# UTILITY FUNCTIONS
# -----------------------------

def print_header(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


def print_section(title):
    print("\n" + "-" * 50)
    print(title)
    print("-" * 50)


def system_risk_level(prob):
    if prob < 0.3:
        return "LOW"
    elif prob < 0.6:
        return "MEDIUM"
    else:
        return "HIGH"


# -----------------------------
# GRAPH FUNCTIONS
# -----------------------------

def plot_risk_scores(devices, title):
    names = [d.name for d in devices]
    risks = evaluate_devices(devices)

    plt.figure(figsize=(8, 5))
    plt.bar(names, risks.values())
    plt.title(f"{title} - Device Risk Scores")
    plt.xlabel("Devices")
    plt.ylabel("Risk Score")
    plt.tight_layout()
    plt.show()


def plot_failure_comparison(home, city, industrial):
    labels = ["Smart Home", "Smart City", "Industrial IoT"]
    values = [home, city, industrial]

    plt.figure()
    plt.pie(values, labels=labels, autopct='%1.1f%%')
    plt.title("Failure Probability Comparison")
    plt.show()


# -----------------------------
# MAIN ANALYSIS
# -----------------------------

def run_analysis(name, devices, cyber_prob, mtbf=100, mttr=10):
    print_header(f"{name} IoT Environment Analysis")

    # 1. Devices
    print_section("Device Configuration")
    for d in devices:
        print(f"{d.name} | Failure Rate: {d.failure_rate} | Impact: {d.impact}")

    # 2. Risk Analysis
    print_section("Risk Analysis + Classification")
    risks = evaluate_devices(devices)

    for device, risk in risks.items():
        level = classify_risk(risk)
        action = mitigation_strategy(level)

        print(f"{device}:")
        print(f"   Risk Score = {round(risk,3)}")
        print(f"   Risk Level = {level}")
        print(f"   Mitigation = {action}")

    # Critical Device
    critical = get_critical_device(risks)
    print(f"\n⚠️ Critical Device: {critical} (Highest Risk)")

    # 3. Fault Tree
    print_section("Fault Tree Analysis (FTA)")
    ft_prob = system_failure(devices)
    print(f"System Failure Probability: {round(ft_prob,3)}")

    # 4. Bayesian
    print_section("Bayesian + Cyber Risk")
    device_probs = [d.failure_rate for d in devices]
    total_prob = combined_failure_probability(device_probs, cyber_prob)

    print(f"Cyber Probability: {cyber_prob}")
    print(f"Combined Failure Probability: {round(total_prob,3)}")

    # System Risk Level
    level = system_risk_level(total_prob)
    print(f"Overall System Risk Level: {level}")

    # 5. What-if Analysis
    print_section("What-If Cyber Attack Analysis")
    low = combined_failure_probability(device_probs, 0.1)
    high = combined_failure_probability(device_probs, 0.5)

    print(f"Low Cyber Risk (0.1): {round(low,3)}")
    print(f"High Cyber Risk (0.5): {round(high,3)}")

    # 6. Simulation
    print_section("Simulation (Monte Carlo)")
    sim = simulate_scenario(system_failure, devices, cyber_prob)
    print(f"Simulated Failure Probability: {round(sim,3)}")

    # 7. Reliability
    print_section("Reliability Metrics")
    avail = availability(mtbf, mttr)

    print(f"MTBF: {mtbf}")
    print(f"MTTR: {mttr}")
    print(f"Availability: {round(avail,3)}")

    # Insight
    print_section("System Insight")
    if total_prob > 0.5:
        print("System is highly vulnerable and requires immediate intervention.")
    else:
        print("System operates within acceptable risk levels.")

    # Graph
    plot_risk_scores(devices, name)

    return ft_prob, avail


# -----------------------------
# EXECUTION
# -----------------------------

if __name__ == "__main__":

    print("\nStarting IoT Safety & Reliability Framework...\n")

    home_prob, home_avail = run_analysis("Smart Home", smart_home(), 0.2)
    city_prob, city_avail = run_analysis("Smart City", smart_city(), 0.25)
    ind_prob, ind_avail = run_analysis("Industrial IoT", industrial_iot(), 0.3)

    # Comparison Table
    print("\n" + "=" * 60)
    print("SCENARIO COMPARISON")
    print("=" * 60)
    print("Scenario        Failure    Availability")
    print("----------------------------------------")
    print(f"Smart Home      {round(home_prob,3)}      {round(home_avail,3)}")
    print(f"Smart City      {round(city_prob,3)}      {round(city_avail,3)}")
    print(f"Industrial IoT  {round(ind_prob,3)}      {round(ind_avail,3)}")

    plot_failure_comparison(home_prob, city_prob, ind_prob)

    print("\nAnalysis Complete.\n")