# KubeSRE AI

AI-Powered Kubernetes Root Cause Analysis and Observability Platform

## Overview

KubeSRE AI is a Python-based observability and incident analysis platform that collects Kubernetes pod status, logs, events, and Prometheus metrics, then uses Large Language Models (LLMs) to generate automated root cause analysis and remediation recommendations.

The project demonstrates how AI can be combined with Kubernetes observability data to assist SRE and DevOps teams in troubleshooting production incidents.

---

## Features

* Kubernetes Pod Monitoring
* Pod Status Collection
* Pod Log Collection
* Kubernetes Event Collection
* Prometheus Metrics Integration
* Restart Count Analysis
* Memory Usage Analysis
* AI-Powered Root Cause Analysis
* FastAPI REST Endpoints
* Incident Report Generation

---

## Architecture

Kubernetes Cluster
│
├── Pod Status
├── Logs
├── Events
└── Prometheus Metrics
│
▼
Python Collector
│
▼
incidents.json
│
▼
OpenRouter LLM
│
▼
Root Cause Analysis
│
▼
FastAPI API

---

## Tech Stack

* Python
* Kubernetes Python Client
* Prometheus
* Grafana
* FastAPI
* OpenRouter
* OpenAI SDK
* JSON

---

## Project Workflow

1. Collect Kubernetes Pod Information
2. Retrieve Pod Logs
3. Retrieve Kubernetes Events
4. Collect Prometheus Metrics
5. Generate Incident Data
6. Send Incident Context to LLM
7. Generate Root Cause Analysis
8. Return AI Recommendations

---

## Example Incident

Input:

```json
{
  "pod": "db-fail-demo",
  "status": "CrashLoopBackOff",
  "restart_count": 41,
  "memory_bytes": 15405056
}
```

Output:

```text
Root Cause:
Database connection failure during application startup.

Severity:
P1

Recommended Fix:
Verify database availability and application configuration.

Business Impact:
Potential application outage affecting dependent services.
```

---

## API Endpoints

### Health Check

GET /health

### Incidents

GET /incidents

### Analysis Results

GET /analysis

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd kubesre-ai
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure OpenRouter API Key

```bash
set OPENROUTER_API_KEY=your_api_key
```

### Run FastAPI

```bash
python -m uvicorn app:app --reload
```

### Access API

```text
http://127.0.0.1:8000/docs
```

---

## Sample Use Cases

* Kubernetes Troubleshooting
* Incident Investigation
* DevOps Learning
* SRE Automation
* AI-Assisted Root Cause Analysis
* Observability Experiments

---

## Future Enhancements

* CPU Metrics Integration
* Structured JSON RCA Output
* POST /analyze Endpoint
* Slack Notifications
* Grafana Dashboards
* Dependency Mapping
* Automated Remediation
* Multi-Agent Analysis

---

## Learning Outcomes

This project helped demonstrate:

* Kubernetes Troubleshooting
* Python Automation
* Observability Concepts
* Prometheus Integration
* FastAPI Development
* LLM Integration
* AI-Assisted Operations

---

## Author

Rohith Reddy

DevOps Engineer | Kubernetes | Cloud | AI for Infrastructure
