# 🛡️ Agentic Model Risk Auditor

### AI Governance System for Monitoring Model Drift, Risk Escalation, and Human Approval

🌐 **Live Demo:** https://agentic-model-risk-auditor.streamlit.app/

---

## Overview

Agentic Model Risk Auditor is an AI governance platform that simulates how organizations monitor machine learning models after deployment.

The system continuously evaluates incoming production data, detects feature and prediction drift, assesses operational risk, generates audit-ready incident reports, and routes high-risk situations through a Human-in-the-Loop approval workflow.

Unlike traditional monitoring dashboards that only display metrics, this system demonstrates an agentic decision process:

**Observe → Detect → Evaluate → Decide → Escalate → Human Approval**

---

## Business Problem

Machine learning models degrade over time as customer behavior, economic conditions, and data distributions evolve.

Without proper monitoring, model drift can lead to:

* Poor business decisions
* Financial losses
* Regulatory risk
* Reduced model reliability
* Compliance concerns

This project demonstrates how AI governance systems can identify these risks before they impact production decisions.

---

## Key Features

### 🏠 Executive Dashboard

* Real-time risk overview
* Drift severity monitoring
* Risk classification
* Approval status tracking
* Executive-level incident summary

### 📊 Drift Analysis

* Population Stability Index (PSI) monitoring
* Drift severity classification
* Feature-level drift investigation
* Visual drift analysis dashboard

### 🚨 Incident Reports

* Structured audit-ready reports
* Escalation rationale
* Governance requirements
* Investigation records

### 🤖 Agent Decision Engine

* Autonomous risk evaluation
* Escalation reasoning
* Recommended remediation actions
* Agentic decision workflow

### 👤 Human-in-the-Loop Governance

* Human approval workflow
* Escalation management
* Governance controls
* Production intervention safeguards

---

## System Workflow

```text
Production Data
       │
       ▼
Observe
       │
       ▼
Detect Drift
       │
       ▼
Evaluate Risk
       │
       ▼
Agent Decision
       │
       ▼
Incident Report
       │
       ▼
Human Approval
```

---

## Drift Detection Methodology

### Feature Drift

Population Stability Index (PSI) is used to compare incoming production data against baseline distributions.

| PSI Range   | Classification |
| ----------- | -------------- |
| < 0.10      | Stable         |
| 0.10 – 0.25 | Moderate Drift |
| > 0.25      | Severe Drift   |

### Prediction Drift

The system monitors changes in prediction distributions to identify model behavior shifts.

### Performance Monitoring

The monitoring layer tracks:

* Baseline AUC
* Drifted AUC
* Performance degradation
* Risk severity

---

## Technology Stack

Python • Streamlit • Pandas • NumPy • Scikit-Learn • Plotly • GitHub

---

### Monitoring & Governance

* Population Stability Index (PSI)
* Risk Classification Engine
* Human-in-the-Loop Approval Workflow

---

## Application Screens

### 🏠 Landing Page

(Add Home Page Screenshot)

### 📊 Executive Dashboard

(Add Dashboard Screenshot)

### 📈 Drift Analysis

(Add Drift Analysis Screenshot)

### 🚨 Incident Report

(Add Incident Report Screenshot)

### 🤖 Agent Decision

(Add Agent Decision Screenshot)

### 👤 Human Approval

(Add Human Approval Screenshot)

---

## Repository Structure

```text
agentic-model-risk-auditor/

├── data/
├── notebooks/
├── pages/
│   ├── Dashboard.py
│   ├── Drift_Analysis.py
│   ├── Incident_Reports.py
│   ├── Agent_Decision.py
│   └── Human_Approval.py
│
├── reports/
├── src/
│
├── app.py
├── requirements.txt
└── README.md
```

---

## Run Locally

Clone the repository:

```bash
git clone https://github.com/Anushka285/agentic-model-risk-auditor.git
cd agentic-model-risk-auditor
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Launch the application:

```bash
streamlit run app.py
```

---

## Skills Demonstrated

* Machine Learning Monitoring
* AI Governance
* Drift Detection
* Model Risk Management
* Human-in-the-Loop Systems
* Streamlit Application Development
* Responsible AI
* Risk Escalation Workflows

