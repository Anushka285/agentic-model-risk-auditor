# 🛡️ Agentic Model Risk Auditor

> An autonomous AI governance system that monitors deployed machine learning models, detects drift, evaluates operational risk, generates incident reports, and escalates high-risk situations through a Human-in-the-Loop approval workflow.

---

## 🚀 Project Overview

Machine learning models do not fail overnight.

They gradually become unreliable as customer behavior, economic conditions, and input data distributions change over time.

In industries such as banking, lending, insurance, and fraud detection, undetected model drift can lead to:

- Financial losses
- Poor business decisions
- Regulatory violations
- Increased operational risk
- Reduced model trustworthiness

To address this challenge, I built an **Agentic Model Risk Auditor** — an autonomous monitoring system that continuously evaluates deployed machine learning models and determines when human intervention is required.

Unlike traditional dashboards that only display metrics, this system actively:

✅ Observes model behavior

✅ Detects feature and prediction drift

✅ Assesses risk severity

✅ Generates incident reports

✅ Recommends actions

✅ Escalates critical cases for human review

---

## 🎯 Business Problem

Organizations often invest significant resources into training machine learning models but spend far less effort monitoring them after deployment.

As production data evolves, models can become less reliable without any visible warning signs.

The goal of this project is to create an intelligent oversight layer capable of identifying model degradation before it causes business impact.

---

## 🏗️ System Architecture

```text
Production Data Batch
          │
          ▼
 ┌─────────────────┐
 │ Monitoring Layer │
 └─────────────────┘
          │
          ▼
 ┌─────────────────┐
 │ Drift Detection │
 │   PSI Analysis  │
 └─────────────────┘
          │
          ▼
 ┌─────────────────┐
 │ Risk Scoring    │
 └─────────────────┘
          │
          ▼
 ┌─────────────────┐
 │ Agent Decision  │
 └─────────────────┘
          │
          ▼
 ┌─────────────────┐
 │ Incident Report │
 └─────────────────┘
          │
          ▼
 Human Approval Layer
```

---

## 🤖 Agentic Workflow

The system follows a decision-making loop similar to an autonomous AI agent:

### 1. Observe

Monitors:

- Feature distributions
- Model predictions
- Batch behavior
- Performance metrics

### 2. Detect

Identifies:

- Feature Drift
- Prediction Drift
- Distribution Shifts

### 3. Evaluate

Calculates:

- Population Stability Index (PSI)
- Drift Severity Levels
- Risk Classification

### 4. Decide

Determines whether the situation is:

- Stable
- Low Risk
- Medium Risk
- High Risk

### 5. Escalate

Generates structured incident reports and recommends next actions.

### 6. Human-in-the-Loop Governance

No automated intervention occurs without human approval.

---

## 📊 Dataset

### Default of Credit Card Clients Dataset

The project uses a real-world credit risk dataset containing customer payment behavior and default information.

Key characteristics:

- 30,000 customer records
- Credit risk prediction problem
- Binary target variable:
  - Default
  - No Default

This domain was selected because model failures in financial decision systems can have significant business and regulatory consequences.

---

## ⚙️ Technologies Used

### Programming

- Python

### Data Science

- Pandas
- NumPy
- Scikit-Learn

### Monitoring & Evaluation

- Population Stability Index (PSI)
- AUC (Area Under ROC Curve)

### Development

- Jupyter Notebook
- Git
- GitHub

---

## 🔍 Drift Detection Methodology

### Feature Drift

Population Stability Index (PSI) is calculated for every feature.

Drift Levels:

| PSI Value | Classification |
|------------|---------------|
| < 0.10 | Stable |
| 0.10 – 0.25 | Moderate Drift |
| > 0.25 | Severe Drift |

---

### Prediction Drift

The system compares prediction probability distributions between baseline and incoming production batches.

A significant shift may indicate changing model behavior.

---

### Performance Monitoring

The system tracks:

- Baseline AUC
- Current AUC
- AUC Degradation

to identify performance deterioration.

---

## 🚨 Risk Classification Logic

The monitoring agent automatically classifies risk levels.

### Stable

No significant drift detected.

### Low Risk

Minor drift requiring observation.

### Medium Risk

Multiple moderate drift signals detected.

### High Risk

Severe drift detected requiring escalation.

---

## 📄 Example Incident Report

```json
{
  "batch_risk_level": "High Risk",
  "decision": "Escalate: Significant feature and prediction drift detected.",
  "prediction_psi": 0.545,
  "auc_drop": 0.0156,
  "requires_human_approval": true
}
```

---

## 📸 Project Screenshots

### Data Understanding

(Add screenshot here)

### Baseline Model Performance

(Add screenshot here)

### Drift Detection Results

(Add screenshot here)

### Agent Risk Decision

(Add screenshot here)

### Incident Report Output

(Add screenshot here)

---

## 📁 Repository Structure

```text
agentic-model-risk-auditor/

├── data/
├── notebooks/
│   ├── 01_data_understanding.ipynb
│   ├── 02_baseline_model.ipynb
│   ├── 03_drift_simulation_and_detection.ipynb
│   └── 04_agent_decision_and_incident_report.ipynb
│
├── reports/
│   └── incidents/
│
├── src/
│   ├── __init__.py
│   ├── monitoring.py
│   └── utils.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

## ▶️ How To Run

### Clone Repository

```bash
git clone https://github.com/Anushka285/agentic-model-risk-auditor.git
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Monitoring

```bash
python main.py
```

The system will:

- Load the credit risk dataset
- Train a baseline model
- Simulate production drift
- Detect distribution changes
- Generate a risk assessment
- Produce an incident report

---

## 🎓 Key Learnings

Through this project I gained hands-on experience in:

- Model Risk Management
- AI Governance
- Drift Detection
- Production Monitoring Concepts
- Human-in-the-Loop Systems
- Credit Risk Analytics
- Machine Learning Operations (MLOps)

---

## 🔮 Future Improvements

Planned enhancements include:

- SHAP-based explainability
- Fairness monitoring
- Concept drift detection
- Streamlit dashboard
- Automated alerting
- MLflow integration
- Real-time monitoring pipelines

---

## 👩‍💻 Author

**Anushka Kadam**

Master's in Business Analytics  
University of North Texas

Passionate about Data Analytics, AI Systems, Machine Learning Monitoring, and Responsible AI.
