import os
import json
import pandas as pd
import numpy as np
from datetime import datetime

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import roc_auc_score

from .utils import psi


def compute_batch_risk(severe_count, moderate_count):
    if severe_count >= 2:
        return "High Risk"
    elif severe_count == 1 or moderate_count >= 2:
        return "Medium Risk"
    elif moderate_count == 1:
        return "Low Risk"
    else:
        return "Stable"


def agent_decision(feature_severe, pred_psi, auc_baseline, auc_drifted):
    performance_drop = auc_baseline - auc_drifted

    if feature_severe >= 2 and pred_psi > 0.25:
        return "Escalate: Significant feature and prediction drift detected."
    elif performance_drop > 0.05:
        return "Investigate: Performance degradation detected."
    elif pred_psi > 0.25:
        return "Monitor Closely: Prediction distribution shifted."
    else:
        return "Stable: No immediate action required."


def run_monitoring(data_path="../data/raw/UCI_Credit_Card.xlsx"):

    # --- Load Data ---
    df = pd.read_excel(data_path)
    df.columns = df.columns.str.replace('# ', '', regex=False).str.strip()
    df = df.drop(columns=["ID"])

    y = df["default.payment.next.month"]
    X = df.drop(columns=["default.payment.next.month"])

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    pipeline = Pipeline([
        ("scaler", StandardScaler()),
        ("logreg", LogisticRegression(max_iter=2000))
    ])

    pipeline.fit(X_train, y_train)

    # --- Batch Simulation ---
    batch_size = 5000
    batches = [X_test.iloc[i:i+batch_size] for i in range(0, len(X_test), batch_size)]
    y_batches = [y_test.iloc[i:i+batch_size] for i in range(0, len(y_test), batch_size)]

    baseline_batch = batches[0].copy()
    drifted_batch = batches[1].copy()

    # Inject synthetic drift
    drifted_batch["LIMIT_BAL"] *= 1.4
    drifted_batch["PAY_0"] += 1

    # --- Feature Drift ---
    psi_report = {col: psi(baseline_batch[col], drifted_batch[col])
                  for col in baseline_batch.columns}

    psi_df = pd.DataFrame.from_dict(psi_report, orient="index", columns=["PSI"])

    def categorize(v):
        if v < 0.10:
            return "Stable"
        elif v < 0.25:
            return "Moderate Drift"
        else:
            return "Severe Drift"

    psi_df["Drift_Level"] = psi_df["PSI"].apply(categorize)

    severe = int((psi_df["Drift_Level"] == "Severe Drift").sum())
    moderate = int((psi_df["Drift_Level"] == "Moderate Drift").sum())

    top_drift_features = (
        psi_df.reset_index()
              .rename(columns={"index": "feature"})
              .sort_values("PSI", ascending=False)
              .head(5)[["feature", "PSI", "Drift_Level"]]
              .to_dict(orient="records")
    )

    # --- Prediction Drift ---
    baseline_proba = pipeline.predict_proba(baseline_batch)[:, 1]
    drifted_proba = pipeline.predict_proba(drifted_batch)[:, 1]

    prediction_psi = psi(baseline_proba, drifted_proba)

    # --- Performance Drift ---
    auc_base = roc_auc_score(y_batches[0], baseline_proba[:len(y_batches[0])])
    auc_new = roc_auc_score(y_batches[1], drifted_proba[:len(y_batches[1])])

    perf_drop = float(auc_base - auc_new)

    # --- Risk & Decision ---
    batch_level = compute_batch_risk(severe, moderate)
    decision = agent_decision(severe, prediction_psi, auc_base, auc_new)

    # --- Incident Report ---
    incident_report = {
        "incident_type": "Model Monitoring Alert",
        "batch_risk_level": batch_level,
        "decision": decision,
        "summary_metrics": {
            "severe_feature_drift_count": severe,
            "moderate_feature_drift_count": moderate,
            "prediction_psi": float(prediction_psi),
            "auc_baseline": float(auc_base),
            "auc_drifted": float(auc_new),
            "auc_drop": perf_drop,
        },
        "top_drift_features": top_drift_features
    }

    # --- Auto Logging ---
    os.makedirs("../reports/incidents", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = f"../reports/incidents/incident_{timestamp}.json"

    with open(file_path, "w") as f:
        json.dump(incident_report, f, indent=2)

    incident_report["log_file_path"] = file_path

    return incident_report
