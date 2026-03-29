# 🛡️ CompliantCare Foundry

### Regulatory-First Healthcare Data Platform

[![Python](https://img.shields.io/badge/Python-3.11-blue)]()
[![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)]()
[![FHIR](https://img.shields.io/badge/FHIR-R5-orange)]()
[![Docker](https://img.shields.io/badge/Docker-Enabled-blue)]()
[![License](https://img.shields.io/badge/License-MIT-yellow)]()

A **regulatory-first healthcare data platform** that ensures clinical datasets become **compliant, de-identified, interoperable, and analytics-ready** before any AI, machine learning, or research workflows begin.

This project implements a **privacy-by-design pipeline** aligned with:

* 🇮🇳 **India DPDP Act 2023**
* 🇺🇸 **HIPAA Safe Harbor**
* 🇪🇺 **GDPR Article 6 & 9**

The system transforms raw clinical data into **secure, standardized, and research-ready datasets** using modern healthcare interoperability standards such as **FHIR, ICD-10, and CPT**.

---

# 🚀 Key Features

### 🔐 Regulatory Compliance Engine

Automatically validates regulatory requirements across multiple jurisdictions.

Supports:

* **DPDP Act 2023 (India)**
* **HIPAA Privacy & Security Rules**
* **GDPR**

Features:

* compliance checklist generation
* regulatory audit artifacts
* readiness scorecard

---

### 🧹 De-Identification Engine

Implements **HIPAA Safe Harbor** style de-identification.

Capabilities:

* removal of direct identifiers
* masking PHI
* date shifting
* k-anonymity for quasi-identifiers

Protected identifiers include:

* names
* emails
* phone numbers
* MRNs
* IP addresses
* free-text notes

---

### 🔗 FHIR Interoperability Layer

Converts raw healthcare datasets into **FHIR R5 resources**.

Supported resources:

* `Patient`
* `Observation`
* `Condition`
* `Encounter`

This enables interoperability with:

* hospital EHR systems
* health information exchanges
* FHIR servers

---

### 🧠 Clinical Coding Engine

Validates medical codes and enables cohort building.

Supports:

* **ICD-10 diagnosis codes**
* **CPT procedure codes**

Capabilities:

* code validation
* cohort SQL generation
* FHIR cohort queries

---

### 🏥 Clinical Data Warehouse

Structured healthcare data storage using:

* **PostgreSQL**
* **SQLAlchemy ORM**

The warehouse enables:

* research queries
* cohort analysis
* ML feature engineering

---

### 🤖 Machine Learning Module

Demonstration ML pipeline for healthcare risk prediction.

Example model:

**Mortality Risk Prediction**

Uses:

* RandomForestClassifier
* patient demographics
* clinical features

---

### 📊 Analytics Dashboard

Interactive **Streamlit dashboard** for clinical analytics.

Features:

* patient statistics
* diagnosis distribution
* age histograms
* compliance indicators
* ML predictions

---

### 🌐 API Layer

FastAPI backend exposing healthcare data services.

Endpoints:

```
/generate-data
/run-pipeline
/compliance-check
/fhir-convert
/analysis-results
```

---

# 🏗️ System Architecture

```
Raw Clinical Data
        │
        ▼
Compliance Validation
        │
        ▼
De-Identification Engine
        │
        ▼
FHIR Conversion Layer
        │
        ▼
Clinical Coding Validation
        │
        ▼
Clinical Data Warehouse
        │
        ▼
ML Analytics Engine
        │
        ▼
API + Dashboard
```

---

# 📁 Project Structure

```
compliantcare-foundry
│
├── api/                     # FastAPI backend
├── compliance/              # regulatory compliance engine
├── privacy/                 # de-identification modules
├── datasets/                # dataset loaders (MIMIC etc.)
├── interoperability/        # FHIR converters
├── coding/                  # ICD-10 / CPT validation
├── warehouse/               # PostgreSQL models
├── ml/                      # machine learning models
├── pipeline/                # end-to-end orchestration
├── dashboard/               # Streamlit dashboard
├── orchestration/           # ETL pipelines
├── tests/                   # automated tests
│
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone the repository

```
git clone https://github.com/yourusername/compliantcare-foundry.git
cd compliantcare-foundry
```

---

## 2️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

## 3️⃣ Run the platform

```
docker compose up --build
```

---

# 🌐 Access the Services

API

```
http://localhost:8000
```

Dashboard

```
http://localhost:8501
```

---

# 📡 Example API Usage

Run pipeline:

```
GET /run-pipeline
```

Response:

```json
{
  "patients": 1000,
  "avg_age": 52.3
}
```

---

# 📊 Example Dashboard

The Streamlit dashboard provides:

* patient demographic insights
* diagnosis distribution
* ML prediction visualization
* compliance indicators

---

# 🔬 Real Dataset Integration

The platform supports integration with **real healthcare datasets** such as:

* **MIMIC-IV Clinical Database**
* hospital EHR exports
* clinical trial datasets
* HL7/FHIR feeds

Example location:

```
data/mimic/PATIENTS.csv
data/mimic/ADMISSIONS.csv
data/mimic/DIAGNOSES_ICD.csv
```

---

# 🧪 Testing

Run automated tests:

```
pytest
```

---

# 🛡️ Security & Compliance

This project demonstrates **privacy-by-design principles**.

Implemented safeguards:

* PHI masking
* regulatory validation
* audit trails
* safe data transformations

⚠️ This repository uses **synthetic or public datasets only**.

---

# 🚀 Roadmap

Future enhancements:

* full **HAPI FHIR server integration**
* **Airflow ETL orchestration**
* **Kafka healthcare event streaming**
* **LLM clinical note summarization**
* **ICD-10 auto-coding models**
* **Kubernetes deployment**
* **real-time hospital analytics**

---

# 🤝 Contributing

Contributions are welcome.

Steps:

```
fork repository
create feature branch
commit changes
open pull request
```

---

# 📜 License

MIT License

---

# 👨‍💻 Author

Built for **healthcare AI research, clinical analytics, and regulatory-compliant data pipelines**.

---

⭐ If you find this project useful, consider **starring the repository**.
