import streamlit as st

st.set_page_config(
    page_title="Agentic Model Risk Auditor",
    page_icon="🛡️",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #fff7ed 0%, #fdf2f8 35%, #eef2ff 70%, #ecfeff 100%);
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

.hero {
    padding: 64px;
    border-radius: 34px;
    background: linear-gradient(135deg, #ff7a7a 0%, #a855f7 45%, #2563eb 100%);
    color: white;
    box-shadow: 0 28px 70px rgba(168, 85, 247, 0.28);
}

.hero h1 {
    font-size: 62px;
    font-weight: 900;
    color: white;
}

.hero p {
    font-size: 18px;
    color: #fff7ed;
    max-width: 980px;
}

.section-title {
    font-size: 32px;
    font-weight: 850;
    color: #111827;
    margin-top: 34px;
    margin-bottom: 18px;
}

.glass {
    padding: 30px;
    border-radius: 26px;
    background: rgba(255,255,255,0.92);
    border: 1px solid rgba(226,232,240,0.9);
    box-shadow: 0 16px 40px rgba(148,163,184,0.18);
    min-height: 205px;
}

.glass h3 {
    color: #111827;
}

.glass p {
    color: #475569;
    font-size: 15px;
}

.accent {
    color: #7c3aed;
    font-weight: 800;
}

.flow {
    text-align: center;
    padding: 26px;
    border-radius: 22px;
    background: linear-gradient(135deg, #ffffff, #f8fafc);
    border: 1px solid #e2e8f0;
    box-shadow: 0 12px 28px rgba(148,163,184,0.15);
    color: #111827;
}

.flow:hover {
    transform: translateY(-3px);
    transition: 0.25s ease;
    box-shadow: 0 18px 38px rgba(168,85,247,0.20);
}

.flow b {
    font-size: 16px;
    color: #1e293b;
}

.footer-card {
    padding: 36px;
    border-radius: 30px;
    background: linear-gradient(135deg, #ecfeff, #f5f3ff, #fdf2f8);
    border: 1px solid #ddd6fe;
    color: #334155;
    box-shadow: 0 16px 40px rgba(148,163,184,0.18);
}

.footer-card h2 {
    color: #111827;
}

.color-strip {
    height: 8px;
    border-radius: 999px;
    background: linear-gradient(90deg, #f97316, #ec4899, #8b5cf6, #06b6d4);
    margin: 22px 0;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <h1>🛡️ Agentic Model Risk Auditor</h1>
    <p><b>AI Governance Command Center for Monitoring Credit-Risk Models</b></p>
    <p>
    A production-style oversight platform that detects model instability, evaluates risk severity,
    generates audit-ready incident reports, and keeps high-risk interventions under human approval.
    </p>
</div>
<div class="color-strip"></div>
""", unsafe_allow_html=True)

st.markdown('<div class="section-title">⚡ Platform Intelligence Layer</div>', unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="glass">
        <h3>📡 Continuous Monitoring</h3>
        <p>Simulates post-deployment monitoring for credit-risk models and tracks changing data behavior over time.</p>
        <p><span class="accent">Focus:</span> production model reliability</p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="glass">
        <h3>🧠 Autonomous Risk Reasoning</h3>
        <p>Evaluates drift signals and converts raw monitoring outputs into clear escalation decisions.</p>
        <p><span class="accent">Focus:</span> agentic decision workflow</p>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="glass">
        <h3>🔐 Human-Gated Governance</h3>
        <p>Prevents blind automated intervention by requiring human approval before high-risk actions.</p>
        <p><span class="accent">Focus:</span> responsible AI control</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="section-title">🧭 Agentic System Flow</div>', unsafe_allow_html=True)

f1, f2, f3, f4, f5 = st.columns(5)

steps = [
    ("1️⃣", "Observe", "Production batch"),
    ("2️⃣", "Detect", "Drift signals"),
    ("3️⃣", "Evaluate", "Risk severity"),
    ("4️⃣", "Decide", "Escalate or monitor"),
    ("5️⃣", "Govern", "Human approval")
]

for col, (num, title, desc) in zip([f1, f2, f3, f4, f5], steps):
    with col:
        st.markdown(
            f'<div class="flow">{num}<br><b>{title}</b><br><small>{desc}</small></div>',
            unsafe_allow_html=True
        )

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<div class="footer-card">
    <h2>🚀 Start Exploring</h2>
    <p>
    Use the sidebar to move through the dashboard, drift analysis, incident reports,
    agent decision logic, and human approval workflow.
    </p>
</div>
""", unsafe_allow_html=True)