import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dashboard", page_icon="🏠", layout="wide")

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
    padding: 26px;
    border-radius: 24px;
    background: rgba(255,255,255,0.96);
    box-shadow: 0 16px 40px rgba(148,163,184,0.18);
    border: 1px solid #e5e7eb;
    min-height: 155px;
}

.risk-card {
    padding: 26px;
    border-radius: 24px;
    background: linear-gradient(135deg, #ffe4e6, #ffffff);
    border: 1px solid #fecdd3;
    box-shadow: 0 16px 40px rgba(244,63,94,0.18);
    min-height: 155px;
}

.metric-label {
    color:#64748b;
    font-size:14px;
    font-weight:700;
}

.metric-red {
    color:#dc2626;
    font-size:32px;
    font-weight:900;
}

.metric-blue {
    color:#2563eb;
    font-size:32px;
    font-weight:900;
}

.metric-dark {
    color:#111827;
    font-size:32px;
    font-weight:900;
}

.badge-red {
    background:#fee2e2;
    color:#b91c1c;
    padding:8px 14px;
    border-radius:999px;
    font-weight:800;
    font-size:13px;
}

.badge-yellow {
    background:#fef3c7;
    color:#92400e;
    padding:8px 14px;
    border-radius:999px;
    font-weight:800;
    font-size:13px;
}

.badge-purple {
    background:#ede9fe;
    color:#6d28d9;
    padding:8px 14px;
    border-radius:999px;
    font-weight:800;
    font-size:13px;
}

.info-box {
    padding: 30px;
    border-radius: 26px;
    background: rgba(255,255,255,0.96);
    border: 1px solid #e5e7eb;
    box-shadow: 0 14px 35px rgba(148,163,184,0.15);
    min-height: 245px;
}

.next-box {
    padding: 26px;
    border-radius: 24px;
    background: linear-gradient(135deg, #fff7ed, #fef3c7);
    border: 1px solid #fde68a;
    box-shadow: 0 14px 35px rgba(245,158,11,0.14);
}

.small-note {
    color:#64748b;
    font-size:14px;
}
</style>
""", unsafe_allow_html=True)

st.title("🏠 Executive Dashboard")
st.caption("High-level monitoring summary for the Agentic Model Risk Auditor")

st.success("Monitoring run completed successfully. Incident risk assessment generated.")

c1, c2, c3, c4, c5 = st.columns(5)

with c1:
    st.markdown("""
    <div class="risk-card">
        <div class="metric-label">Current Risk Level</div>
        <div class="metric-red">HIGH</div><br>
        <span class="badge-red">Escalation Required</span>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="card">
        <div class="metric-label">Prediction PSI</div>
        <div class="metric-red">0.5454</div><br>
        <span class="badge-red">Severe Drift</span>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="card">
        <div class="metric-label">AUC Drop</div>
        <div class="metric-blue">0.0156</div><br>
        <span class="badge-yellow">Performance Shift</span>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown("""
    <div class="card">
        <div class="metric-label">Severe Features</div>
        <div class="metric-red">2</div><br>
        <span class="badge-red">PAY_0 + LIMIT_BAL</span>
    </div>
    """, unsafe_allow_html=True)

with c5:
    st.markdown("""
    <div class="card">
        <div class="metric-label">Approval Status</div>
        <div class="metric-dark">Pending</div><br>
        <span class="badge-purple">Human Review</span>
    </div>
    """, unsafe_allow_html=True)

st.markdown("## Latest Incident Summary")

left, right = st.columns([1.15, 1])

with left:
    st.markdown("""
    <div class="info-box">
        <h3>🚨 Model Monitoring Alert</h3>
        <p><b>Risk Level:</b> <span style="color:#dc2626;font-weight:900;">High Risk</span></p>
        <p><b>Decision:</b> Escalate: Significant feature and prediction drift detected.</p>
        <p><b>Business Meaning:</b> The credit-risk model is receiving data that looks materially different from the baseline population. Human review is required before automated intervention.</p>
    </div>
    """, unsafe_allow_html=True)

with right:
    st.markdown("### Top Drift Drivers")

    drift_preview = pd.DataFrame({
        "Feature": ["PAY_0", "LIMIT_BAL"],
        "PSI": [1.9833, 0.4346],
        "Status": ["Severe Drift", "Severe Drift"]
    })

    st.dataframe(drift_preview, use_container_width=True, hide_index=True)

    st.markdown("""
    <div class="next-box">
        <h4>⚠️ Next Action Required</h4>
        <p>Human approval is required before freezing decisions, retraining, or changing thresholds.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.caption("Use the sidebar to explore Drift Analysis, Incident Reports, Agent Decision, and Human Approval.")