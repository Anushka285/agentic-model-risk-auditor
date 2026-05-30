import streamlit as st

st.set_page_config(
    page_title="Human Approval",
    page_icon="👤",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #fff7ed 0%, #fdf2f8 35%, #eef2ff 70%, #ecfeff 100%);
    color: #111827;
}

.status-card {
    padding: 28px;
    border-radius: 24px;
    background: linear-gradient(135deg, #fff7ed, #fef3c7);
    border: 1px solid #fcd34d;
    box-shadow: 0 10px 25px rgba(245,158,11,0.12);
}

.action-card {
    padding: 28px;
    border-radius: 22px;
    background: white;
    border: 1px solid #e5e7eb;
    border-top: 4px solid #8b5cf6;
    box-shadow: 0 10px 25px rgba(148,163,184,0.14);
    min-height: 170px;
    text-align: center;
}

.action-card h3 {
    font-size: 22px;
    margin-bottom: 10px;
}

.action-card p {
    color: #64748b;
    font-size: 15px;
}

.action-link {
    color: #7c3aed;
    font-weight: 900;
    margin-top: 14px;
}

.info-card {
    padding: 30px;
    border-radius: 24px;
    background: white;
    border: 1px solid #e5e7eb;
    box-shadow: 0 10px 25px rgba(148,163,184,0.14);
}
</style>
""", unsafe_allow_html=True)

st.title("👤 Human-in-the-Loop Governance")

st.markdown("""
<div class="status-card">
    <h3>⚠️ Pending Human Approval</h3>
    <p>The agent has escalated this incident. Production intervention should not proceed until a reviewer approves the next step.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("## Governance Actions")

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="action-card">
        <h3>✅ Approve Investigation</h3>
        <p>Allow deeper diagnostics and validation.</p>
        <div class="action-link">Review action →</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="action-card">
        <h3>🚨 Escalate to Risk Team</h3>
        <p>Route incident to governance stakeholders.</p>
        <div class="action-link">Review action →</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="action-card">
        <h3>📌 Mark as Reviewed</h3>
        <p>Close the governance review loop.</p>
        <div class="action-link">Review action →</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("## 🛡 Why Human Approval Matters")

left, right = st.columns(2)

with left:
    st.markdown("""
    <div class="info-card">
        <h3>🤖 Agent</h3>
        <p>✔ Detect Drift</p>
        <p>✔ Evaluate Risk</p>
        <p>✔ Recommend Actions</p>
        <p>✔ Escalate Cases</p>
    </div>
    """, unsafe_allow_html=True)

with right:
    st.markdown("""
    <div class="info-card">
        <h3>👤 Human</h3>
        <p>✔ Review Findings</p>
        <p>✔ Approve / Reject</p>
        <p>✔ Escalate Further</p>
        <p>✔ Authorize Intervention</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div class="info-card" style="margin-top:20px;">
    <center>
    <h4>Governance Principle</h4>
    <p>
    Human approval prevents unsafe automated intervention
    in high-risk production credit-risk models.
    </p>
    </center>
</div>
""", unsafe_allow_html=True)