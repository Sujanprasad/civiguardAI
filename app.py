
import streamlit as st
import os
import json
from dotenv import load_dotenv
from groq import Groq

# Load API key
load_dotenv()

print("API KEY:", os.getenv("GROQ_API_KEY"))

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

st.set_page_config(page_title="CIVIGUARD AI", layout="wide")

st.title("🚨 CIVIGUARD AI")
st.subheader("Prompt-Engineered Crisis Intelligence System")

# 👇 NEW ARCHITECTURE SECTION
st.markdown("### 🧠 Multi-Agent Civic Intelligence Architecture")

st.write("""
CIVIGUARD AI helps users during emergency situations by:
- Analyzing crisis severity
- Simulating critical decisions
- Detecting misinformation & panic content
""")

st.info("This system uses structured prompt engineering with role-based reasoning, JSON enforcement, and risk aggregation modeling.")

st.divider()

# -------------------- CIVIC THREAT CALCULATION --------------------

def calculate_civic_threat(urgency, escalation, credibility):
    threat_score = (urgency * 10 + escalation + (100 - credibility)) / 3
    return int(threat_score)

# -------------------- CRISIS FUNCTION --------------------

def analyze_crisis(user_input):

    prompt = f"""
You are a certified disaster risk analyst.

Analyze the situation below.

Return response ONLY in valid JSON format.

Required JSON structure:

{{
  "hazard_type": "",
  "severity_level": "",
  "escalation_probability_percent": "",
  "urgency_score_1_to_10": "",
  "immediate_actions": [],
  "common_mistakes_to_avoid": []
}}

Situation:
{user_input}
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {"role": "system", "content": "You are a structured emergency risk analyst."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    return response.choices[0].message.content

# -------------------- DECISION FUNCTION --------------------

def simulate_decision(user_input):

    prompt = f"""
You are a strategic risk decision analyst.

Analyze the decision scenario below.

Return response ONLY in valid JSON format.

Required JSON structure:

{{
  "option_A": {{
      "description": "",
      "risk_level_1_to_10": "",
      "short_term_consequence": "",
      "worst_case_scenario": ""
  }},
  "option_B": {{
      "description": "",
      "risk_level_1_to_10": "",
      "short_term_consequence": "",
      "worst_case_scenario": ""
  }},
  "recommended_option": "",
  "reasoning": ""
}}

