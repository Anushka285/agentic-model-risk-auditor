import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Drift Analysis", page_icon="📊", layout="wide")

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
}

.metric-card {
    padding: 24px;
    border-radius: 22px;
    background: rgba(255,255,255,0.96);
    box-shadow: 0 14px 35px rgba(148,163,184,0.16);
    border: 1px solid #e5e7eb;
    min-height: 135px;
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

.badge-green {
    background:#dcfce7;
    color:#166534;
    padding:8px 14px;
    border-radius:999px;
    font-weight:800;
    font-size:13px;
}

.insight-box {
    padding: 26px;
    border-radius: 24px;
    background: linear-gradient(135deg, #fff7ed, #fef3c7);
    border: 1px solid #fde68a;
    box-shadow: 0 14px 35px rgba(245,158,11,0.14);
}
</style>
""", unsafe_allow_html=True)

st.title("📊 Drift Analysis")
st.caption("Feature-level stability check using Population Stability Index")

drift_df = pd.DataFrame({
    "Feature": ["PAY_0", "LIMIT_BAL", "BILL_AMT6", "PAY_AMT5", "BILL_AMT5"],
    "PSI": [1.9833, 0.4346, 0.0145, 0.0127, 0.0101],
    "Drift Level": ["Severe Drift", "Severe Drift", "Stable", "Stable", "Stable"]
})

severe_count = int((drift_df["Drift Level"] == "Severe Drift").sum())
stable_count = int((drift_df["Drift Level"] == "Stable").sum())
max_psi = drift_df["PSI"].max()

m1, m2, m3 = st.columns(3)

with m1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Severe Drift Features</div>
        <div class="metric-red">{severe_count}</div><br>
        <span class="badge-red">Requires Investigation</span>
    </div>
    """, unsafe_allow_html=True)

with m2:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Highest PSI</div>
        <div class="metric-red">{max_psi:.4f}</div><br>
        <span class="badge-red">PAY_0</span>
    </div>
    """, unsafe_allow_html=True)

with m3:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Stable Features</div>
        <div class="metric-dark">{stable_count}</div><br>
        <span class="badge-green">Low Shift</span>
    </div>
    """, unsafe_allow_html=True)

st.markdown("## Drift Drivers")

left, right = st.columns([1.1, 1])

with left:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.dataframe(drift_df, use_container_width=True, hide_index=True)
    st.markdown('</div>', unsafe_allow_html=True)

with right:
    st.markdown("""
    <div class="insight-box">
        <h3>⚠️ Key Finding</h3>
        <p><b>PAY_0</b> and <b>LIMIT_BAL</b> show severe population shift.</p>
        <p>This indicates that the incoming batch is materially different from the baseline population and should be investigated before automated intervention.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("## PSI Severity Chart")

fig = px.bar(
    drift_df,
    x="Feature",
    y="PSI",
    color="Drift Level",
    text="PSI",
    color_discrete_map={
        "Severe Drift": "#dc2626",
        "Stable": "#22c55e"
    }
)

fig.update_traces(texttemplate="%{text:.4f}", textposition="outside")
fig.update_layout(
    height=480,
    showlegend=True,
    plot_bgcolor="rgba(255,255,255,0)",
    paper_bgcolor="rgba(255,255,255,0)",
    margin=dict(l=20, r=20, t=40, b=20)
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("## PSI Threshold Reference")

st.markdown("""
| PSI Range | Interpretation |
|---|---|
| < 0.10 | Stable |
| 0.10 – 0.25 | Moderate Drift |
| > 0.25 | Severe Drift |
""")