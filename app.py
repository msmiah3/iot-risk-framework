# app.py

import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

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
# PAGE CONFIG
# -----------------------------
st.set_page_config(page_title="IoT Safety Framework", layout="wide")

st.title("🔐 IoT Safety & Reliability Analysis Dashboard")
st.markdown("A professional framework for analysing safety and reliability in IoT-enabled smart environments.")

# -----------------------------
# SIDEBAR INPUT
# -----------------------------
st.sidebar.header("⚙️ Configuration")

scenario = st.sidebar.selectbox(
    "Select IoT Scenario",
    ["Smart Home", "Smart City", "Industrial IoT"]
)

cyber_prob = st.sidebar.slider(
    "Cyber Attack Probability",
    0.0, 1.0, 0.2
)

# -----------------------------
# LOAD SCENARIO
# -----------------------------
if scenario == "Smart Home":
    devices = smart_home()
elif scenario == "Smart City":
    devices = smart_city()
else:
    devices = industrial_iot()

# -----------------------------
# DEVICE TABLE
# -----------------------------
st.subheader("📡 Device Configuration")

device_data = pd.DataFrame([{
    "Device": d.name,
    "Failure Rate": d.failure_rate,
    "Impact": d.impact
} for d in devices])

st.dataframe(device_data)

# -----------------------------
# RISK ANALYSIS TABLE
# -----------------------------
st.subheader("⚠️ Risk Analysis")
st.caption("Risk Score = Failure Rate × Impact")

risks = evaluate_devices(devices)

risk_data = pd.DataFrame([{
    "Device": device,
    "Risk Score": round(risk, 3),
    "Risk Level": classify_risk(risk),
    "Mitigation": mitigation_strategy(classify_risk(risk))
} for device, risk in risks.items()])

st.dataframe(risk_data)

# -----------------------------
# CRITICAL DEVICE
# -----------------------------
critical = get_critical_device(risks)
st.error(f"⚠️ Critical Device: {critical}")

# -----------------------------
# ANALYSIS CALCULATIONS
# -----------------------------
device_probs = [d.failure_rate for d in devices]

ft_prob = system_failure(devices)
total_prob = combined_failure_probability(device_probs, cyber_prob)
sim = simulate_scenario(system_failure, devices, cyber_prob)
avail = availability(100, 10)

# -----------------------------
# SYSTEM SUMMARY PANEL
# -----------------------------
st.subheader("📌 System Summary")

st.info(f"""
Scenario: {scenario}  
FTA Failure: {round(ft_prob,3)}  
Combined Risk: {round(total_prob,3)}  
Simulation: {round(sim,3)}  
Availability: {round(avail,3)}
""")

# -----------------------------
# RISK LEVEL INDICATOR
# -----------------------------
if total_prob < 0.3:
    st.success("🟢 Low Risk System")
elif total_prob < 0.6:
    st.warning("🟡 Medium Risk System")
else:
    st.error("🔴 High Risk System")

# -----------------------------
# INSIGHT SECTION
# -----------------------------
st.subheader("🧠 System Insight")

if total_prob > 0.5:
    st.error("System is highly vulnerable and requires immediate intervention.")
elif total_prob > 0.3:
    st.warning("System shows moderate risk. Preventative maintenance is recommended.")
else:
    st.success("System operates within acceptable safety limits.")

# -----------------------------
# KPI METRICS
# -----------------------------
st.subheader("📊 Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("FTA Failure", round(ft_prob, 3))
col2.metric("Combined Risk", round(total_prob, 3))
col3.metric("Availability", round(avail, 3))

# -----------------------------
# INTERACTIVE BAR CHART
# -----------------------------
st.subheader("📈 Device Risk Scores")

fig_bar = px.bar(
    risk_data,
    x="Device",
    y="Risk Score",
    color="Risk Level",
    title="Device Risk Analysis"
)

st.plotly_chart(fig_bar, use_container_width=True)

# -----------------------------
# INTERACTIVE PIE CHART
# -----------------------------
st.subheader("📊 Risk Distribution")

fig_pie = px.pie(
    risk_data,
    names="Device",
    values="Risk Score",
    hole=0.4,
    title="Risk Distribution"
)

st.plotly_chart(fig_pie, use_container_width=True)

# -----------------------------
# CYBER RISK TREND GRAPH
# -----------------------------
st.subheader("📉 Cyber Risk Impact Analysis")

cyber_range = np.linspace(0, 1, 10)
trend = [combined_failure_probability(device_probs, c) for c in cyber_range]

fig_line = px.line(
    x=cyber_range,
    y=trend,
    labels={"x": "Cyber Probability", "y": "Failure Probability"},
    title="Impact of Cyber Risk on System Failure"
)

st.plotly_chart(fig_line, use_container_width=True)

# -----------------------------
# DOWNLOAD REPORT
# -----------------------------
st.subheader("📥 Export Results")

csv = risk_data.to_csv(index=False)

st.download_button(
    label="Download Risk Report",
    data=csv,
    file_name="iot_risk_report.csv",
    mime="text/csv",
)