Scenario:
{user_input}
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {"role": "system", "content": "You are a structured decision risk analyst."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    return response.choices[0].message.content

# -------------------- RUMOR FUNCTION --------------------

def analyze_rumor(user_input):

    prompt = f"""
You are a misinformation detection analyst trained in logical reasoning and psychological bias detection.

Analyze the message below.

Return response ONLY in valid JSON format.

Required JSON structure:

{{
  "emotional_triggers_detected": [],
  "logical_fallacies_detected": [],
  "source_credibility_assessment": "",
  "credibility_score_0_to_100": "",
  "recommended_safe_action": ""
}}

Message:
{user_input}
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {"role": "system", "content": "You are a structured misinformation detection expert."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )

    return response.choices[0].message.content

# -------------------- TABS --------------------

tab1, tab2, tab3 = st.tabs(["🚨 Crisis Mode", "🧠 Decision Mode", "🔍 Rumor Check"])

# -------------------- TAB 1 --------------------

with tab1:
    st.header("Crisis Analysis")

    crisis_input = st.text_area(
        "Describe the emergency situation:",
        placeholder="Example: Water entering ground floor, power cut, elderly parents at home..."
    )

    if st.button("Analyze Crisis"):
        if crisis_input.strip() == "":
            st.warning("Please describe the situation.")
        else:
            with st.spinner("Analyzing crisis..."):
                result = analyze_crisis(crisis_input)

                try:
                    parsed = json.loads(result)

                    st.success("Analysis Complete")

                    st.write("### 🔍 Hazard Type")
                    st.write(parsed["hazard_type"])

                    st.write("### ⚠ Severity Level")
                    severity = parsed["severity_level"]

                    if severity.lower() == "high":
                        st.error(severity)
                    elif severity.lower() == "medium":
                        st.warning(severity)
                    else:
                        st.success(severity)

                    escalation = int(parsed["escalation_probability_percent"])
                    st.write("### 📈 Escalation Probability")
                    st.write(f"{escalation}%")

                    urgency = int(parsed["urgency_score_1_to_10"])
                    st.write("### 🚨 Urgency Score (1-10)")
                    st.progress(urgency * 10)
                    st.write(f"Score: {urgency}/10")

                    credibility = 50

                    threat_index = calculate_civic_threat(urgency, escalation, credibility)

                    st.write("## 🚨 Civic Threat Index")

                    if threat_index >= 75:
                        st.error(f"🔴 HIGH THREAT: {threat_index}/100")
                    elif threat_index >= 40:
                        st.warning(f"🟠 MODERATE THREAT: {threat_index}/100")
                    else:
                        st.success(f"🟢 LOW THREAT: {threat_index}/100")

                    st.progress(threat_index)
                    
                    

                    st.write("### ✅ Immediate Actions")
                    for action in parsed["immediate_actions"]:
                        st.write("- " + action)

                    st.write("### ❌ Common Mistakes to Avoid")
                    for mistake in parsed["common_mistakes_to_avoid"]:
                        st.write("- " + mistake)

                except:
                    st.error("AI returned invalid format. Try again.")

# -------------------- TAB 2 --------------------

with tab2:
    st.header("Decision Simulator")

    decision_input = st.text_area(
        "Describe your decision dilemma:",
        placeholder="Example: Should I evacuate now or wait until morning?"
    )

    if st.button("Simulate Decision"):
        if decision_input.strip() == "":
            st.warning("Please describe your scenario.")
        else:
            with st.spinner("Simulating decision outcomes..."):
                result = simulate_decision(decision_input)

                try:
                    parsed = json.loads(result)

                    st.success("Simulation Complete")

                    st.write("## 🔵 Option A")
                    st.write("Description:", parsed["option_A"]["description"])
                    st.write("Risk Level:", parsed["option_A"]["risk_level_1_to_10"])
                    st.write("Short-Term Consequence:", parsed["option_A"]["short_term_consequence"])
                    st.write("Worst Case:", parsed["option_A"]["worst_case_scenario"])

                    st.write("## 🟢 Option B")
                    st.write("Description:", parsed["option_B"]["description"])
                    st.write("Risk Level:", parsed["option_B"]["risk_level_1_to_10"])
                    st.write("Short-Term Consequence:", parsed["option_B"]["short_term_consequence"])
                    st.write("Worst Case:", parsed["option_B"]["worst_case_scenario"])

                    st.write("## ⭐ Recommended Option")
                    st.write(parsed["recommended_option"])

                    st.write("### 🧠 Reasoning")
                    st.write(parsed["reasoning"])

                except:
                    st.error("AI returned invalid format. Try again.")

# -------------------- TAB 3 --------------------

with tab3:
    st.header("Rumor & Misinformation Detector")

    rumor_input = st.text_area(
        "Paste the message or rumor here:",
        placeholder="Example: Dam gates broken! Run immediately or you will die!"
    )

    if st.button("Check Credibility"):
        if rumor_input.strip() == "":
            st.warning("Please paste a message.")
        else:
            with st.spinner("Analyzing message credibility..."):
                result = analyze_rumor(rumor_input)

                try:
                    parsed = json.loads(result)

                    st.success("Analysis Complete")

                    st.write("### 🔥 Emotional Triggers Detected")
                    for trigger in parsed["emotional_triggers_detected"]:
                        st.write("- " + trigger)

                    st.write("### ⚠ Logical Fallacies Detected")
                    for fallacy in parsed["logical_fallacies_detected"]:
                        st.write("- " + fallacy)

                    st.write("### 🏛 Source Credibility Assessment")
                    st.write(parsed["source_credibility_assessment"])

                    cred_score = int(parsed["credibility_score_0_to_100"])

                    st.write("### 📊 Credibility Score (0-100)")
                    st.progress(cred_score)
                    st.write(f"Score: {cred_score}/100")

                    st.write("### ✅ Recommended Safe Action")
                    st.write(parsed["recommended_safe_action"])

                except:
                    st.error("AI returned invalid format. Try again.")