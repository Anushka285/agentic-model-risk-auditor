import streamlit as st

st.set_page_config(page_title="Agent Decision", page_icon="🤖", layout="wide")

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #fff7ed 0%, #fdf2f8 35%, #eef2ff 75%, #ecfeff 100%);
    color: #111827;
}
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #ffffff, #f8fafc);
    border-right: 1px solid #e5e7eb;
}
[data-testid="stSidebar"] * {
    color: #334155 !important;
    font-weight: 600;
}
.card {
    padding: 28px;
    border-radius: 26px;
    background: rgba(255,255,255,0.96);
    border: 1px solid #e5e7eb;
    box-shadow: 0 14px 35px rgba(148,163,184,0.16);
}
.alert-card {
    padding: 30px;
    border-radius: 28px;
    background: linear-gradient(135deg, #ffe4e6, #ffffff);
    border: 1px solid #fecdd3;
    box-shadow: 0 14px 35px rgba(244,63,94,0.16);
}
.step-card {
    padding: 22px;
    border-radius: 22px;
    background: white;
    border: 1px solid #e5e7eb;
    box-shadow: 0 10px 25px rgba(148,163,184,0.12);
    min-height: 145px;
}
.action-box {
    padding: 18px;
    border-radius: 18px;
    background: white;
    border: 1px solid #e5e7eb;
    box-shadow: 0 10px 25px rgba(148,163,184,0.12);
    margin-bottom: 12px;
}
.badge-red {
    background:#fee2e2;
    color:#b91c1c;
    padding:8px 14px;
    border-radius:999px;
    font-weight:800;
}
.badge-purple {
    background:#ede9fe;
    color:#6d28d9;
    padding:8px 14px;
    border-radius:999px;
    font-weight:800;
}
.badge-yellow {
    background:#fef3c7;
    color:#92400e;
    padding:8px 14px;
    border-radius:999px;
    font-weight:800;
}
</style>
""", unsafe_allow_html=True)

st.title("🤖 Agent Decision")
st.caption("Autonomous risk reasoning and escalation logic")

st.markdown("""
<div class="alert-card">
    <h3>🚨 Decision: Escalate</h3>
    <p>Significant feature and prediction drift were detected in the monitored batch.</p>
    <span class="badge-red">High Risk</span>
    <span class="badge-yellow">Human Review Required</span>
</div>
""", unsafe_allow_html=True)

st.markdown("## Why the Agent Escalated")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown("""
    <div class="step-card">
        <h3>1️⃣ Feature Drift</h3>
        <p>Two features showed severe drift:</p>
        <b>PAY_0</b><br>
        <b>LIMIT_BAL</b>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="step-card">
        <h3>2️⃣ Prediction Shift</h3>
        <p>Prediction PSI crossed the severe threshold.</p>
        <span class="badge-red">PSI = 0.5454</span>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="step-card">
        <h3>3️⃣ Performance Change</h3>
        <p>Model ranking performance shifted.</p>
        <b>AUC:</b> 0.7100 → 0.6944
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown("""
    <div class="step-card">
        <h3>4️⃣ Business Risk</h3>
        <p>The model supports financial risk decisions, so automated action must be controlled.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("## Recommended Agent Actions")

a1, a2 = st.columns(2)

with a1:
    st.markdown("""
    <div class="action-box">✅ Notify model owner + risk team</div>
    <div class="action-box">✅ Run deeper diagnostics</div>
    <div class="action-box">✅ Collect additional validation data</div>
    """, unsafe_allow_html=True)

with a2:
    st.markdown("""
    <div class="action-box">⚠️ Freeze automated decisions if high-stakes</div>
    <div class="action-box">🧪 Prepare retraining plan, but do not retrain automatically</div>
    <div class="action-box">👤 Route final decision to human approval</div>
    """, unsafe_allow_html=True)

st.markdown("## Agentic Decision Loop")

st.markdown("""
<div class="card">
    <h3>Observe → Detect → Evaluate → Decide → Recommend → Escalate</h3>
    <p>
    This system is agentic because it does not only display metrics. It interprets monitoring signals,
    assigns risk severity, recommends action, and escalates high-risk cases while keeping final intervention under human approval.
    </p>
</div>
""", unsafe_allow_html=True)